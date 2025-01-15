import graphene
from django.db.models import QuerySet
from graphene_django.forms.mutation import DjangoFormMutation
from graphql_jwt.decorators import login_required, user_passes_test

from api_server.constants import PermissionType
from api_server.forms import (
    RemovePlayerForm, 
    RemovePlayerFromMatchForm,
    RemoveMatchForm,
    RemoveTeamForm,
    RemovePlayerFromTeamForm,
    RemoveEventForm,
)
from api_server.auth.permissions import user_has_permission
from api_server.models import MatchEvent, PlayerInMatch, Team, Match, Player
from api_server.graphql.mutations._utils import convert_form_to_mutation_errors_response


ERROR_PLAYER_IS_NOT_REPRESENTING_TEAM: str = "Player is not representing this team in any match!"


class RemoveEventFromMatch(DjangoFormMutation):
    """
    Remove existing event from existing match.
    """
    class Meta:
        form_class = RemoveEventForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.DELETE))
    def perform_mutate(cls, form: RemoveEventForm, info: graphene.ResolveInfo):
        try:
            event = MatchEvent.objects.get(id=form.cleaned_data["event_id"])
        except MatchEvent.DoesNotExist as e:
            form.add_error("event_id", str(e))

        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_errors_response(form))

        event.delete()

        return cls(errors=[])


class RemovePlayerFromTeam(DjangoFormMutation):
    """
    Remove player from all team's matches.
    """
    class Meta:
        form_class = RemovePlayerFromTeamForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.DELETE))
    def perform_mutate(cls, form: RemovePlayerFromTeamForm, info: graphene.ResolveInfo):
        player_in_matches: QuerySet[PlayerInMatch] = PlayerInMatch.objects.filter(
            player=form.cleaned_data['player_id'], team=form.cleaned_data['team_id']
        )
        if player_in_matches.count() == 0:
            form.add_error(None, ERROR_PLAYER_IS_NOT_REPRESENTING_TEAM)

        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_errors_response(form))

        player_in_matches.delete()

        return cls(errors=[])


class RemoveTeam(DjangoFormMutation):
    class Meta:
        form_class = RemoveTeamForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.DELETE))
    def perform_mutate(cls, form: RemoveTeamForm, info: graphene.ResolveInfo):
        try:
            team = Team.objects.get(id=form.cleaned_data["team_id"])
        except Team.DoesNotExist as e:
            form.add_error("team_id", str(e))

        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_errors_response(form))

        team.delete()

        return cls(errors=[])


class RemoveMatch(DjangoFormMutation):
    class Meta:
        form_class = RemoveMatchForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.DELETE))
    def perform_mutate(cls, form: RemoveMatchForm, info: graphene.ResolveInfo):
        try:
            match = Match.objects.get(id=form.cleaned_data["match_id"])
        except Match.DoesNotExist as e:
            form.add_error("match_id", str(e))

        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_errors_response(form))

        match.delete()

        return cls(errors=[])


class RemovePlayer(DjangoFormMutation):
    class Meta:
        form_class = RemovePlayerForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.DELETE))
    def perform_mutate(cls, form: RemovePlayerForm, info: graphene.ResolveInfo):
        try:
            player = Player.objects.get(id=form.cleaned_data["player_id"])
        except Player.DoesNotExist as e:
            form.add_error("player_id", str(e))

        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_errors_response(form))

        player.delete()

        return cls(errors=[])


class RemovePlayerFromMatch(DjangoFormMutation):
    class Meta:
        form_class = RemovePlayerFromMatchForm

    @classmethod
    @login_required
    @user_passes_test(lambda user: user_has_permission(user.pk, PermissionType.DELETE))
    def perform_mutate(cls, form: RemovePlayerFromMatchForm, info: graphene.ResolveInfo):
        try:
            player_in_match = PlayerInMatch.objects.get(
                player__pk=form.cleaned_data["player"].pk,
                match__pk=form.cleaned_data["match"].pk
            )
        except PlayerInMatch.DoesNotExist as e:
            form.add_error(None, str(e))

        if not form.is_valid():
            return cls(errors=convert_form_to_mutation_errors_response(form))

        player_in_match.delete()

        return cls(errors=[])


