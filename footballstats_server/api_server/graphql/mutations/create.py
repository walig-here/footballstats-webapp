import graphene
from django.contrib.auth.models import User
from graphene_django.forms.mutation import DjangoFormMutation
from graphql_jwt.decorators import login_required, user_passes_test

from api_server.forms import (
    CreateTeamForm, 
    CreateLeagueForm, 
    CreateLeagueSeasonForm, 
    CreateMatchForm, 
    AddExistingPlayerToMatchForm, 
    CreateCountryForm, 
    CreatePlayerForm, 
    AddEventToMatchForm,
)
from api_server.auth.permissions import user_has_permission
from api_server.constants import PermissionType
from api_server.models import Team, Player, Match, PlayerInMatch
from api_server.graphql.mutations._utils import convert_form_to_mutation_error_response


ERROR_PLAYER_ADDED_TO_MATCH_HAVE_NO_MINUTES_PLAYED: str = "Player have no minutes played info!"
ERROR_PLAYER_HAS_NON_NUMERIC_DATA: str = "Player's data contains non-numeric id or minutes played!"
ERROR_PLAYER_ASSIGNED_TO_BOTH_TEAMS: str = "The same player is assigned to both teams!"
ERROR_PLAYER_ASSIGNED_TO_TEAM_NOT_TAKING_PART_IN_MATCH: str = "This team is not taking part in that match!"
ERROR_PLAYER_ALREADY_ASSIGNED_TO_MATCH: str = "Player already takes part in that match!"
ERROR_PLAYER_NOT_ASSIGNED_TO_MATCH: str = "Player is not taking part in this match!"


class AddEventToMatch(DjangoFormMutation):
    """
    Creates new event in system.
    
    Arguments
    - `player` (`int`): ID of player that initiated the event.
    - `match` (`int`): ID of match where event have taken place.
    - `occurrenceMinute` (`float`): Minute of match when event occurred.
    - `eventType` (`int`): ID of event type.
    """
    class Meta:
        form_class = AddEventToMatchForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.CREATE))
    def perform_mutate(cls, form: AddEventToMatchForm, info: graphene.ResolveInfo):
        player: Player = form.cleaned_data['player']
        match: Match = form.cleaned_data['match']

        if match.get_players().filter(pk=player.pk).count() == 0:
            form.add_error("player", ERROR_PLAYER_NOT_ASSIGNED_TO_MATCH)
        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_error_response(form))
        return super().perform_mutate(form, info)


class CreatePlayer(DjangoFormMutation):
    """
    Creates player in system.
    
    Arguments
    - `name` (`str`): Name. Should be uniq together with surname!
    - `surname` (`str`): Surname. Should be uniq together with name!
    - `nickname` (`str`): Nickname. Optional.
    - `country_of_origin` (`int`): ID of player's country of origin.
    - `profile_photo_url` (`str`): ULR of player's profile photo.
    """
    class Meta:
        form_class = CreatePlayerForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.CREATE))
    def perform_mutate(cls, form: CreatePlayerForm, info: graphene.ResolveInfo):
        return super().perform_mutate(form, info)

class CreateCountry(DjangoFormMutation):
    """
    Creates country in system.
    
    Arguments
    - `name` (`str`): Country name. Should be uniq!
    - `flag_url` (`str`): Country flag URL. Optional.
    """
    class Meta:
        form_class = CreateCountryForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.CREATE))
    def perform_mutate(cls, form: CreateCountryForm, info: graphene.ResolveInfo):
        return super().perform_mutate(form, info)


class AddExistingPlayerToMatch(DjangoFormMutation):
    """
    Adds existing player to given match as a repentant of a team that takes part in that match.
    
    Arguments
    - `player` (`int`): ID of player that's being added to match.
    - `match` (`int`): ID of match that we want to add player to.
    - `team` (`int`): ID of team that takes part in match that we want to add player to.
    - `minutes_played` (`float`): How many minutes player was playing in given match.
    """
    class Meta:
        form_class = AddExistingPlayerToMatchForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.CREATE))
    def perform_mutate(cls, form: AddExistingPlayerToMatchForm, info: graphene.ResolveInfo):
        match: Match = form.cleaned_data['match']
        team: Team = form.cleaned_data['team']
        player: Player = form.cleaned_data['player']

        if match.get_teams().filter(pk=team.pk).count() == 0:
            form.add_error("team", ERROR_PLAYER_ASSIGNED_TO_TEAM_NOT_TAKING_PART_IN_MATCH)
        if match.get_players().filter(pk=player.pk).count() > 0:
            form.add_error("player", ERROR_PLAYER_ALREADY_ASSIGNED_TO_MATCH)
        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_error_response(form))
        return super().perform_mutate(form, info)


