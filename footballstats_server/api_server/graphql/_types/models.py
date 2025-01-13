from datetime import date

import graphene
from django.contrib.auth.models import User, Permission
from django.db.models import Model
from graphene_django import DjangoObjectType

from api_server import constants
from api_server.models import (
    Player, Team, Match, LeagueSeason, League, MatchEvent, MatchAdminAction, EventType, Country, TeamAdminAction, PlayerAdminAction,
    AdminAction
)
from api_server.graphql._types.utils import MetricType


class AdminActionTypeType(DjangoObjectType):
    class Meta:
        model = Permission
        fields = ("name", )


class CountryType(DjangoObjectType):
    class Meta:
        model: Model = Country
        fields: tuple[str] = "__all__"


class EventTypeType(DjangoObjectType):
    class Meta:
        model: Model = EventType
        fields: str = "__all__"


class MetricHistoryPointType(graphene.ObjectType):
    value = graphene.Float()
    time = graphene.Date()


class MatchEventType(DjangoObjectType):
    class Meta:
        model: Model = MatchEvent
        exclude: str = ("match", "id")


class LeagueType(DjangoObjectType):
    class Meta:
        model: Model = League
        fields: str = "__all__"


class LeagueSeasonType(DjangoObjectType):
    class Meta:
        model: Model = LeagueSeason
        fields: str = "__all__"


class PlayerAdminActionType(DjangoObjectType):
    class Meta:
        model = PlayerAdminAction
        exclude: str = ("player", "id")


class PlayerType(DjangoObjectType):
    class Meta:
        model: Model = Player
        fields: str = "__all__"

    admin_actions: graphene.List = graphene.List(PlayerAdminActionType)
    def resolve_admin_actions(self, info: graphene.ResolveInfo) -> graphene.List:
        return PlayerAdminAction.objects.filter(player=self.id)

    calculate_metric: graphene.Float = graphene.Float(
        start_date=graphene.Date(), 
        end_date=graphene.Date(),
        match=graphene.Int(required=True),
        team=graphene.Int(required=True),
        metric=MetricType(required=True),
    )
    def resolve_calculate_metric(
        self, 
        info: graphene.ResolveInfo, 
        start_date: date,
        end_date: date,
        match: int,
        team: int,
        metric: MetricType,
    ) -> float:
        return Player.objects.get(pk=self.id).calculate_metric(
            start_date, end_date, match, team, metric.metric_type, metric.target_match_event, metric.metric_params
        )

    metric_history: graphene.List = graphene.List(
        MetricHistoryPointType,
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
    ) -> list[MetricHistoryPointType]:
        player: Player = Player.objects.get(pk=self.id)

        dates: list[date] = [
            match.game_date
            for match in player.get_matches(start_date, end_date)
        ]
        dates.insert(0, start_date)
        dates.append(end_date)

        return [
            MetricHistoryPointType(
                value=player.calculate_metric(
                    start_date, 
                    current_date,
                    constants.MetricScope.METRIC_FOR_ALL_MATCHES.value, 
                    constants.MetricScope.METRIC_FOR_ANY_TEAM.value, 
                    metric.metric_type,  
                    metric.target_match_event, 
                    metric.metric_params
                ),
                time=current_date
            )
            for current_date in dates
        ]

class TeamMatchScore(graphene.ObjectType):
    score: graphene.Int = graphene.Int()
    def resolve_score(self, info: graphene.ResolveInfo) -> graphene.Int:
        raise NotImplementedError
    
    team_id: graphene.Int = graphene.Int()
    def resolve_team_id(self, info: graphene.ResolveInfo) -> int:
        raise NotImplementedError


class AdminActionType(DjangoObjectType):
    class Meta:
        model: Model = AdminAction
        fields: str = ("action_type", "user", "action_date")


class MatchAdminActionType(DjangoObjectType):
    class Meta:
        model: Model = MatchAdminAction
        exclude: str = ("match", "id")


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
        exclude: str = ("team", "id")


class TeamType(DjangoObjectType):
    class Meta:
        model: Model = Team
        fields: str = "__all__"

    admin_actions: graphene.List = graphene.List(TeamAdminActionType)
    def resolve_admin_actions(self, info: graphene.ResolveInfo) -> graphene.List:
        return TeamAdminAction.objects.filter(team=self.id)

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
        return Team.objects.get(pk=self.id).calculate_metric(
            start_date, end_date, match, metric.metric_type, metric.target_match_event, metric.metric_params
        )

    metric_history: graphene.List = graphene.List(
        MetricHistoryPointType,
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
        team: Team = Team.objects.get(pk=self.id)

        dates: list[date] = [
            match.game_date
            for match in team.get_matches(start_date, end_date)
        ]
        dates.insert(0, start_date)
        dates.append(end_date)

        return [
            MetricHistoryPointType(
                value=team.calculate_metric(
                    start_date, 
                    current_date,
                    constants.MetricScope.METRIC_FOR_ALL_MATCHES.value, 
                    metric.metric_type,  
                    metric.target_match_event, 
                    metric.metric_params
                ),
                time=current_date
            )
            for current_date in dates
        ]


class UserType(DjangoObjectType):
    class Meta:
        model: Model = User
        fields: tuple[str] = ("id", "username", "is_superuser")