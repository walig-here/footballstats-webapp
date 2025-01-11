from unittest.mock import patch, MagicMock
from uuid import UUID

from django.test import SimpleTestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema
from api_server.tests.__data__.auth import query as data
from api_server.tests import testconf as global_testconf


class Test__AuthQuery__generate_registration_token(SimpleTestCase):
    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema)

    @patch("api_server.auth.query.RegistrationTokenStorage.add_token", return_value=True)
    @patch("api_server.auth.query.uuid.uuid4", return_value=UUID("92f3dcfc-6457-4248-8a29-18b164a2a29a"))
    def test_when_owner_queries_for_token_then_return_them_token(self, mock_uuid4: MagicMock, mock_add_token: MagicMock):
        response: dict = self.client.execute(
            data.GENERATE_REGISTRATION_TOKEN_REQUEST, 
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        self.assertEqual(response, data.GENERATE_REGISTRATION_TOKEN_OWNER_RESPONSE)

    def test_when_admin_queries_for_token_then_return_error_about_unsufficient_permissions(self):
        response: dict = self.client.execute(
            data.GENERATE_REGISTRATION_TOKEN_REQUEST, 
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        self.assertEqual(response, data.GENERATE_REGISTRATION_NOT_OWNER_RESPONSE)

    def test_when_viewer_queries_for_token_then_return_error_about_unsufficient_permissions(self):
        response: dict = self.client.execute(
            data.GENERATE_REGISTRATION_TOKEN_REQUEST, 
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        self.assertEqual(response, data.GENERATE_REGISTRATION_NOT_OWNER_RESPONSE)


