import graphene
from graphene_django.forms.mutation import DjangoFormMutation

from api_server.forms import (
    RemovePlayerForm, 
    RemovePlayerFromMatchForm,
    RemoveMatchForm,
    RemoveTeamForm,
    RemovePlayerFromTeam,
    RemoveEventForm,
)


class RemoveEventFromMatch(DjangoFormMutation):
    class Meta:
        form_class = RemoveEventForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class RemovePlayerFromTeam(DjangoFormMutation):
    class Meta:
        form_class = RemovePlayerFromTeam

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class RemoveTeam(DjangoFormMutation):
    class Meta:
        form_class = RemoveTeamForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class RemoveMatch(DjangoFormMutation):
    class Meta:
        form_class = RemoveMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class RemovePlayer(DjangoFormMutation):
    class Meta:
        form_class = RemovePlayerForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


class RemovePlayerFromMatch(DjangoFormMutation):
    class Meta:
        form_class = RemovePlayerFromMatchForm

    @classmethod
    def perform_mutate(cls, form, info: graphene.ResolveInfo):
        raise NotImplementedError
        return super().perform_mutate(form, info)


