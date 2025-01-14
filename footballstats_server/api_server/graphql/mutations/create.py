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
    CreatePlayerToMatchForm, 
    AddEventToMatchForm,
)
from api_server.auth.permissions import user_has_permission
from api_server.constants import PermissionType
from api_server.models import Team, Player, Match, PlayerInMatch


ERROR_PLAYER_ADDED_TO_MATCH_HAVE_NO_MINUTES_PLAYED: str = "Player have no minutes played info!"
ERROR_PLAYER_HAS_NON_NUMERIC_DATA: str = "Player's data contains non-numeric id or minutes played!"


def _snake_to_camel_case(snake_str: str):
    """
    Converts snake case to camel case.
    """
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


class AddEventToMatch(DjangoFormMutation):
    class Meta:
        form_class = AddEventToMatchForm

    @classmethod
    def perform_mutate(cls, form: AddEventToMatchForm, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class CreatePlayerToMatch(DjangoFormMutation):
    class Meta:
        form_class = CreatePlayerToMatchForm

    @classmethod
    def perform_mutate(cls, form: CreatePlayerToMatchForm, info: graphene.ResolveInfo):
        raise NotImplementedError
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
    class Meta:
        form_class = AddExistingPlayerToMatchForm

    @classmethod
    def perform_mutate(cls, form: AddExistingPlayerToMatchForm, info: graphene.ResolveInfo):
        raise NotImplementedError
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
                    lineups[team][1].append(((Player.objects.get(pk=player_id)), minutes_played))
                except Player.DoesNotExist as e2:
                    form.add_error(field=f"{team}_players", error=str(e2))
                except IndexError:
                    form.add_error(field=f"{team}_players", error=ERROR_PLAYER_ADDED_TO_MATCH_HAVE_NO_MINUTES_PLAYED)
                except ValueError:
                    form.add_error(field=f"{team}_players", error=ERROR_PLAYER_HAS_NON_NUMERIC_DATA)

        if not form.is_valid():
            return cls(errors=[
                {
                    "field": _snake_to_camel_case(field), 
                    "messages": [
                        data["message"] for data in payload
                    ]
                }
                for field, payload in form.errors.get_json_data().items()
            ])

        new_match: Match = form.save()

        for lineup in lineups.values():
            team: Team = lineup[0]
            for player_data in lineup[1]:
                PlayerInMatch(player=player_data[0], team=team, match=new_match, minutes_played=player_data[1]).save()

        return cls(errors=[])