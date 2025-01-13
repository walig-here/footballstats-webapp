from freezegun import freeze_time
from django.test import TestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema

from api_server.tests.integration.__data__.graphql.queries import MiscellaneousQuery as data
from api_server.tests import testconf as global_testconf


class Test__NotEmptyDatabase(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_get_range(self):
        response: dict = self.client.execute(
            data.DATA_DATE_RANGE_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.DATA_DATE_RANGE_RESPONSE__NOT_EMPTY_DATA_BASE)

    def test_can_get_list_of_countries(self):
        response: dict = self.client.execute(
            data.COUNTRY_LIST_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.COUNTRY_LIST_RESPONSE__NOT_EMPTY_DATA_BASE)

    def test_can_get_list_of_event_types(self):
        response: dict = self.client.execute(
            data.EVENT_TYPES_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.EVENT_TYPES_RESPONSE)


@freeze_time("2025-01-01")
class Test__EmptyDatabase(TestCase):
    fixtures = ["initial_data"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_get_range(self):
        response: dict = self.client.execute(
            data.DATA_DATE_RANGE_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.DATA_DATE_RANGE_RESPONSE__EMPTY_DATA_BASE)

    def test_can_get_list_of_countries(self):
        response: dict = self.client.execute(
            data.COUNTRY_LIST_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.COUNTRY_LIST_RESPONSE__EMPTY_DATA_BASE)

    def test_can_get_list_of_event_types(self):
        response: dict = self.client.execute(
            data.EVENT_TYPES_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.EVENT_TYPES_RESPONSE)
