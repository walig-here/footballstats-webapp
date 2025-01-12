from datetime import date
from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User, Permission
from django.dispatch import receiver

from api_server.constants import Metrics, MatchEvents, MATCH_LENGTH_MINUTES, METRIC_UNDEFINED_VALUE, MetricScope

def _delete_country_if_it_is_not_referenced_by_any_object(country: "Country") -> None:
    country_of_origin: Country = Country.objects.get(pk=country.pk)
    objects_referencing_team_country: int = (
        League.objects.filter(country_of_origin=country_of_origin).count() +
        Team.objects.filter(country_of_origin=country_of_origin).count() +
        Player.objects.filter(country_of_origin=country_of_origin).count()
    )
    if objects_referencing_team_country == 0:
        country_of_origin.delete()


class Country(models.Model):
    name: models.CharField = models.CharField(max_length=255, unique=True)
    flag_url: models.CharField = models.CharField(max_length=255, blank=True, null=True)


class League(models.Model):
    name: models.CharField = models.CharField(max_length=255, unique=True)
    country_of_origin: Country = models.ForeignKey(Country, models.PROTECT)
    logo_url: models.CharField = models.CharField(max_length=255, blank=True, null=True)


@receiver(models.signals.post_delete, sender=League)
def _after_delete_on_league(sender: models.base.Model, instance: League, **kwargs: dict[str]) -> None:
    try:
        _delete_country_if_it_is_not_referenced_by_any_object(instance.country_of_origin)
    except Country.DoesNotExist:
        return


class LeagueSeason(models.Model):
    name: models.CharField = models.CharField(max_length=255)
    league: League = models.ForeignKey(League, models.PROTECT)

    class Meta:
        unique_together: list[str] = ["name", "league"]


@receiver(models.signals.post_delete, sender=LeagueSeason)
def _after_delete_on_league_season(sender: models.base.Model, instance: LeagueSeason, **kwargs: dict[str]) -> None:
    league: League = instance.league
    if LeagueSeason.objects.filter(league=league).count() == 0:
        league.delete()


