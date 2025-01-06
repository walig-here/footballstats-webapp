from datetime import date

import graphene
from django.contrib.auth.models import User

from api_server.models import Player, Team, Match, Country, EventType
from api_server.graphql._types.models import (
    PlayerType, MatchType, TeamType, UserType, LeagueType, LeagueSeasonType, CountryType, EventTypeType
)
from api_server.graphql._types.utils import TextualFilterType, NumericalFilterType, MetricFilterType, SortingType


class PlayerQuery(graphene.ObjectType):
    player_sorting_attributes = graphene.List(graphene.String)
    def resolve_player_sorting_attributes(root, info: graphene.ResolveInfo) -> list[str]:
        raise NotImplementedError

    player_filtering_attributes = graphene.List(graphene.String)
    def resolve_player_filtering_attributes(root, info: graphene.ResolveInfo) -> list[str]:
        raise NotImplementedError

    player = graphene.Field(PlayerType, id=graphene.Int())
    def resolve_player(root, info: graphene.ResolveInfo, id: int) -> Player:
        raise NotImplementedError

    players_list = graphene.List(
        PlayerType,
        start_date=graphene.Date(),
        end_date=graphene.Date(),
        page=graphene.Int(),
        textual_filters=graphene.List(TextualFilterType, default_value=[]),
        numerical_filters=graphene.List(NumericalFilterType, default_value=[]),
        metric_filters=graphene.List(MetricFilterType, default_value=[]),
        sorting=SortingType(default_value=SortingType(target_attribute_name="SURNAME", direction=0)),
        representing_team=graphene.Int(default_value=None),
        playing_in_match=graphene.Int(default_value=None),
        ids=graphene.List(graphene.Int, default_value=[])
    )
    def resolve_players_list(
        root,
        info: graphene.ResolveInfo,
        start_date: date,
        end_date: date,
        page: int,
        textual_filters: list[TextualFilterType],
        numerical_filters: list[NumericalFilterType],
        metric_filters: list[MetricFilterType],
        sorting: list[SortingType],
        representing_team: int | None,
        playing_in_match: int | None,
        ids: list[int]
    ) -> list[Player]:
        raise NotImplementedError


class MatchQuery(graphene.ObjectType):
    match_sorting_attributes = graphene.List(graphene.String)
    def resolve_match_sorting_attributes(root, info: graphene.ResolveInfo) -> list[str]:
        raise NotImplementedError

    match_filtering_attributes = graphene.List(graphene.String)
    def resolve_match_filtering_attributes(root, info: graphene.ResolveInfo) -> list[str]:
        raise NotImplementedError

    match = graphene.Field(MatchType, id=graphene.Int())
    def resolve_match(root, info: graphene.ResolveInfo, id: int) -> Match:
        raise NotImplementedError

    matches_list: graphene.List = graphene.List(
        MatchType,
        start_date=graphene.Date(), 
        end_date=graphene.Date(),
        page=graphene.Int(),
        textual_filters=graphene.List(TextualFilterType, default_value=[]),
        numerical_filters=graphene.List(NumericalFilterType, default_value=[]),
        metric_filters=graphene.List(MetricFilterType, default_value=[]),
        sorting=SortingType(default_value=SortingType(target_attribute_name="DATE", direction=1)),
        team_involved=graphene.Int(default_value=None),
        player_involved=graphene.Int(default_value=None),
        ids=graphene.List(graphene.Int, default_value=[])
    )
    def resolve_matches_list(
        root, 
        info: graphene.ResolveInfo, 
        start_date: date,
        end_date: date,
        page: int,
        textual_filters: list[TextualFilterType],
        numerical_filters: list[NumericalFilterType],
        metric_filters: list[MetricFilterType],
        sorting: list[SortingType],
        team_involved: int | None,
        player_involved: int | None,
        ids: list[int]
    ) -> list[Match]:
        raise NotImplementedError


