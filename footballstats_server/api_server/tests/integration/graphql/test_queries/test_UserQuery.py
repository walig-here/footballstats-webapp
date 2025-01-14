from django.test import TestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema

from api_server.tests.integration.__data__.graphql.queries import UserQuery as data
from api_server.tests import testconf as global_testconf


class Test__QueryAttributes(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_get_user_filtering_attributes(self):
        response: dict = self.client.execute(
            data.USER_FILTERING_ATTRIBUTES_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.USER_FILTERING_ATTRIBUTES_RESPONSE)

    def test_can_get_user_sorting_attributes(self):
        response: dict = self.client.execute(
            data.USER_SORTING_ATTRIBUTES_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.USER_SORTING_ATTRIBUTES_RESPONSE)


class Test__QueryUserList(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_owner_get_user_list(self):
        response: dict = self.client.execute(
            data.USERS_LIST_QUERY,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        self.assertEqual(response, data.USERS_LIST_RESPONSE_FOR_OWNER)

    def test_cant_admin_get_user_list(self):
        response: dict = self.client.execute(
            data.USERS_LIST_QUERY,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        self.assertEqual(response, data.USERS_LIST_RESPONSE_FOR_NOT_OWNER)

    def test_cant_viewer_get_user_list(self):
        response: dict = self.client.execute(
            data.USERS_LIST_QUERY,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, data.USERS_LIST_RESPONSE_FOR_NOT_OWNER)

    def test_owner_can_get_user_permissions(self):
        response: dict = self.client.execute(
            data.USER_PERMISSIONS_QUERY,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        self.assertEqual(response, data.USER_PERMISSIONS_RESPONSE)