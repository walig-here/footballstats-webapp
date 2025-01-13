from django.test import TestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema

from api_server.tests.integration.__data__.graphql.queries import LeagueQuery as data
from api_server.tests import testconf as global_testconf


class Test__NotEmptyDataBase(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_get_leagues(self):
        response: dict = self.client.execute(
            data.LEAGUE_LIST_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.LEAGUE_LIST_RESPONSE)

    def test_can_get_leagues_seasons(self):
        response: dict = self.client.execute(
            data.LEAGUE_SEASON_LIST_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.LEAGUE_SEASON_LIST_RESPONSE)