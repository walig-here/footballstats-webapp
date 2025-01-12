from django.test import SimpleTestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema

from api_server.tests.__data__.graphql.queries import PlayerQuery as global_data
from api_server.tests import testconf as global_testconf


class Test__PlayerQuery__player_sorting_attributes(SimpleTestCase):
    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_when_client_queries_then_return_sorting_attributes(self):
        response: dict = self.client.execute(
            global_data.PLAYER_SORTING_ATTRIBUTES_REQUEST,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, global_data.PLAYER_SORTING_ATTRIBUTES_RESPONSE)


class Test__PlayerQuery__player_filtering_attributes(SimpleTestCase):
    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_when_client_queries_then_return_filtering_attributes(self):
        response: dict = self.client.execute(
            global_data.PLAYER_FILTERING_ATTRIBUTES_REQUEST,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, global_data.PLAYER_FILTERING_ATTRIBUTES_RESPONSE)


class Test__PlayerQuery__player(SimpleTestCase):
    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_when_client_provided_id_of_not_existing_player_then_return_error(self):
        ...