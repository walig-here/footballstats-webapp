import graphene
from graphene_django.forms.mutation import DjangoFormMutation

from api_server.forms import (
    AddTeamToMatchForm, 
    CreateLeagueForm, 
    CreateLeagueSeasonForm, 
    CreateMatchForm, 
    AddExistingPlayerToMatchForm, 
    CreateCountryForm, 
    AddNewPlayerToMatchForm, 
    AddEventToMatchForm, 
)


class AddEventToMatch(DjangoFormMutation):
    class Meta:
        form_class = AddEventToMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class AddNewPlayerToMatch(DjangoFormMutation):
    class Meta:
        form_class = AddNewPlayerToMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)

class CreateCountry(DjangoFormMutation):
    class Meta:
        form_class = CreateCountryForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class AddExistingPlayerToMatch(DjangoFormMutation):
    class Meta:
        form_class = AddExistingPlayerToMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class AddNewTeamToMatch(DjangoFormMutation):
    class Meta:
        form_class = AddTeamToMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class CreateLeagueSeason(DjangoFormMutation):
    class Meta:
        form_class = CreateLeagueSeasonForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class CreateLeague(DjangoFormMutation):
    class Meta:
        form_class = CreateLeagueForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class CreateMatch(DjangoFormMutation):
    class Meta:
        form_class = CreateMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)