class CreateTeam(DjangoFormMutation):
    """
    Creates new team in system and assigns it to Match.
    
    Arguments
    - `name` (`str`): Team's name. Should be uniq!
    - `country_of_origin` (`int`): ID of team's country of origin.
    - `logo_url` (`str`): URL to team's logo.
    """
    class Meta:
        form_class = CreateTeamForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.CREATE))
    def perform_mutate(cls, form: CreateTeamForm, info: graphene.ResolveInfo):
        return super().perform_mutate(form, info)


class CreateLeagueSeason(DjangoFormMutation):
    """
    Creates league's season in system.
    
    Arguments
    - `name` (`str`): League season's name. Should be uniq together with league name!
    - `league` (`int`): If of season's league.
    """
    class Meta:
        form_class = CreateLeagueSeasonForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.CREATE))
    def perform_mutate(cls, form: CreateLeagueSeasonForm, info: graphene.ResolveInfo):
        return super().perform_mutate(form, info)


class CreateLeague(DjangoFormMutation):
    """
    Creates league in system.
    
    Arguments
    - `name` (`str`): League's name. Should be uniq!
    - `country_of_origin` (`int`): ID of league's country of origin.
    - `logo_url` (`str`): Country flag URL. Optional.
    """
    class Meta:
        form_class = CreateLeagueForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.CREATE))
    def perform_mutate(cls, form: CreateLeagueForm, info: graphene.ResolveInfo):
        return super().perform_mutate(form, info)


class CreateMatch(DjangoFormMutation):
    """
    Creates match in system.
    
    Arguments
    - `game_date` (`date`): Matches' game date.
    - `league_season` (`int`): ID of season that match is a part of.
    - `home_team` (`int`): ID of home team.
    - `home_team_players` (`str`): String with whitespace-separated ID=<minutes_played> of home team's players.
    - `away_team` (`int`): ID of away team.
    - `away_team_players` (`str`): String with whitespace-separated ID=<minutes_played> of away team's players.
    """
    class Meta:
        form_class = CreateMatchForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.CREATE))
    def perform_mutate(cls, form: CreateMatchForm, info: graphene.ResolveInfo):
        lineups: dict[str, tuple[Team | None, list[tuple[Player, float]]]] = {
            "home_team": [None, []],
            "away_team": [None, []]
        }
        players_ids: set[int] = set() 

        for team in ("home_team", "away_team"):
            try:
                lineups[team][0] = Team.objects.get(pk=form.cleaned_data[team])
            except Team.DoesNotExist as e1:
                form.add_error(field=team, error=str(e1))

        for team in ("home_team", "away_team"):
            for player_data in form.cleaned_data[f"{team}_players"].split():
                try:
                    player_id: int = int(player_data.split("=")[0])
                    minutes_played: float = float(player_data.split("=")[1])
                    if player_id in players_ids:
                        form.add_error(field=f"{team}_players", error=ERROR_PLAYER_ASSIGNED_TO_BOTH_TEAMS)
                        continue
                    lineups[team][1].append(((Player.objects.get(pk=player_id)), minutes_played))
                    players_ids.add(player_id)
                except Player.DoesNotExist as e2:
                    form.add_error(field=f"{team}_players", error=str(e2))
                except IndexError:
                    form.add_error(field=f"{team}_players", error=ERROR_PLAYER_ADDED_TO_MATCH_HAVE_NO_MINUTES_PLAYED)
                except ValueError:
                    form.add_error(field=f"{team}_players", error=ERROR_PLAYER_HAS_NON_NUMERIC_DATA)

        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_error_response(form))

        new_match: Match = form.save()

        for lineup in lineups.values():
            team: Team = lineup[0]
            for player_data in lineup[1]:
                PlayerInMatch(player=player_data[0], team=team, match=new_match, minutes_played=player_data[1]).save()

        return cls(errors=[])