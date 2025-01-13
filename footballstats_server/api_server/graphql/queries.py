from datetime import date

import graphene
from django.contrib.auth.models import User
from django.db.models import QuerySet, Case, When, Max, Min

from api_server import constants
from api_server.models import Player, Team, Match, Country, EventType
from api_server.graphql._types.models import (
    PlayerType, MatchType, TeamType, UserType, LeagueType, LeagueSeasonType, CountryType, EventTypeType, MetricType
)
from api_server.graphql._types.utils import TextualFilterType, NumericalFilterType, MetricFilterType, SortingType


ERROR_FILTER_INVALID_NUMBER_OF_PARAMETERS: str = "Invalid number of parameters passed for filter!"
ERROR_INVALID_FILTERING_ATTRIBUTE: str = "Invalid filtering attribute!"
ERROR_INVALID_SORTING_ATTRIBUTE: str = "Invalid sorting attribute!"


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
                players = players.filter(id__in=match.get_players().values("id")).distinct()
        elif playing_in_match is not None:
            match = Match.objects.get(pk=playing_in_match)
            players = match.get_players().distinct()

        players = _filter_query_set_with_attributes(players, textual_filters, [], constants.PLAYER_FILTER_ATTRIBUTES)
        players = _filter_query_set_with_metrics(start_date, end_date, players, metric_filters)

        if sorting is None or sorting.target_attribute_name in constants.PLAYER_SORT_ATTRIBUTES:
            players = _sort_query_set_with_attributes(
                players,
                sorting if sorting is not None
                else ("surname", constants.SortingDirection.ASCENDING), 
            )
        elif str(sorting.target_attribute_name).split()[0] in constants.Metrics._member_names_:
            players = _sort_query_set_with_metric(players, sorting, start_date, end_date)
        else:
            raise ValueError(ERROR_INVALID_SORTING_ATTRIBUTE)

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
        result: dict[str, date] = Match.objects.aggregate(
            min_date=Min('game_date'),
            max_date=Max('game_date')
        )
        return [
            result['min_date'] if result['min_date'] is not None else date.today(), 
            result['max_date'] if result['max_date'] is not None else date.today()
        ]

    country_list: graphene.List = graphene.List(CountryType)
    def resolve_country_list(root, info: graphene.ResolveInfo) -> list[Country]:
        return Country.objects.all().order_by('name')

    event_types_list: graphene.List = graphene.List(EventTypeType)
    def resolve_event_types_list(root, info: graphene.ResolveInfo) -> list[EventType]:
        return EventType.objects.all().order_by('name')


def _sort_query_set_with_metric(
    query_set: QuerySet[Match | Player | Team | User],
    sorting_criteria: SortingType,
    start_date: date,
    end_date: date
) -> QuerySet:
    """
    Sorts given `QuerySet` accordingly to the passed sorting criteria and `id` field of underlying model.
    
    Elements with undefined values would be last!
    
    Param
    - `query_set` (`QuerySet`): The `QuerySet` that is to be sorted.
    - `sorting_criteria` (`SortingType`): Sorting criteria that consist of sorting metrics's name 
    and sorting direction.
    """
    metric_name, target_event, *metric_params = str(sorting_criteria.target_attribute_name).split()
    metric_values: list[tuple[int, float]] = []
    for object in query_set:
        if target_event not in constants.MatchEvents._member_names_:
            raise ValueError("Invalid target event for metric sorting!")
        metric_value: float = object.calculate_metric(
            start_date, 
            end_date, 
            constants.MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            constants.MetricScope.METRIC_FOR_ANY_TEAM.value,
            constants.Metrics[metric_name],
            constants.MatchEvents[target_event],
            [int(param) for param in metric_params]
        )
        metric_values.append((object.pk, metric_value))
    metric_values.sort(key=lambda x: x[1])

    metric_ordering: Case = Case(
        *[When(id=metric_value[0], then=position) for position, metric_value in enumerate(metric_values)]
    )
    return (
        query_set.order_by(metric_ordering, 'id') if sorting_criteria.direction == constants.SortingDirection.ASCENDING
        else query_set.order_by(metric_ordering, 'id').reverse()
    )


def _sort_query_set_with_attributes(
    query_set: QuerySet[Match | Player | Team | User], 
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
        sorting_criteria.direction if isinstance(sorting_criteria, SortingType)
        else sorting_criteria[1]
    )
    sorting_attribute: str = (
        sorting_criteria.target_attribute_name if isinstance(sorting_criteria, SortingType)
        else sorting_criteria[0]
    )
    sorting_expression: str = (
        f"{'-' if direction == constants.SortingDirection.DESCENDING else ''}"
        f"{sorting_attribute}"
    )
    return query_set.order_by(sorting_expression, 'id')


