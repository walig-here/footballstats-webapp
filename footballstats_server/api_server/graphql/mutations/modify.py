import graphene
from graphene_django.forms.mutation import DjangoFormMutation
from graphql_jwt.decorators import login_required, user_passes_test

from api_server.constants import PermissionType
from api_server.forms import (
    ModifyPlayerMatchContributionForm, 
    ModifyPlayerForm,
    ModifyMatchForm,
    ModifyTeamForm,
    ModifyCountryForm,
    ModifyLeagueForm,
    ModifyLeagueSeasonForm,
    ModifyEventForm
)
from api_server.auth.permissions import user_has_permission
from api_server.models import MatchEvent, Player, LeagueSeason, League, Country, Team, Match, PlayerInMatch
from api_server.graphql.mutations._utils import convert_form_to_mutation_errors_response


ERROR_PLAYER_NOT_TAKING_PART_IN_MATCH: str = "Player is not taking part in this match!"
ERROR_SEASON_NAME_TO_UNIQ_WITHIN_LEAGUE: str = "Season name is not uniq within league!"
ERROR_TEAM_NOT_TAKING_PART_IN_THAT_MATCH: str = "Team is not taking part in that match!"
ERROR_PLAYER_IS_TEAM_LAST_PLAYER: str =  "Can't reassign team's last player!"


class ModifyEventFromMatch(DjangoFormMutation):
    """
    Edits data of existing match event.
    
    Arguments
    - `event_id` (`int`): ID of modified event.
    - `player` (`int`): ID of new player attached to event as its initiator.
    - `occurrence_minute` (`float`): New occurrence minute of the event.
    """
    class Meta:
        form_class = ModifyEventForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.EDIT))
    def perform_mutate(cls, form: ModifyEventForm, info: graphene.ResolveInfo):
        event_id: int = form.cleaned_data['event_id']
        player: Player = form.cleaned_data['player']

        try:
            event = MatchEvent.objects.get(id=event_id)
        except MatchEvent.DoesNotExist as e:
            form.add_error("match", str(e))
        try:
            event.match.get_players().get(id=player.pk)
        except Player.DoesNotExist as e:
            form.add_error("player", ERROR_PLAYER_NOT_TAKING_PART_IN_MATCH)
        
        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_errors_response(form))

        event.player = form.cleaned_data['player']
        event.occurrence_minute = form.cleaned_data.get('occurrence_minute')
        event.save()

        return cls(errors=[])


class ModifyLeagueSeason(DjangoFormMutation):
    """
    Edits data of existing season.
    
    Arguments
    - `league_season_id` (`int`): ID of modified season.
    - `name` (`str`): New name. Must be uniq with league!
    """
    class Meta:
        form_class = ModifyLeagueSeasonForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.EDIT))
    def perform_mutate(cls, form: ModifyLeagueSeasonForm, info: graphene.ResolveInfo):
        season_id: int = form.cleaned_data['league_season_id']
        new_name: str = form.cleaned_data['name']

        try:
            season = LeagueSeason.objects.get(id=season_id)
        except LeagueSeason.DoesNotExist as e:
            form.add_error("match", str(e))
        if LeagueSeason.objects.filter(name=new_name, league__pk=season.league.pk).count() > 0:
            form.add_error("name", ERROR_SEASON_NAME_TO_UNIQ_WITHIN_LEAGUE)
        
        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_errors_response(form))

        season.name = new_name
        season.save()

        return cls(errors=[])


class ModifyLeague(DjangoFormMutation):
    """
    Edits data of existing league.
    
    Arguments
    - `league_id` (`int`): ID of modified league.
    - `name` (`str`): New name. Must be uniq!
    - `countryOfOrigin` (`int`): ID of league's new country of origin.
    - `logoUrl` (`str`): New logo URL.
    """
    class Meta:
        form_class = ModifyLeagueForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.EDIT))
    def perform_mutate(cls, form: ModifyLeagueForm, info: graphene.ResolveInfo):
        league_id: int = form.cleaned_data['league_id']
        new_name: str = form.cleaned_data['name']

        try:
            league = League.objects.get(id=league_id)
        except League.DoesNotExist as e:
            form.add_error("league", str(e))
        try:
            new_country: Country = Country.objects.get(pk=form.cleaned_data['country_of_origin'].pk)
        except League.DoesNotExist as e:
            form.add_error("countryOfOrigin", str(e))
        
        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_errors_response(form))

        league.name = new_name
        league.country_of_origin = new_country
        league.logo_url = form.cleaned_data['logo_url']
        league.save()

        return cls(errors=[])