class Match(models.Model):
    game_date: models.DateField = models.DateField()
    league_season: LeagueSeason = models.ForeignKey(LeagueSeason, models.PROTECT)

    def get_players(self) -> models.QuerySet["Player"]:
        """
        Returns all players that participate in match. They are sorted by their full name.
        """
        return Player.objects.filter(playerinmatch__match_id=self.pk).order_by('name', 'surname')

    def get_teams(self) -> models.QuerySet["Team"]:
        """
        Returns all teams that participate in match. They are sorted by their name.
        """
        return Team.objects.filter(playerinmatch__match_id=self.pk).distinct().order_by('name')

    def get_events(self) -> models.QuerySet["MatchEvent"]:
        """
        Returns all events that occurred in match. They are sorted by their minute of occurrence.
        """
        return MatchEvent.objects.filter(match_id=self.pk).order_by('occurrence_minute', 'id')
    
    def get_result(self) -> dict["Team", int]:
        """
        Get score of both teams that participated in match.
        
        Return
        - `dict[Team, int]`: Map where key is team and value is its score.
        """
        events = self.get_events()
        return {
            team: events.filter(event_type_id=MatchEvents.GOAL.value, player__playerinmatch__team__id=team.pk).count()
            for team in self.get_teams()
        }
    
    def get_admin_actions(self) -> models.QuerySet["MatchAdminAction"]:
        """
        Get all admin actions performed against the match. They are sorted by their date.
        """
        return MatchAdminAction.objects.filter(match__id=self.pk)

    def calculate_metric(
        self, metric_type: Metrics, target_event: MatchEvents, metric_params: list[int]
    ) -> float:
        """
        Calculates a value for given metric type that targets some kind of match event.
        Calculations are based on matches' event.
        
        Params
        - `metric_type` (`Metrics`): Metric type.
        - `target_event` (`MatchEvents`): Targeted match event type.
        - `metric_params` (`list[str]`): Metric's parameters values.
        
        Return:
        - `-1.0`: When value of metric is undefined.
        - `> -1.0`: Metric value. 
        
        Raises
        - `ValueError`: When invalid metric parameters were passed.
        """
        NOT_NEEDED_PARAMS_ERROR: str = f"Not needed metric params passed. Passed params: {metric_params}"
        
        if len(metric_params) > 0 and metric_type not in (Metrics.ODDS_FOR_MORE_THAN, Metrics.ODDS_IN_TIME_RANGE):
            raise ValueError(NOT_NEEDED_PARAMS_ERROR)

        def _calculate_odd_for_more_than(amount: int) -> float:
            id_of_matches_with_more_than = (
                MatchEvent.objects
                .filter(event_type_id=target_event.value)
                .values('match_id')
                .annotate(event_count=models.Count('id'))
                .filter(event_count__gt=amount)
                .values('match_id')
            )
            return Match.objects.filter(id=self.pk, id__in=id_of_matches_with_more_than).count() * 100.0

        match metric_type:
            case Metrics.ODDS_FOR:
                return _calculate_odd_for_more_than(0)
            case Metrics.SUM:
                return MatchEvent.objects.filter(match_id=self.pk, event_type_id=target_event.value).count()
            case Metrics.AVERAGE:
                return self.calculate_metric(Metrics.SUM, target_event, []) / MATCH_LENGTH_MINUTES
            case Metrics.MINUTES_UNTIL:
                minutes_until_value: Decimal | None = (
                    MatchEvent.objects
                    .filter(match_id=self.pk, event_type_id=target_event.value)
                    .aggregate(min_occurrence_minute=models.Min('occurrence_minute'))['min_occurrence_minute']
                )
                return float(minutes_until_value) if minutes_until_value is not None else METRIC_UNDEFINED_VALUE
            case Metrics.ODDS_FOR_MORE_THAN:
                if len(metric_params) > 1:
                    raise ValueError(NOT_NEEDED_PARAMS_ERROR)

                return _calculate_odd_for_more_than(int(metric_params[0]))
            case Metrics.ODDS_IN_TIME_RANGE:
                if len(metric_params) > 2:
                    raise ValueError(NOT_NEEDED_PARAMS_ERROR)
                lower_bound: float = float(metric_params[0])
                upper_bound: float = float(metric_params[1])
                all_target_events_count: int = self.calculate_metric(Metrics.SUM, target_event, [])
                if all_target_events_count == 0:
                    return 0.0

                return MatchEvent.objects.filter(
                    match_id=self.pk, 
                    event_type_id=target_event.value, 
                    occurrence_minute__gte=lower_bound, 
                    occurrence_minute__lte=upper_bound
                ).count() / all_target_events_count
            case _:
                raise NotImplementedError


@receiver(models.signals.post_delete, sender=Match)
def _after_delete_on_match(sender: models.base.Model, instance: Match, **kwargs: dict[str]) -> None:
    try:
        season: LeagueSeason = instance.league_season
    except LeagueSeason.DoesNotExist:
        return
    if Match.objects.filter(league_season=season).count() == 0:
        season.delete()


class AdminAction(models.Model):
    action_type: Permission = models.ForeignKey(Permission, models.PROTECT)
    user: User = models.ForeignKey(User, models.SET_NULL, null=True)
    action_date: models.DateField = models.DateField()


class MatchAdminAction(models.Model):
    admin_action: AdminAction = models.OneToOneField(AdminAction, models.CASCADE)
    match: Match = models.ForeignKey(Match, models.CASCADE)


