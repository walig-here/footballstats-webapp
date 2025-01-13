from django.test import TestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema

from api_server.tests.integration.__data__.graphql.queries import PlayerQuery as data
from api_server.tests import testconf as global_testconf


class Test__QueryForPlayerList__Sort(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_country_of_origin_name_descending(self):
        response: dict = self.client.execute(
            data.LIST_OF_PLAYERS_QUERY__DESCENDING_SORT_COUNTRY_OF_ORIGIN_NAME,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.LIST_OF_PLAYERS_RESPONSE__DESCENDING_SORT_COUNTRY_OF_ORIGIN_NAME)

    def test_sum_goals_ascending(self):
        response: dict = self.client.execute(
            data.LIST_OF_PLAYERS_QUERY__ASCENDING_SORT_ON_SUM_GOALS,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.LIST_OF_PLAYERS_RESPONSE__ASCENDING_SORT_ON_SUM_GOALS)

    def test_minutes_until_goal_descending(self):
        response: dict = self.client.execute(
            data.LIST_OF_PLAYERS_QUERY__DESCENDING_SORT_ON_MINUTES_UNTIL_GOAL,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.LIST_OF_PLAYERS_RESPONSE__DESCENDING_SORT_ON_MINUTES_UNTIL_GOAL)

    def test_odds_for_more_than_1_goal_ascending(self):
        ...


class Test__QueryForPlayerList__UnsortedMetricFilters(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_sum_shot_not_on_target_equals(self):
        response: dict = self.client.execute(
            data.LIST_OF_PLAYERS_QUERY__FILTER_SUM_SHOT_NOT_ON_TARGET_EQUALS,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.LIST_OF_PLAYERS_RESPONSE__FILTER_SUM_SHOT_NOT_ON_TARGET_EQUALS)

    def test_odds_for_goals_for_in_closed_range(self):
        response: dict = self.client.execute(
            data.LIST_OF_PLAYERS_QUERY__FILTER_ODDS_FOR_GOAL_IN_CLOSED_RANGE,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.LIST_OF_PLAYERS_RESPONSE__FILTER_ODDS_FOR_GOAL_IN_CLOSED_RANGE)

    def test_minutes_until_yellow_card_not_in_closed_range(self):
        response: dict = self.client.execute(
            data.LIST_OF_PLAYERS_QUERY__FILTER_MINUTES_UNTIL_YELLOW_CARD_NOT_IN_CLOSED_RANGE,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(
            response, 
            data.LIST_OF_PLAYERS_RESPONSE__FILTER_MINUTES_UNTIL_YELLOW_CARD_NOT_IN_CLOSED_RANGE
        )

    def test_conjunction_of_metric_filters(self):
        response: dict = self.client.execute(
            data.LIST_OF_PLAYERS_QUERY__CONJUNCTION_OF_METRIC_FILTERS,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(
            response, 
            data.LIST_OF_PLAYERS_RESPONSE__CONJUNCTION_OF_METRIC_FILTERS
        )


class Test__QueryForPlayerList__UnsortedTextualFilters(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_league_name_full_text_search(self):
        response: dict = self.client.execute(
            data.LIST_OF_PLAYERS_QUERY__FULL_TEXT_SEARCH_LEAGUE_NAME,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.LIST_OF_PLAYERS_RESPONSE__FULL_TEXT_SEARCH_LEAGUE_NAME)

    def test_league_name_full_in_set(self):
        response: dict = self.client.execute(
            data.LIST_OF_PLAYERS_QUERY__IN_SET_LEAGUE_NAME,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.LIST_OF_PLAYERS_RESPONSE__IN_SET_LEAGUE_NAME)

    def test_league_name_full_not_in_set(self):
        response: dict = self.client.execute(
            data.LIST_OF_PLAYERS_QUERY__NOT_IN_SET_LEAGUE_NAME,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.LIST_OF_PLAYERS_RESPONSE__NOT_IN_SET_LEAGUE_NAME)

    def test_country_of_origin_name_full_text_search(self):
        response: dict = self.client.execute(
            data.FULL_LIST_OF_PLAYERS_QUERY__COUNTRY_FULL_TEXT_SEARCH_FILTER,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.FULL_LIST_OF_PLAYERS_RESPONSE__COUNTRY_FULL_TEXT_SEARCH_FILTER)

    def test_country_of_origin_name_in_set(self):
        response: dict = self.client.execute(
            data.FULL_LIST_OF_PLAYERS_QUERY__COUNTRY_IN_SET_FILTER,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.FULL_LIST_OF_PLAYERS_RESPONSE__COUNTRY_IN_SET_FILTER)

    def test_country_of_origin_name_not_in_set(self):
        response: dict = self.client.execute(
            data.FULL_LIST_OF_PLAYERS_QUERY__COUNTRY_NOT_IN_SET_FILTER,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.FULL_LIST_OF_PLAYERS_RESPONSE__COUNTRY_NOT_IN_SET_FILTER)


class Test__QueryForPlayerList__UnsortedUnfiltered(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_query_for_full_list_of_players(self):
        response: dict = self.client.execute(
            data.FULL_LIST_OF_PLAYERS_QUERY__UNFILTERED,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.FULL_LIST_OF_PLAYERS_RESPONSE__UNFILTERED)

    def test_query_for_list_of_players_for_match(self):
        response: dict = self.client.execute(
            data.LIST_OF_PLAYERS_FROM_MATCH_QUERY__NO_FILTER,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.LIST_OF_PLAYERS_FROM_MATCH_RESPONSE__NO_FILTER)

    def test_query_for_list_of_players_for_team(self):
        response: dict = self.client.execute(
            data.LIST_OF_PLAYERS_FROM_TEAM_QUERY__NO_FILTER,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.LIST_OF_PLAYERS_FROM_TEAM_RESPONSE__NO_FILTER)

    def test_query_for_list_of_players_for_team_and_match(self):
        response: dict = self.client.execute(
            data.LIST_OF_PLAYERS_FROM_TEAM_QUERY_AND_MATCH__NO_FILTER,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.LIST_OF_PLAYERS_FROM_TEAM_AND_MATCH_RESPONSE__NO_FILTER)

    def test_query_for_list_of_players_from_limited_date_range(self):
        response: dict = self.client.execute(
            data.LIST_OF_PLAYERS_QUERY__LIMITED_DATE_RANGE,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.LIST_OF_PLAYERS_RESPONSE__LIMITED_DATE_RANGE)


class Test__QueryForPlayerData(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_query_for_player_own_data(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__OWN_DATA,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.PLAYER_QUERY_RESPONSE__OWN_DATA)

    def test_query_for_player_admin_actions(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__ADMIN_ACTIONS,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.PLAYER_QUERY_RESPONSE__ADMIN_ACTIONS)

    def test_query_for_player_country(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__COUNTRY_OF_ORIGIN_DATA,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.PLAYER_QUERY_RESPONSE__COUNTRY_OF_ORIGIN_DATA)


class Test__QueryForPlayerMetrics__Sum(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_sum_from_single_match(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__SUM_FOR_SUCCESSFUL_PASS_IN_MATCH,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.PLAYER_QUERY_RESPONSE__SUM_FOR_SUCCESSFUL_PASS_IN_MATCH)

class Test__QueryForPlayerMetrics__Average(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_average_from_team_matches(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__AVERAGE_FOR_SUCCESSFUL_PASS_IN_TEAM_MATCHES,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(
            response,
            data.PLAYER_QUERY_RESPONSE__AVERAGE_FOR_SUCCESSFUL_PASS_IN_TEAM_MATCHES
        )

class Test__QueryForPlayerMetrics__OddsFor(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_odds_for_from_all_matches(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__ODDS_FOR_SUCCESSFUL_PASS_IN_ALL_MATCHES,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(
            response,
            data.PLAYER_QUERY_RESPONSE__ODDS_FOR_SUCCESSFUL_PASS_IN_ALL_MATCHES
        )

class Test__QueryForPlayerMetrics__OddsForMoreThan(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_odds_for_more_than_from_all_matches(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__ODDS_FOR_MORE_THAN_SUCCESSFUL_PASS_IN_ALL_MATCHES,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(
            response,
            data.PLAYER_QUERY_RESPONSE__ODDS_FOR_MORE_THAN_SUCCESSFUL_PASS_IN_ALL_MATCHES
        )

class Test__QueryForPlayerMetrics__MinutesUntil(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_minutes_until_from_single_match(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__MINUTES_UNTIL_SUCCESSFUL_PASS_IN_MATCH,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(
            response,
            data.PLAYER_QUERY_RESPONSE__MINUTES_UNTIL_SUCCESSFUL_PASS_IN_MATCH
        )

class Test__QueryForPlayerMetrics__OddsInTimeRange(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_odds_in_time_range_from_team_matches(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__ODDS_IN_TIME_RANGE_SUCCESSFUL_PASS_IN_TEAM_MATCHES,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(
            response,
            data.PLAYER_QUERY_RESPONSE__ODDS_IN_TIME_RANGE_SUCCESSFUL_PASS_IN_TEAM_MATCHES
        )

class Test__QueryForPlayerMetricHistory(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_sum_metric_history(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__METRIC_HISTORY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(
            response,
            data.PLAYER_QUERY_RESPONSE__METRIC_HISTORY
        )