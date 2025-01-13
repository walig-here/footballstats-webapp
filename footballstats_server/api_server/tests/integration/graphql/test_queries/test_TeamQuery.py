from django.test import TestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema

from api_server.tests.integration.__data__.graphql.queries import TeamQuery as data
from api_server.tests import testconf as global_testconf


class Test__QueryAttributes(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_get_team_sorting_attributes(self):
        response: dict = self.client.execute(
            data.TEAM_SORTING_ATTRIBUTES_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.TEAM_SORTING_ATTRIBUTES_RESPONSE)

    def test_can_get_team_filtering_attributes(self):
        response: dict = self.client.execute(
            data.TEAM_FILTERING_ATTRIBUTES_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.TEAM_FILTERING_ATTRIBUTES_RESPONSE)


class Test__QueryTeamData(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_get_team_own_data(self):
        response: dict = self.client.execute(
            data.TEAM_OWN_DATA_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.TEAM_OWN_DATA_RESPONSE)

    def test_can_get_team_country_of_origin(self):
        response: dict = self.client.execute(
            data.TEAM_COUNTRY_OF_ORIGIN_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.TEAM_COUNTRY_OF_ORIGIN_RESPONSE)


class Test__QueryTeam__TeamsList__UnsortedUnfiltered(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_get_all_teams(self):
        response: dict = self.client.execute(
            data.ALL_TEAMS_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.ALL_TEAMS_RESPONSE)

    def test_can_get_teams_playing_in_match(self):
        response: dict = self.client.execute(
            data.MATCH_TEAMS_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.MATCH_TEAMS_RESPONSE)

    def test_can_get_teams_represented_by_player(self):
        response: dict = self.client.execute(
            data.PLAYER_TEAMS_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.PLAYER_TEAMS_RESPONSE)


class Test__QueryTeam__calculateMetric(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_calculate_sum_successful_pass_single_match(self):
        response: dict = self.client.execute(
            data.TEAM_SUCCESSFUL_PASS_SUM_FOR_SINGLE_MARCH_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.TEAM_SUCCESSFUL_PASS_SUM_FOR_SINGLE_MARCH_RESPONSE)

    def test_can_calculate_average_successful_pass_all_matches(self):
        response: dict = self.client.execute(
            data.TEAM_SUCCESSFUL_PASS_AVERAGE_ALL_MATCHES_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.TEAM_SUCCESSFUL_PASS_AVERAGE_ALL_MATCHES_RESPONSE)

    def test_can_calculate_odds_for_successful_pass_all_matches(self):
        response: dict = self.client.execute(
            data.TEAM_SUCCESSFUL_PASS_ODDS_FOR_ALL_MATCHES_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.TEAM_SUCCESSFUL_PASS_ODDS_FOR_ALL_MATCHES_RESPONSE)

    def test_can_calculate_odds_for_more_than_successful_pass_single_match(self):
        response: dict = self.client.execute(
            data.TEAM_SUCCESSFUL_PASS_ODDS_FOR_MORE_THAN_SINGLE_MARCH_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.TEAM_SUCCESSFUL_PASS_ODDS_FOR_MORE_THAN_SINGLE_MARCH_RESPONSE)

    def test_can_calculate_minutes_until_than_successful_pass_all_matches(self):
        response: dict = self.client.execute(
            data.TEAM_SUCCESSFUL_PASS_MINUTES_UNTIL_ALL_MATCHES_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.TEAM_SUCCESSFUL_PASS_MINUTES_UNTIL_ALL_MATCHES_RESPONSE)

    def test_can_calculate_odds_in_time_range_than_successful_pass_single_match(self):
        response: dict = self.client.execute(
            data.TEAM_SUCCESSFUL_ODDS_INT_TIME_RANGE_SINGLE_MATCH_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.TEAM_SUCCESSFUL_ODDS_INT_TIME_RANGE_SINGLE_MATCH_RESPONSE)

    def test_can_calculate_history_for_SUM_for_successful_pass(self):
        response: dict = self.client.execute(
            data.TEAM_METRIC_HISTORY_SUM_SUCCESSFUL_PASS_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.TEAM_METRIC_HISTORY_SUM_SUCCESSFUL_PASS_RESPONSE)