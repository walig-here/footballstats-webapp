import graphene
from graphene_django.forms.mutation import DjangoFormMutation

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


class ModifyEventFromMatch(DjangoFormMutation):
    class Meta:
        form_class = ModifyEventForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class ModifyLeagueSeason(DjangoFormMutation):
    class Meta:
        form_class = ModifyLeagueSeasonForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class ModifyLeague(DjangoFormMutation):
    class Meta:
        form_class = ModifyLeagueForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class ModifyCountry(DjangoFormMutation):
    class Meta:
        form_class = ModifyCountryForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class ModifyTeam(DjangoFormMutation):
    class Meta:
        form_class = ModifyTeamForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class ModifyMatch(DjangoFormMutation):
    class Meta:
        form_class = ModifyMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)

class ModifyPlayer(DjangoFormMutation):
    class Meta:
        form_class = ModifyPlayerForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class ModifyPlayerMatchContribution(DjangoFormMutation):
    class Meta:
        form_class = ModifyPlayerMatchContributionForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)