class TeamQuery(graphene.ObjectType):
    team_sorting_attributes = graphene.List(graphene.String)
    def resolve_team_sorting_attributes(root, info: graphene.ResolveInfo) -> list[str]:
        raise NotImplementedError

    team_filtering_attributes = graphene.List(graphene.String)
    def resolve_team_filtering_attributes(root, info: graphene.ResolveInfo) -> list[str]:
        raise NotImplementedError

    team = graphene.Field(TeamType, id=graphene.Int())
    def resolve_team(root, info: graphene.ResolveInfo, id: int) -> Team:
        raise NotImplementedError

    teams_list: graphene.List = graphene.List(
        TeamType,
        start_date=graphene.Date(), 
        end_date=graphene.Date(),
        page=graphene.Int(),
        textual_filters=graphene.List(TextualFilterType, default_value=[]),
        numerical_filters=graphene.List(NumericalFilterType, default_value=[]),
        metric_filters=graphene.List(MetricFilterType, default_value=[]),
        sorting=SortingType(default_value=SortingType(target_attribute_name="NAME", direction=0)),
        playing_in_match=graphene.Int(default_value=None),
        represented_by_player=graphene.Int(default_value=None),
        ids=graphene.List(graphene.Int, default_value=[])
    )
    def resolve_teams_list(
        root,
        info: graphene.ResolveInfo, 
        start_date: date, 
        end_date: date,
        page: int,
        textual_filters: list[TextualFilterType],
        numerical_filters: list[NumericalFilterType],
        metric_filters: list[MetricFilterType],
        sorting: list[SortingType],
        playing_in_match: int | None,
        represented_by_player: int | None,
        ids: list[int]
    ) -> list[Team]:
        raise NotImplementedError


class UserQuery(graphene.ObjectType):
    user_sorting_attributes = graphene.List(graphene.String)
    def resolve_user_sorting_attributes(root, info: graphene.ResolveInfo) -> list[str]:
        raise NotImplementedError

    user_filtering_attributes = graphene.List(graphene.String)
    def resolve_user_filtering_attributes(root, info: graphene.ResolveInfo) -> list[str]:
        raise NotImplementedError

    users_list: graphene.List = graphene.List(
        UserType,
        page=graphene.Int(),
        textual_filters=graphene.List(TextualFilterType, default_value=[]),
        numerical_filters=graphene.List(NumericalFilterType, default_value=[]),
        metric_filters=graphene.List(MetricFilterType, default_value=[]),
        sorting=SortingType(default_value=SortingType(target_attribute_name="USERNAME", direction=0))
    )
    def resolve_users_list(
        root,
        info: graphene.ResolveInfo, 
        start_date: date,
        end_date: date,
        page: int,
        textual_filters: list[TextualFilterType],
        numerical_filters: list[NumericalFilterType],
        sorting: list[SortingType]
    ) -> list[User]:
        raise NotImplementedError


class LeagueQuery(graphene.ObjectType):
    leagues_list: graphene.List = graphene.List(LeagueType)
    def resolve_list_of_leagues(self, info: graphene.ResolveInfo) -> list[LeagueType]:
        raise NotImplementedError

    league_seasons_list: graphene.List = graphene.List(LeagueSeasonType, league_id=graphene.Int())
    def resolve_list_league_seasons(self, info: graphene.ResolveInfo, league_id: int) -> list[LeagueSeasonType]:
        raise NotImplementedError


class MiscellaneousQuery(graphene.ObjectType):
    data_date_range: graphene.List = graphene.List(graphene.Date)
    def resolve_data_date_range(root, info: graphene.ResolveInfo) -> list[date]:
        raise NotImplementedError

    country_list: graphene.List = graphene.List(CountryType)
    def resolve_country_list(root, info: graphene.ResolveInfo) -> list[Country]:
        raise NotImplementedError

    event_types_list: graphene.List = graphene.List(EventTypeType)
    def resolve_event_type_list(root, info: graphene.ResolveInfo) -> list[EventType]:
        raise NotImplementedError