from django.test import TestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema

from api_server.tests.integration.__data__.graphql.queries import PlayerQuery as data
from api_server.tests import testconf as global_testconf


class Test__PlayerQuery__PlayerType__CountryType__Country(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_when_client_queries_for_player_country_then_return_it(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__COUNTRY_OF_ORIGIN_DATA,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.PLAYER_QUERY_RESPONSE__COUNTRY_OF_ORIGIN_DATA)


class Tests__PlayerQuery__PlayerType__AdminAction(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_when_client_queries_for_player_admin_actions_then_return_them(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__ADMIN_ACTIONS,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.PLAYER_QUERY_RESPONSE__ADMIN_ACTIONS)


class Test__PlayerQuery__PlayerType__Player(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_query_for_player_own_data(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__OWN_DATA,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.PLAYER_QUERY_RESPONSE__OWN_DATA)

    def test_when_client_queries_for_player_sum_from_match_then_return_metric_value(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__SUM_FOR_SUCCESSFUL_PASS_IN_MATCH,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.PLAYER_QUERY_RESPONSE__SUM_FOR_SUCCESSFUL_PASS_IN_MATCH)

    def test_when_client_queries_for_player_average_from_team_matches_then_return_metric_value(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__AVERAGE_FOR_SUCCESSFUL_PASS_IN_TEAM_MATCHES,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(
            response,
            data.PLAYER_QUERY_RESPONSE__AVERAGE_FOR_SUCCESSFUL_PASS_IN_TEAM_MATCHES
        )

    def test_when_client_queries_for_player_odds_for_from_all_matches_then_return_metric_value(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__ODDS_FOR_SUCCESSFUL_PASS_IN_ALL_MATCHES,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(
            response,
            data.PLAYER_QUERY_RESPONSE__ODDS_FOR_SUCCESSFUL_PASS_IN_ALL_MATCHES
        )

    def test_when_client_queries_for_player_odds_for_more_than_from_all_matches_then_return_metric_value(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__ODDS_FOR_MORE_THAN_SUCCESSFUL_PASS_IN_ALL_MATCHES,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(
            response,
            data.PLAYER_QUERY_RESPONSE__ODDS_FOR_MORE_THAN_SUCCESSFUL_PASS_IN_ALL_MATCHES
        )

    def test_when_client_queries_for_player_minutes_until_from_match_then_return_metric_value(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__MINUTES_UNTIL_SUCCESSFUL_PASS_IN_MATCH,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(
            response,
            data.PLAYER_QUERY_RESPONSE__MINUTES_UNTIL_SUCCESSFUL_PASS_IN_MATCH
        )

    def test_when_client_queries_for_player_odds_in_time_range_from_team_matches_then_return_metric_value(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__ODDS_IN_TIME_RANGE_SUCCESSFUL_PASS_IN_TEAM_MATCHES,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(
            response,
            data.PLAYER_QUERY_RESPONSE__ODDS_IN_TIME_RANGE_SUCCESSFUL_PASS_IN_TEAM_MATCHES
        )

    def test_when_client_queries_for_player_sum_metric_history_then_return_metric_history(self):
        response: dict = self.client.execute(
            data.PLAYER_QUERY__METRIC_HISTORY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(
            response,
            data.PLAYER_QUERY_RESPONSE__METRIC_HISTORY
        )