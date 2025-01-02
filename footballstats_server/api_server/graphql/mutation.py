import graphene
from graphene_django.forms.mutation import DjangoFormMutation

from api_server.auth.mutation import AuthMutation
from api_server.forms import (
    AddTeamToMatchForm, 
    CreateLeagueForm, 
    CreateLeagueSeasonForm, 
    CreateMatchForm, 
    AddExistingPlayerToMatchForm, 
    CreateCountryForm, 
    AddNewPlayerToMatchForm, 
    AddEventToMatchForm, 
    ModifyPlayerMatchContributionForm, 
    RemovePlayerForm, 
    RemovePlayerFromMatchForm,
    ModifyPlayerForm,
    RemoveMatchForm,
    ModifyMatchForm
)


class _ModifyMatch(DjangoFormMutation):
    class Meta:
        form_class = ModifyMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class _RemoveMatch(DjangoFormMutation):
    class Meta:
        form_class = RemoveMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class _ModifyPlayer(DjangoFormMutation):
    class Meta:
        form_class = ModifyPlayerForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class _RemovePlayer(DjangoFormMutation):
    class Meta:
        form_class = RemovePlayerForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class _RemovePlayerFromMatch(DjangoFormMutation):
    class Meta:
        form_class = RemovePlayerFromMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class _AddEventToMatch(DjangoFormMutation):
    class Meta:
        form_class = AddEventToMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class _AddNewPlayerToMatch(DjangoFormMutation):
    class Meta:
        form_class = AddNewPlayerToMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)

class _CreateCountry(DjangoFormMutation):
    class Meta:
        form_class = CreateCountryForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class _ModifyPlayerMatchContribution(DjangoFormMutation):
    class Meta:
        form_class = ModifyPlayerMatchContributionForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class _AddExistingPlayerToMatch(DjangoFormMutation):
    class Meta:
        form_class = AddExistingPlayerToMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class _AddNewTeamToMatch(DjangoFormMutation):
    class Meta:
        form_class = AddTeamToMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class _CreateLeagueSeason(DjangoFormMutation):
    class Meta:
        form_class = CreateLeagueSeasonForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class _CreateLeague(DjangoFormMutation):
    class Meta:
        form_class = CreateLeagueForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class _CreateMatch(DjangoFormMutation):
    class Meta:
        form_class = CreateMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class Mutation(AuthMutation, graphene.ObjectType):
    add_new_team_to_match = _AddNewTeamToMatch.Field()
    add_existing_player_to_match = _AddExistingPlayerToMatch.Field()
    add_new_player_to_match = _AddNewPlayerToMatch.Field()
    add_event_to_match = _AddEventToMatch.Field()

    create_match = _CreateMatch.Field()
    create_league = _CreateLeague.Field()
    create_league_season = _CreateLeagueSeason.Field()
    create_country = _CreateCountry.Field()

    remove_player_from_match = _RemovePlayerFromMatch.Field()
    remove_player = _RemovePlayer.Field()
    remove_match = _RemoveMatch.Field()

    modify_player_match_contribution = _ModifyPlayerMatchContribution.Field()
    modify_player = _ModifyPlayer.Field()
    modify_match = _ModifyMatch.Field()