def _filter_query_set_with_attributes(
    query_set: QuerySet[Match | Player | Team | User], 
    textual_filters: list[TextualFilterType], 
    numeric_filters: list[NumericalFilterType],
    valid_filtering_attributes: list[str]
) -> QuerySet:
    """
    Sorts given `QuerySet` accordingly to passed textual and numeric filtering criteria. 
    It applies criteria sequentially in following order:
    
    1. Numeric filters
    2. Textural filters
    
    Params
    - `query_set` (`QuerySet`): Query set that would be filtered.
    - `textual_filters` (`list[TextualFilterType]`): Textual filters to be applied.
    - `numeric_filters` (`list[NumericalFilterType]`): Numerical filters to be applied.
    - `valid_filtering_attributes` (`list[str]`): List of valid filtering attributes.
    
    Return
    - `QuerySet`: Filtered `QuerySet`.
    """
    for textual_filter in textual_filters:
        if textual_filter.target_attribute_name not in valid_filtering_attributes:
            raise ValueError(ERROR_INVALID_FILTERING_ATTRIBUTE)
        match textual_filter.filtering_criteria:
            case constants.TextualFilteringCriteria.TEXTUAL_FULL_TEXT_SEARCH:
                if len(textual_filter.filter_params) != 1:
                    raise ValueError(ERROR_FILTER_INVALID_NUMBER_OF_PARAMETERS)
                query_set = query_set.filter(
                    **{f"{textual_filter.target_attribute_name}__startswith": textual_filter.filter_params[0]}
                )
            case constants.TextualFilteringCriteria.TEXTUAL_IN_SET:
                if len(textual_filter.filter_params) == 0:
                    raise ValueError(ERROR_FILTER_INVALID_NUMBER_OF_PARAMETERS)
                query_set = query_set.filter(
                    **{f"{textual_filter.target_attribute_name}__in": textual_filter.filter_params}
                )
            case constants.TextualFilteringCriteria.TEXTUAL_NOT_IN_SET:
                if len(textual_filter.filter_params) == 0:
                    raise ValueError(ERROR_FILTER_INVALID_NUMBER_OF_PARAMETERS)
                query_set = query_set.exclude(
                    **{f"{textual_filter.target_attribute_name}__in": textual_filter.filter_params}
                )
            case _:
                raise NotImplementedError("Provided textual filtering criteria does not exist!")
    return query_set.distinct()


def _filter_query_set_with_metrics(
    start_date: date,
    end_date: date,
    query_set: QuerySet[Match | Player | Team],
    metric_filters: list[MetricFilterType]
) -> QuerySet:
    """
    Sorts given `QuerySet` accordingly to passed metric filtering criteria.
    
    Params
    - `start_date` (`date`): Start date for metric calculations.
    - `end_date` (`date`): End date for metric calculations.
    - `query_set` (`QuerySet`): Query set that would be filtered.
    - `metric_filters` (`list[MetricFilterType]`): Metric filters to be applied.
    
    Return
    - `QuerySet`: Filtered `QuerySet`.
    """
    if len(metric_filters) == 0:
        return query_set
    metric_filter_qualified_objects_ids: set[int] = set()

    for metric_filter in metric_filters:
        current_metric_filter_qualified_objects_ids: set[int] = set()
        metric: MetricType = metric_filter.metric

        metric_values: list[tuple[int, float]] = []
        for object in query_set:
            metric_value: float = object.calculate_metric(
                start_date, 
                end_date, 
                constants.MetricScope.METRIC_FOR_ALL_MATCHES.value, 
                constants.MetricScope.METRIC_FOR_ANY_TEAM.value,
                metric.metric_type,
                metric.target_match_event,
                metric.metric_params
            )
            if metric_value == constants.METRIC_UNDEFINED_VALUE:
                continue
            metric_values.append((object.pk, metric_value))

        match metric_filter.filtering_criteria:
            case constants.NumericFilteringCriteria.NUMERIC_EQUALS:
                if len(metric_filter.filter_params) != 1:
                    raise ValueError(ERROR_FILTER_INVALID_NUMBER_OF_PARAMETERS)
                current_metric_filter_qualified_objects_ids = {
                    id for id, metric_value in metric_values if metric_value == metric_filter.filter_params[0]
                }
            case constants.NumericFilteringCriteria.NUMERIC_IN_CLOSED_RANGE:
                if len(metric_filter.filter_params) != 2:
                    raise ValueError(ERROR_FILTER_INVALID_NUMBER_OF_PARAMETERS)
                current_metric_filter_qualified_objects_ids = {
                    id for id, metric_value in metric_values
                    if metric_filter.filter_params[0] <= metric_value <= metric_filter.filter_params[1]
                }
            case constants.NumericFilteringCriteria.NUMERIC_NOT_IN_CLOSED_RANGE:
                if len(metric_filter.filter_params) != 2:
                    raise ValueError(ERROR_FILTER_INVALID_NUMBER_OF_PARAMETERS)
                current_metric_filter_qualified_objects_ids = {
                    id for id, metric_value in metric_values
                    if not (metric_filter.filter_params[0] <= metric_value <= metric_filter.filter_params[1])
                }
            case _:
                raise NotImplementedError("Provided numeric filtering criteria does not exist!")

        metric_filter_qualified_objects_ids = (
            metric_filter_qualified_objects_ids.intersection(current_metric_filter_qualified_objects_ids)
            if len(metric_filter_qualified_objects_ids)
            else metric_filter_qualified_objects_ids.union(current_metric_filter_qualified_objects_ids)
        )

    query_set = query_set.filter(id__in=metric_filter_qualified_objects_ids)
    return query_set.distinct()


def _get_page_from_query_set(query_set: QuerySet[Match | Player | Team | User], page_index: int) -> QuerySet:
    """
    Returns a subset of query set that is contained on a list's page with given index.
    
    Param
    - `query_set` (`QuerySet`): Query from which page would be retrieved.
    - `page_index` (`int`): Page index.
    
    Return
    - `QuerySet`: Sorted `QuerySet`.
    """
    first: int = constants.OBJECTS_PER_PAGE * page_index
    last: int = first + constants.OBJECTS_PER_PAGE

    if query_set.count() < first:
        return []
    elif query_set.count() > constants.OBJECTS_PER_PAGE:
        return query_set[first: last]
    return query_set