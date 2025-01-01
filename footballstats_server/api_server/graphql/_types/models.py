from datetime import date

import graphene
from django.contrib.auth.models import User
from django.db.models import Model
from graphene_django import DjangoObjectType

from api_server.models import (
    Player, Team, Match, LeagueSeason, League, MatchEvent, MatchAdminAction, EventType, Country, TeamAdminAction,
    AdminAction
)
from api_server.graphql._types.utils import MetricType


class CountryType(DjangoObjectType):
    class Meta:
        model: Model = Country
        fields: tuple[str] = ("name", "flag_url")


class EventTypeType(DjangoObjectType):
    class Meta:
        model: Model = EventType
        fields: str = "__all__"


class MatchEventType(DjangoObjectType):
    class Meta:
        model: Model = MatchEvent
        fields: str = "__all__"


class LeagueType(DjangoObjectType):
    class Meta:
        model: Model = League
        fields: str = "__all__"


class LeagueSeasonType(DjangoObjectType):
    class Meta:
        model: Model = LeagueSeason
        fields: str = "__all__"


class PlayerType(DjangoObjectType):
    class Meta:
        model: Model = Player
        fields: str = "__all__"

    calculate_metric: graphene.Float = graphene.Float(
        start_date=graphene.Date(), 
        end_date=graphene.Date(),
        match=graphene.Int(required=True), 
        metric=MetricType(required=True),
    )
    def resolve_calculate_metric(
        self, 
        info: graphene.ResolveInfo, 
        start_date: date,
        end_date: date,
        match: int,
        metric: MetricType,
    ) -> float:
        raise NotImplementedError

    metric_history: graphene.List = graphene.List(
        graphene.Float,
        start_date=graphene.Date(), 
        end_date=graphene.Date(),
        metric=MetricType(required=True)
    )
    def resolve_metric_history(
        self, 
        info: graphene.ResolveInfo, 
        start_date: date,
        end_date: date,
        metric: MetricType
    ) -> list[float]:
        raise NotImplementedError

class TeamMatchScore(graphene.ObjectType):
    score: graphene.Int = graphene.Int()
    def resolve_score(self, info: graphene.ResolveInfo) -> graphene.Int:
        raise NotImplementedError
    
    id: graphene.Int = graphene.Int()
    def resolve_id(self, info: graphene.ResolveInfo) -> int:
        raise NotImplementedError


class AdminActionType(DjangoObjectType):
    class Meta:
        model: Model = AdminAction
        fields: str = "__all__"


class MatchAdminActionType(DjangoObjectType):
    class Meta:
        model: Model = MatchAdminAction
        fields: str = "__all__"


class MatchType(DjangoObjectType):
    class Meta:
        model: Model = Match
        fields: str = "__all__"

    events: graphene.List = graphene.List(MatchEventType)
    def resolve_events(self, info: graphene.ResolveInfo) -> graphene.List:
        raise NotImplementedError

    teams_scores: graphene.List = graphene.List(TeamMatchScore)
    def resolve_teams(self, info: graphene.ResolveInfo) -> graphene.List:
        raise NotImplementedError

    admin_actions: graphene.List = graphene.List(MatchAdminActionType)
    def resolve_admin_actions(self, info: graphene.ResolveInfo) -> graphene.List:
        raise NotImplementedError

    calculate_metric: graphene.Float = graphene.Float(
        metric=MetricType(required=True),
        target_player_id=graphene.Int(default_value=None),
    )
    def resolve_calculate_metric(
        self, 
        info: graphene.ResolveInfo,
        metric: MetricType,
        target_player_id: int | None
    ) -> float:
        raise NotImplementedError


class TeamAdminActionType(DjangoObjectType):
    class Meta:
        model: Model = TeamAdminAction
        fields: str = "__all__"


class TeamType(DjangoObjectType):
    class Meta:
        model: Model = Team
        fields: str = "__all__"

    admin_actions: graphene.List = graphene.List(TeamAdminActionType)
    def resolve_admin_actions(self, info: graphene.ResolveInfo) -> graphene.List:
        raise NotImplementedError

    calculate_metric: graphene.Float = graphene.Float(
        start_date=graphene.Date(), 
        end_date=graphene.Date(),
        match=graphene.Int(required=True),
        metric=MetricType(required=True)
    )
    def resolve_calculate_metric(
        self, 
        info: graphene.ResolveInfo, 
        start_date: date,
        end_date: date,
        match: int, 
        metric: MetricType
    ) -> float:
        raise NotImplementedError

    metric_history: graphene.List = graphene.List(
        graphene.Float,
        start_date=graphene.Date(), 
        end_date=graphene.Date(),
        metric=MetricType(required=True)
    )
    def resolve_metric_history(
        self, 
        info: graphene.ResolveInfo, 
        start_date: date,
        end_date: date,
        metric: MetricType
    ) -> list[float]:
        raise NotImplementedError


class UserType(DjangoObjectType):
    class Meta:
        model: Model = User
        fields: tuple[str] = ("id", "username", "is_superuser")