class Player(models.Model):
    name: models.CharField = models.CharField(max_length=255)
    surname: models.CharField = models.CharField(max_length=255)
    nickname: models.CharField = models.CharField(max_length=255, blank=True, null=True)
    country_of_origin: Country = models.ForeignKey(Country, models.PROTECT)
    profile_photo_url: models.CharField = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together: list[str] = ["name", "surname"]

    def get_matches(self, start: date, end: date) -> models.QuerySet[Match]:
        """
        Returns all matches from given date range that player participated in.
        """
        return Match.objects.filter(playerinmatch__player_id=self.pk, game_date__gte=start, game_date__lte=end)

    def get_teams(self, start: date, end: date) -> models.QuerySet["Team"]:
        """
        Returns all teams from given date range that player participated in.
        """
        return Team.objects.filter(
            playerinmatch__player=self.pk, 
            playerinmatch__match__game_date__range=(start, end)
        ).distinct()
    
    def get_admin_actions(self) -> models.QuerySet["PlayerAdminAction"]:
        """
        Returns all admin actions performed against the player.
        """
        return PlayerAdminAction.objects.filter(player=self.pk)

    def calculate_metric(
        self, 
        start: date, 
        end: date,
        match_id: int, 
        team_id: int, 
        metric_type: Metrics, 
        target_event: MatchEvents, 
        metric_params: list[int], 
    ) -> float:
        """
        Calculates a value for given metric type that targets some kind of match event.
        Calculations are based on events initiated by player in its matches.
        
        Params
        - `metric_type` (`Metrics`): Metric type.
        - `target_event` (`MatchEvents`): Targeted match event type.
        - `metric_params` (`list[str]`): Metric's parameters values.
        
        Return:
        - `-1.0`: When value of metric is undefined.
        - `> -1.0`: Metric value. 
        
        Raises
        - `ValueError`: When invalid metric parameters were passed.
        """
        NOT_NEEDED_PARAMS_ERROR: str = f"Not needed metric params passed. Passed params: {metric_params}"

        if len(metric_params) > 0 and metric_type not in (Metrics.ODDS_FOR_MORE_THAN, Metrics.ODDS_IN_TIME_RANGE):
            raise ValueError(NOT_NEEDED_PARAMS_ERROR)

        def _calculate_odds_for_more_than(amount: int) -> float:
            all_matches: models.QuerySet[Match] = self.get_matches(start, end)
            if match_id != MetricScope.METRIC_FOR_ALL_MATCHES:
                all_matches = all_matches.filter(pk=match_id)
            if team_id != MetricScope.METRIC_FOR_ANY_TEAM:
                all_matches = all_matches.filter(playerinmatch__team=team_id, playerinmatch__player=self.pk)
            targeted_matches_count: int = (
                all_matches
                .filter(matchevent__event_type=target_event.value, matchevent__player=self.pk)
                .annotate(event_count=models.Count('matchevent'))
                .filter(event_count__gt=amount)
                .count()
            )
            all_matches_count: int = all_matches.count()
            if all_matches_count == 0:
                return 0.0
            return targeted_matches_count / all_matches_count * 100.0
        
        match metric_type:
            case Metrics.SUM:
                player_target_events: models.QuerySet[MatchEvent] = MatchEvent.objects.filter(
                    player=self.pk, 
                    event_type=target_event.value,
                    match__game_date__range=(start, end)
                )
                if match_id != MetricScope.METRIC_FOR_ALL_MATCHES:
                    player_target_events = player_target_events.filter(match=match_id)
                if team_id != MetricScope.METRIC_FOR_ANY_TEAM:
                    player_target_events = player_target_events.filter(
                        match__playerinmatch__player=self.pk,
                        match__playerinmatch__team=team_id
                    )
                return player_target_events.count()
            case Metrics.AVERAGE:
                targeted_player_events_count: float = self.calculate_metric(
                    start, end, match_id, team_id, Metrics.SUM, target_event, []
                )

                targeted_matches: models.QuerySet[Match] = self.get_matches(start, end).values('id')
                if match_id != MetricScope.METRIC_FOR_ALL_MATCHES:
                    targeted_matches = targeted_matches.filter(pk=match_id)
                if team_id != MetricScope.METRIC_FOR_ANY_TEAM:
                    targeted_matches = targeted_matches.filter(
                        playerinmatch__player=self.pk,
                        playerinmatch__team=team_id
                    )

                total_minutes_played: Decimal | None = (
                    PlayerInMatch.objects
                    .filter(player_id=self.pk, match__in=targeted_matches)
                    .aggregate(total_minutes=models.Sum('minutes_played'))['total_minutes']
                )
                if total_minutes_played is None or total_minutes_played == 0.0:
                    return 0.0
                return targeted_player_events_count / float(total_minutes_played)
            case Metrics.ODDS_FOR:
                return _calculate_odds_for_more_than(0)
            case Metrics.ODDS_FOR_MORE_THAN:
                if len(metric_params) != 1:
                    raise ValueError(NOT_NEEDED_PARAMS_ERROR)
                return _calculate_odds_for_more_than(int(metric_params[0]))
            case Metrics.MINUTES_UNTIL:
                player_target_events: models.QuerySet[MatchEvent] = MatchEvent.objects.filter(
                    player=self.pk, 
                    event_type=target_event.value,
                    match__game_date__range=(start, end)
                )
                if match_id != MetricScope.METRIC_FOR_ALL_MATCHES:
                    player_target_events = player_target_events.filter(match=match_id)
                if team_id != MetricScope.METRIC_FOR_ANY_TEAM:
                    player_target_events = player_target_events.filter(
                        match__playerinmatch__player=self.pk,
                        match__playerinmatch__team=team_id
                    )
                minutes_until: Decimal | None = (
                    player_target_events
                    .aggregate(min_occurrence_minute=models.Min('occurrence_minute'))['min_occurrence_minute']
                )
                return float(minutes_until) if minutes_until is not None else METRIC_UNDEFINED_VALUE
            case Metrics.ODDS_IN_TIME_RANGE:
                if len(metric_params) != 2:
                    raise ValueError(NOT_NEEDED_PARAMS_ERROR)
                lower_bound: float = float(metric_params[0])
                upper_bound: float = float(metric_params[1])
                
                player_target_events: models.QuerySet[MatchEvent] = MatchEvent.objects.filter(
                    player=self.pk, 
                    match__game_date__range=(start, end),
                    event_type=target_event.value
                )
                if match_id != MetricScope.METRIC_FOR_ALL_MATCHES:
                    player_target_events = player_target_events.filter(match=match_id)
                if team_id != MetricScope.METRIC_FOR_ANY_TEAM:
                    player_target_events = player_target_events.filter(
                        match__playerinmatch__player=self.pk,
                        match__playerinmatch__team=team_id
                    )

                player_target_events_from_range: models.QuerySet[MatchEvent] = (
                    player_target_events.filter(occurrence_minute__range=(lower_bound, upper_bound))
                )
                player_target_events_count: int = player_target_events.count()
                return (
                    player_target_events_from_range.count() / player_target_events_count 
                    if player_target_events_count != 0
                    else 0.0
                )
            case _:
                raise NotImplementedError