class ModifyCountry(DjangoFormMutation):
    """
    Edits data of existing country.
    
    Arguments
    - `country_id` (`int`): ID of modified country.
    - `name` (`str`): New name. Must be uniq!
    - `flagUrl` (`str`): New flag URL.
    """
    class Meta:
        form_class = ModifyCountryForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.EDIT))
    def perform_mutate(cls, form: ModifyCountryForm, info: graphene.ResolveInfo):
        country_id: int = form.cleaned_data['country_id']
        new_name: str = form.cleaned_data['name']

        try:
            country = Country.objects.get(id=country_id)
        except Country.DoesNotExist as e:
            form.add_error("country_id", str(e))
        
        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_errors_response(form))

        country.name = new_name
        country.flag_url = form.cleaned_data['flag_url']
        country.save()

        return cls(errors=[])


class ModifyTeam(DjangoFormMutation):
    """
    Edits data of existing country.
    
    Arguments
    - `team_id` (`int`): ID of modified team.
    - `name` (`str`): New name. Must be uniq!
    - `country_of_origin` (`int`): ID of league's new country of origin.
    - `logo_url` (`str`): New logo URL.
    """
    class Meta:
        form_class = ModifyTeamForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.EDIT))
    def perform_mutate(cls, form: ModifyTeamForm, info: graphene.ResolveInfo):
        team_id: int = form.cleaned_data['team_id']
        new_name: str = form.cleaned_data['name']

        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist as e:
            form.add_error("league", str(e))
        
        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_errors_response(form))

        team.name = new_name
        team.country_of_origin = form.cleaned_data['country_of_origin']
        team.logo_url = form.cleaned_data['logo_url']
        team.save()

        return cls(errors=[])


class ModifyMatch(DjangoFormMutation):
    """
    Edits data of existing match.
    
    Arguments
    - `match_id` (`int`): ID of modified match.
    - `game_date` (`date`): New game date.
    - `league_season` (`int`): ID of new season.
    """
    class Meta:
        form_class = ModifyMatchForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.EDIT))
    def perform_mutate(cls, form: ModifyMatchForm, info: graphene.ResolveInfo):
        match_id: int = form.cleaned_data['match_id']

        try:
            match = Match.objects.get(id=match_id)
        except Match.DoesNotExist as e:
            form.add_error("match_id", str(e))
        
        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_errors_response(form))

        match.game_date = form.cleaned_data['game_date']
        match.league_season = form.cleaned_data['league_season']
        match.save()

        return cls(errors=[])

class ModifyPlayer(DjangoFormMutation):
    """
    Edits data of existing player.
    
    Arguments
    - `player_id` (`int`): ID of modified match.
    - `name` (`str`): New name. Have to be uniq with surname.
    - `surname` (`str`): New surname. Have to be uniq with name.
    - `nickname` (`str`): New nickname.
    - `country_of_origin` (`int`): ID of new season.
    - `profile_photo_url` (`str`): URL of profile photo.
    """
    class Meta:
        form_class = ModifyPlayerForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.EDIT))
    def perform_mutate(cls, form: ModifyPlayerForm, info: graphene.ResolveInfo):
        player_id: int = form.cleaned_data['player_id']

        try:
            player = Player.objects.get(id=player_id)
        except Player.DoesNotExist as e:
            form.add_error("player_id", str(e))
        
        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_errors_response(form))

        player.name = form.cleaned_data['name']
        player.surname = form.cleaned_data['surname']
        player.nickname = form.cleaned_data['nickname']
        player.profile_photo_url = form.cleaned_data['profile_photo_url']
        player.country_of_origin = form.cleaned_data['country_of_origin']
        player.save()

        return cls(errors=[])


class ModifyPlayerMatchContribution(DjangoFormMutation):
    """
    Edits data of existing player.
    
    Arguments
    - `player_id` (`int`): ID of modified player.
    - `match_id` (`int`): ID of modified match.
    - `team` (`int`): ID of players new team. This team needs to be playing in this match.
    - `minutes_played` (`float`): New minutes played.
    """
    class Meta:
        form_class = ModifyPlayerMatchContributionForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.EDIT))
    def perform_mutate(cls, form: ModifyPlayerMatchContributionForm, info: graphene.ResolveInfo):
        player_id: int = form.cleaned_data['player_id']
        match_id: int = form.cleaned_data['match_id']
        team: Team = form.cleaned_data['team']

        try:
            player_in_match = PlayerInMatch.objects.get(player=player_id, match=match_id)
        except PlayerInMatch.DoesNotExist as e:
            form.add_error(None, str(e))
        if Match.objects.get(pk=match_id).get_teams().filter(pk=team.pk).count() == 0:
            form.add_error("team", ERROR_TEAM_NOT_TAKING_PART_IN_THAT_MATCH)
        elif PlayerInMatch.objects.filter(match=match_id, team=player_in_match.team).exclude(player=player_id).count() == 0:
            form.add_error(None, ERROR_PLAYER_IS_TEAM_LAST_PLAYER)
        
        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_errors_response(form))

        player_in_match.team = form.cleaned_data['team']
        player_in_match.minutes_played = form.cleaned_data['minutes_played']
        player_in_match.save()

        return cls(errors=[])