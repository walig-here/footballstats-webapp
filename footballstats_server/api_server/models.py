from datetime import date

from django.db import models
from django.contrib.auth.models import User, Permission
from django.dispatch import receiver

from api_server.constants import Metrics, MatchEvents, MATCH_LENGTH_MINUTES, METRIC_UNDEFINED_VALUE, MetricScope


class Country(models.Model):
    name: models.CharField = models.CharField(max_length=255, unique=True)
    flag_url: models.CharField = models.CharField(max_length=255, blank=True, null=True)


class League(models.Model):
    name: models.CharField = models.CharField(max_length=255, unique=True)
    country_of_origin: Country = models.ForeignKey(Country, models.PROTECT)
    logo_url: models.CharField = models.CharField(max_length=255, blank=True, null=True)


class LeagueSeason(models.Model):
    name: models.CharField = models.CharField(max_length=255)
    league: League = models.ForeignKey(League, models.PROTECT)

    class Meta:
        unique_together: list[str] = ["name", "league"]


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
                minutes_until_value: float | None = (
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


class AdminAction(models.Model):
    action_type: Permission = models.ForeignKey(Permission, models.PROTECT)
    user: User = models.ForeignKey(User, models.CASCADE)
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
            playerinmatch__match__game_date__gte=start, 
            playerinmatch__match__game_date__lte=end
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
        Calculations are based on matches' event.
        
        Params
        - `metric_type` (`Metrics`): Metric type.
        - `target_event` (`MatchEvents`): Targeted match event type.
        - `metric_params` (`list[str]`): Metric's parameters values.
        
        Raises
        - `ValueError`: When invalid metric parameters were passed.
        """
        match metric_type:
            case Metrics.SUM:
                targeted_player_events = MatchEvent.objects.filter(
                    player=self.pk, 
                    event_type=target_event.value,
                    match__game_date__gte=start,
                    match__game_date__lte=end
                )
                if match_id != MetricScope.METRIC_FOR_ALL_MATCHES:
                    targeted_player_events = targeted_player_events.filter(match=match_id)
                if team_id != MetricScope.METRIC_FOR_ANY_TEAM:
                    targeted_player_events = targeted_player_events.filter(
                        match__playerinmatch__player=self.pk,
                        match__playerinmatch__team=team_id
                    )
                return targeted_player_events.count()
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

                total_minutes_played: float = float(
                    PlayerInMatch.objects
                    .filter(player_id=self.pk, match__in=targeted_matches)
                    .aggregate(total_minutes=models.Sum('minutes_played'))['total_minutes']
                )
                return targeted_player_events_count / total_minutes_played


class PlayerAdminAction(models.Model):
    admin_action: models.OneToOneField = models.OneToOneField(AdminAction, models.CASCADE)
    player: Player = models.ForeignKey(Player, models.CASCADE)


class Team(models.Model):
    name: models.CharField = models.CharField(max_length=255, unique=True)
    country_of_origin: Country = models.ForeignKey(Country, models.PROTECT)
    logo_url: models.CharField = models.CharField(max_length=255, blank=True, null=True)

    def get_matches(self, start: date, end: date) -> models.QuerySet[Match]:
        raise NotImplementedError

    def get_players(self, start: date, end: date) -> models.QuerySet[Player]:
        raise NotImplementedError
    
    def get_admin_actions(self) -> models.QuerySet["TeamAdminAction"]:
        raise NotImplementedError

    def calculate_metric(
        self, 
        start: date, 
        end: date,
        match_id: int, 
        metric_type: Metrics, 
        target_event: MatchEvents,
        metric_params: list[int]
    ) -> float:
        raise NotImplementedError


class TeamAdminAction(models.Model):
    admin_action: AdminAction = models.OneToOneField(AdminAction, models.CASCADE)
    team: Team = models.ForeignKey(Team, models.CASCADE)


class PlayerInMatch(models.Model):
    player: Player = models.ForeignKey(Player, models.CASCADE)
    match: Match = models.ForeignKey(Match, models.CASCADE)
    team: Team = models.ForeignKey(Team, models.CASCADE)
    minutes_played: models.DecimalField = models.DecimalField(decimal_places=3, max_digits=10)


@receiver(models.signals.post_delete, sender=PlayerInMatch)
def _on_player_in_match_deleted(sender: models.base.Model, instance: PlayerInMatch, **kwargs: dict[str]) -> None:
    try:
        Match.objects.get(pk=instance.match.pk)
    except Match.DoesNotExist as e:
        return
    players_in_team: int = PlayerInMatch.objects.filter(team=instance.team, match=instance.match).count()
    if players_in_team == 0:
        instance.match.delete()


class EventType(models.Model):
    name: models.CharField = models.CharField(max_length=255)


class MatchEvent(models.Model):
    player: Player = models.ForeignKey(Player, models.CASCADE)
    match: Match = models.ForeignKey(Match, models.CASCADE)
    occurrence_minute: models.DecimalField = models.DecimalField(decimal_places=3, max_digits=10)
    event_type: EventType = models.ForeignKey(EventType, models.PROTECT)