@receiver(models.signals.post_delete, sender=Player)
def _after_delete_on_player(sender: models.base.Model, instance: Player, **kwargs: dict[str]) -> None:
    try:
        _delete_country_if_it_is_not_referenced_by_any_object(instance.country_of_origin)
    except Country.DoesNotExist:
        return


class PlayerAdminAction(models.Model):
    admin_action: models.OneToOneField = models.OneToOneField(AdminAction, models.CASCADE)
    player: Player = models.ForeignKey(Player, models.CASCADE)


class Team(models.Model):
    name: models.CharField = models.CharField(max_length=255, unique=True)
    country_of_origin: Country = models.ForeignKey(Country, models.PROTECT)
    logo_url: models.CharField = models.CharField(max_length=255, blank=True, null=True)

    def get_matches(self, start: date, end: date) -> models.QuerySet[Match]:
        """
        Gets all matches that team participated in. Sorted by game date.
        """
        return (
            Match.objects
            .filter(playerinmatch__team=self.pk, game_date__range=(start, end))
            .distinct()
            .order_by('game_date')
        )

    def get_players(self, start: date, end: date) -> models.QuerySet[Player]:
        """
        Gets all players that have ever represented team in any match. Sorted by full name.
        """
        return (
            Player.objects
            .filter(playerinmatch__team=self.pk, playerinmatch__match__game_date__range=(start, end))
            .distinct()
            .order_by('name', 'surname')
        )
    
    def get_admin_actions(self) -> models.QuerySet["TeamAdminAction"]:
        """
        Gets all admin actions that have been performed against team.
        """
        return TeamAdminAction.objects.filter(team=self.pk)

    def calculate_metric(
        self, 
        start: date, 
        end: date,
        match_id: int, 
        metric_type: Metrics, 
        target_event: MatchEvents,
        metric_params: list[int]
    ) -> float:
        """
        Calculates a value for given metric type that targets some kind of match event.
        Calculations are based on events initiated by players that represented team in some matches.
        
        Params
        - `metric_type` (`Metrics`): Metric type.
        - `target_event` (`MatchEvents`): Targeted match event type.
        - `metric_params` (`list[str]`): Metric's parameters values.
        
        Return:
        - `-1.0`: When value of metric is undefined.
        - `> -1.0`: Metric's value. 
        
        Raises
        - `ValueError`: When invalid metric parameters were passed.
        """
        INVALID_NUMBER_OF_PARAMS: str = f"Invalid number of params passed. Passed params: {metric_params}"

        if len(metric_params) > 0 and metric_type not in (Metrics.ODDS_FOR_MORE_THAN, Metrics.ODDS_IN_TIME_RANGE):
            raise ValueError(INVALID_NUMBER_OF_PARAMS)
        
        def _calculate_odd_for_more_than(amount: int) -> float:
            all_matches: models.QuerySet[Match] = self.get_matches(start, end)
            targeted_matches: models.QuerySet[Match] = (
                Match.objects
                .filter(
                    game_date__range=(start, end),
                    playerinmatch__team=self.pk,
                    playerinmatch__player=models.F('matchevent__player'),
                    matchevent__event_type=target_event.value
                )
                .annotate(event_count=models.Count('matchevent'))
                .filter(event_count__gt=amount)
            )

            if match_id != MetricScope.METRIC_FOR_ALL_MATCHES:
                all_matches = all_matches.filter(pk=match_id)
                targeted_matches = targeted_matches.filter(id=match_id)

            all_matches_count: int = all_matches.count()
            if all_matches_count == 0:
                return 0.0
            return targeted_matches.count() / all_matches_count * 100.0
        
        match metric_type:
            case Metrics.SUM:
                team_targeted_events: models.QuerySet[MatchEvent] = (
                    MatchEvent.objects
                    .filter(
                        match__game_date__range=(start, end),
                        match__playerinmatch__team=self.pk,
                        event_type=target_event.value,
                        match__playerinmatch__player_id=models.F('player_id')
                    )
                )
                if match_id != MetricScope.METRIC_FOR_ALL_MATCHES:
                    team_targeted_events = team_targeted_events.filter(match=match_id)
                return team_targeted_events.count()
            case Metrics.AVERAGE:
                targeted_team_events_count: float = self.calculate_metric(
                    start, end, match_id, Metrics.SUM, target_event, []
                )

                targeted_matches: models.QuerySet[Match] = self.get_matches(start, end)
                if match_id != MetricScope.METRIC_FOR_ALL_MATCHES:
                    targeted_matches = targeted_matches.filter(pk=match_id)
                
                targeted_matches_count: int = targeted_matches.count()
                return (
                    targeted_team_events_count / (targeted_matches_count * MATCH_LENGTH_MINUTES)
                    if targeted_matches_count != 0
                    else 0.0
                )
            case Metrics.ODDS_FOR:
                return _calculate_odd_for_more_than(0)
            case Metrics.ODDS_FOR_MORE_THAN:
                if len(metric_params) != 1:
                    raise ValueError(INVALID_NUMBER_OF_PARAMS)
                return _calculate_odd_for_more_than(int(metric_params[0]))
            case Metrics.MINUTES_UNTIL:
                team_targeted_events: models.QuerySet[MatchEvent] = (
                    MatchEvent.objects
                    .filter(
                        match__game_date__range=(start, end),
                        match__playerinmatch__team=self.pk,
                        event_type=target_event.value,
                        match__playerinmatch__player_id=models.F('player_id')
                    )
                )
                if match_id != MetricScope.METRIC_FOR_ALL_MATCHES:
                    team_targeted_events = team_targeted_events.filter(match=match_id)
                
                minutes_until: Decimal | None = (
                    team_targeted_events
                    .aggregate(min_occurrence_minute=models.Min('occurrence_minute'))['min_occurrence_minute']
                )
                return float(minutes_until) if minutes_until is not None else METRIC_UNDEFINED_VALUE
            case Metrics.ODDS_IN_TIME_RANGE:
                if len(metric_params) != 2:
                    raise ValueError(INVALID_NUMBER_OF_PARAMS)
                lower_bound: float = float(metric_params[0])
                upper_bound: float = float(metric_params[1])

                team_targeted_events_from_match: models.QuerySet[MatchEvent] = (
                    MatchEvent.objects
                    .filter(
                        match__game_date__range=(start, end),
                        match__playerinmatch__team=self.pk,
                        event_type=target_event.value,
                        match__playerinmatch__player_id=models.F('player_id')
                    )
                )
                if match_id != MetricScope.METRIC_FOR_ALL_MATCHES:
                    team_targeted_events_from_match = team_targeted_events_from_match.filter(match=match_id)

                team_targeted_events_from_range: models.QuerySet[MatchEvent] = (
                    team_targeted_events_from_match
                    .filter(occurrence_minute__range=(lower_bound, upper_bound))
                )

                return (
                    team_targeted_events_from_range.count() / team_targeted_events_from_match.count()
                    if team_targeted_events_from_match.count() != 0
                    else 0.0
                )
            case _:
                raise NotImplementedError


