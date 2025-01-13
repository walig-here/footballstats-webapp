from datetime import date

import graphene
from django.contrib.auth.models import User
from django.db.models import QuerySet

from api_server import constants
from api_server.models import Player, Team, Match, Country, EventType
from api_server.graphql._types.models import (
    PlayerType, MatchType, TeamType, UserType, LeagueType, LeagueSeasonType, CountryType, EventTypeType
)
from api_server.graphql._types.utils import TextualFilterType, NumericalFilterType, MetricFilterType, SortingType


ERROR_FILTER_INVALID_NUMBER_OF_PARAMETERS: str = "Invalid number of parameters passed for filter!"


class PlayerQuery(graphene.ObjectType):
    player_sorting_attributes = graphene.List(graphene.String)
    def resolve_player_sorting_attributes(root, info: graphene.ResolveInfo) -> list[str]:
        """
        Returns names of all player's attributes that could be used for sorting.
        
        Return
        - `list[str]`: Names of all player's attributes that could be used for sorting.
        """
        return constants.PLAYER_SORT_ATTRIBUTES

    player_filtering_attributes = graphene.List(graphene.String)
    def resolve_player_filtering_attributes(root, info: graphene.ResolveInfo) -> list[str]:
        """
        Returns names of all player's attributes that could be used for filtering.
        
        Return
        - `list[str]`: Names of all player's attributes that could be used for filtering.
        """
        return constants.PLAYER_FILTER_ATTRIBUTES

    player = graphene.Field(PlayerType, id=graphene.Int())
    def resolve_player(root, info: graphene.ResolveInfo, id: int) -> Player:
        """
        Returns data of a single player with a given id.
        
        Param
        - `id` (`str`): Player's identifier.
        
        Return
        - `Player`: Player's data.
        """
        return Player.objects.get(pk=id)

    players_list = graphene.List(
        PlayerType,
        start_date=graphene.Date(),
        end_date=graphene.Date(),
        page=graphene.Int(),
        textual_filters=graphene.List(TextualFilterType, default_value=[]),
        metric_filters=graphene.List(MetricFilterType, default_value=[]),
        sorting=SortingType(default_value=None),
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
        metric_filters: list[MetricFilterType],
        sorting: SortingType,
        representing_team: int | None,
        playing_in_match: int | None,
        ids: list[int]
    ) -> list[Player]:
        players = (
            Player.objects
            .filter(playerinmatch__match__game_date__range=(start_date, end_date))
            .distinct()
        )

        if representing_team is not None:
            team = Team.objects.get(pk=representing_team)
            players = team.get_players(start_date, end_date)
            if playing_in_match is not None:
                match = Match.objects.get(pk=playing_in_match)
                players = players.filter(id__in=match.get_players().values("id"))
        elif playing_in_match is not None:
            match = Match.objects.get(pk=playing_in_match)
            players = match.get_players()

        players = _filter_query_set(players, textual_filters, [], metric_filters)
        players = _sort_query_set(
            players, 
            sorting if sorting is not None 
            else ("surname", constants.SortingDirection.ASCENDING), 
        )

        return _get_page_from_query_set(players, page)


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


def _sort_query_set(
    query_set: QuerySet, 
    sorting_criteria: SortingType | tuple[str, constants.SortingDirection]
) -> QuerySet:
    """
    Sorts given `QuerySet` accordingly to the passed sorting criteria and `id` field of underlying model.
    
    Param
    - `query_set` (`QuerySet`): The `QuerySet` that is to be sorted.
    - `sorting_criteria` (`SortingType | tuple[str, constants.SortingDirection]`): Sorting criteria that consist of
    sorting attribute's name and sorting direction.
    """
    direction: constants.SortingDirection = (
        sorting_criteria.direction if type(sorting_criteria) is SortingType
        else sorting_criteria[1]
    )
    sorting_attribute: str = (
        sorting_criteria.target_attribute_name if type(sorting_criteria) is SortingType
        else sorting_criteria[0]
    )
    sorting_expression: str = (
        f"{'-' if direction == constants.SortingDirection.DESCENDING else ''}"
        f"{sorting_attribute}"
    )
    return query_set.order_by(sorting_expression, 'id')


def _filter_query_set(
    query_set: QuerySet, 
    textual_filters: list[TextualFilterType], 
    numeric_filters: list[NumericalFilterType],
    metric_filters: list[MetricFilterType]
) -> QuerySet:
    """
    Sorts given `QuerySet` accordingly to passed filtering criteria. It applies criteria sequentially
    in following order:
    
    1. Textural filters
    2. Numeric filters
    3. Metric filters
    
    Params
    - `query_set` (`QuerySet`): Query set that would be filtered.
    - `textual_filters` (`list[TextualFilterType]`): Textual filters to be applied.
    - `numeric_filters` (`list[NumericalFilterType]`): Numerical filters to be applied.
    - `metric_filters` (`list[MetricFilterType]`): Metric filters to be applied.
    """
    for textual_filter in textual_filters:
        match textual_filter.filtering_criteria:
            case constants.TextualFilteringCriteria.TEXTUAL_FULL_TEXT_SEARCH:
                if len(textual_filter.filter_params) != 1:
                    raise ValueError(ERROR_FILTER_INVALID_NUMBER_OF_PARAMETERS)
                query_set = query_set.filter(
                    **{f"{textual_filter.target_attribute_name}__startswith": textual_filter.filter_params[0]}
                )
            case constants.TextualFilteringCriteria.TEXTUAL_IN_SET:
                query_set = query_set.filter(
                    **{f"{textual_filter.target_attribute_name}__in": textual_filter.filter_params}
                )
            case constants.TextualFilteringCriteria.TEXTUAL_NOT_IN_SET:
                query_set = query_set.exclude(
                    **{f"{textual_filter.target_attribute_name}__in": textual_filter.filter_params}
                )
            case _:
                raise NotImplementedError("Provided filtering criteria does not exist!")
    return query_set


def _get_page_from_query_set(query_set: QuerySet, page_index: int) -> QuerySet:
    """
    Returns a subset of query set that is contained on a list's page with given index.
    
    Param
    - `query_set` (`QuerySet`): Query from which page would be retrieved.
    - `page_index` (`int`): Page index.
    """
    first: int = constants.OBJECTS_PER_PAGE * page_index
    last: int = first + constants.OBJECTS_PER_PAGE

    if query_set.count() < first:
        return []
    elif query_set.count() > constants.OBJECTS_PER_PAGE:
        return query_set[first: last]
    return query_set