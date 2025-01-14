from django.test import TestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema

from api_server.tests.integration.__data__.graphql.queries import MatchQuery as data
from api_server.tests import testconf as global_testconf


class Test__QueryMatchList__UnfilteredUnsorted(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_get_all_matches(self):
        response: dict = self.client.execute(
            data.ALL_MATCHES_LIST_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.ALL_MATCHES_LIST_RESPONSE)

    def test_can_get_player_matches(self):
        response: dict = self.client.execute(
            data.PLAYER_MATCHES_LIST_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.PLAYER_MATCHES_LIST_RESPONSE)

    def test_can_get_team_matches(self):
        response: dict = self.client.execute(
            data.TEAM_MATCHES_LIST_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.TEAM_MATCHES_LIST_RESPONSE)


class Test__QueryAttributes(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_get_match_filtering_attributes(self):
        response: dict = self.client.execute(
            data.MATCH_FILTERING_ATTRIBUTES_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.MATCH_FILTERING_ATTRIBUTES_RESPONSE)

    def test_can_get_match_sorting_attributes(self):
        response: dict = self.client.execute(
            data.MATCH_SORTING_ATTRIBUTES_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.MATCH_SORTING_ATTRIBUTES_RESPONSE)


class Test__QueryData(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_get_match_own_data(self):
        response: dict = self.client.execute(
            data.MATCH_OWN_DATA_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.MATCH_OWN_DATA_RESPONSE)

    def test_can_get_events(self):
        response: dict = self.client.execute(
            data.MATCH_EVENTS_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(len(response["data"]["match"]["events"]), 924)

    def test_can_get_league_and_season(self):
        response: dict = self.client.execute(
            data.MATCH_LEAGUE_SEASON_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.MATCH_LEAGUE_SEASON_RESPONSE)

    def test_can_get_team_scores(self):
        response: dict = self.client.execute(
            data.MATCH_TEAM_SCORES_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.MATCH_TEAM_SCORES_RESPONSE)


class Test__QueryMatchMetric(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_calculate_sum_for_shot_not_on_target(self):
        response: dict = self.client.execute(
            data.MATCH_SUM_SHOT_NOT_ON_TARGET_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.MATCH_SUM_SHOT_NOT_ON_TARGET_RESPONSE)

    def test_calculate_average_for_shot_not_on_target(self):
        response: dict = self.client.execute(
            data.MATCH_AVERAGE_SHOT_NOT_ON_TARGET_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.MATCH_AVERAGE_SHOT_NOT_ON_TARGET_RESPONSE)

    def test_calculate_odds_for_for_shot_not_on_target(self):
        response: dict = self.client.execute(
            data.MATCH_ODDS_FOR_SHOT_NOT_ON_TARGET_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.MATCH_ODDS_FOR_SHOT_NOT_ON_TARGET_RESPONSE)

    def test_calculate_odds_for_more_than_for_shot_not_on_target(self):
        response: dict = self.client.execute(
            data.MATCH_ODDS_FOR_MORE_THAN_SHOT_NOT_ON_TARGET_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.MATCH_ODDS_FOR_MORE_THAN_SHOT_NOT_ON_TARGET_RESPONSE)

    def test_calculate_minutes_until_for_shot_not_on_target(self):
        response: dict = self.client.execute(
            data.MATCH_MINUTES_UNTIL_SHOT_NOT_ON_TARGET_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.MATCH_MINUTES_UNTIL_SHOT_NOT_ON_TARGET_RESPONSE)

    def test_calculate_odds_in_time_range_for_shot_not_on_target(self):
        response: dict = self.client.execute(
            data.MATCH_ODDS_IN_TIME_RANGE_SHOT_NOT_ON_TARGET_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.MATCH_ODDS_IN_TIME_RANGE_SHOT_NOT_ON_TARGET_RESPONSE)