@receiver(models.signals.post_delete, sender=Team)
def _after_delete_on_team(sender: models.base.Model, instance: Team, **kwargs: dict[str]) -> None:
    try:
        _delete_country_if_it_is_not_referenced_by_any_object(instance.country_of_origin)
    except Country.DoesNotExist:
        return

class TeamAdminAction(models.Model):
    admin_action: AdminAction = models.OneToOneField(AdminAction, models.CASCADE)
    team: Team = models.ForeignKey(Team, models.CASCADE)


class PlayerInMatch(models.Model):
    player: Player = models.ForeignKey(Player, models.CASCADE)
    match: Match = models.ForeignKey(Match, models.CASCADE)
    team: Team = models.ForeignKey(Team, models.CASCADE)
    minutes_played: models.DecimalField = models.DecimalField(decimal_places=3, max_digits=10)


@receiver(models.signals.post_delete, sender=PlayerInMatch)
def _after_delete_on_player_in_match(sender: models.base.Model, instance: PlayerInMatch, **kwargs: dict[str]) -> None:
    def _delete_matches_with_empty_teams() -> None:
        try:
            Match.objects.get(pk=instance.match.pk)
        except Match.DoesNotExist:
            return
        try:
            Team.objects.get(pk=instance.team.pk)
            players_in_team: int = PlayerInMatch.objects.filter(team=instance.team, match=instance.match).count()
            if players_in_team == 0:
                instance.match.delete()
        except Team.DoesNotExist:
            instance.match.delete()

    def _delete_players_with_no_matches() -> None:
        try:
            Player.objects.get(pk=instance.player.pk)
        except Player.DoesNotExist:
            return
        if len(instance.player.get_matches(date.min, date.max)) == 0:
            instance.player.delete()

    def _delete_teams_with_no_matches() -> None:
        try:
            Team.objects.get(pk=instance.team.pk)
        except Team.DoesNotExist:
            return
        if len(instance.team.get_matches(date.min, date.max)) == 0:
            instance.team.delete()
    
    _delete_teams_with_no_matches()
    _delete_matches_with_empty_teams()
    _delete_players_with_no_matches()


class EventType(models.Model):
    name: models.CharField = models.CharField(max_length=255)


class MatchEvent(models.Model):
    player: Player = models.ForeignKey(Player, models.CASCADE)
    match: Match = models.ForeignKey(Match, models.CASCADE)
    occurrence_minute: models.DecimalField = models.DecimalField(decimal_places=3, max_digits=10)
    event_type: EventType = models.ForeignKey(EventType, models.PROTECT)
