from datetime import datetime
from freezegun import freeze_time
from unittest.mock import patch, MagicMock

from django.test import SimpleTestCase
from graphene.test import Client as GraphQlClient

from api_server.auth._registration_tokens import RegistrationTokenStorage
from api_server.views import schema
from api_server.tests.__data__.auth import query as global_data
from api_server.tests.integration.__data__.auth import query as data
from api_server.tests import testconf as global_testconf


@freeze_time("2025-01-04 12:00:00")
class Test__can_generate_registration_token(SimpleTestCase):
    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema)
        self.token_storage: RegistrationTokenStorage = RegistrationTokenStorage()
        self.token_storage.tokens.clear()
        self.token_storage.tokens.append(("not_expired_token", datetime(2025, 1, 6)))
        self.token_storage.tokens.append(("92f3dcfc-6457-4248-8a29-18b164a2a29", datetime(2025, 1, 1)))
        self.token_storage.tokens.append(("expired_token", datetime(2025, 1, 3)))

    @patch("api_server.auth.query.uuid.uuid4", side_effect=["not_expired_token", "92f3dcfc-6457-4248-8a29-18b164a2a29a"])
    def test_can_generate_new_registration_token_when_owner_queries_for_it(self, mock_uuid4: MagicMock):
        response: dict = self.client.execute(
            global_data.GENERATE_REGISTRATION_TOKEN_REQUEST, 
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        
        self.assertEqual(response, global_data.GENERATE_REGISTRATION_TOKEN_OWNER_RESPONSE)
        self.assertEqual(self.token_storage.tokens, data.EXPECTED_TOKEN_STORAGE_AFTER_OWNER_QUERY)

    @patch("api_server.auth.query.uuid.uuid4", side_effect=["not_expired_token", "92f3dcfc-6457-4248-8a29-18b164a2a29a"])
    def test_cant_generate_new_registration_token_when_admin_queries_for_it(self, mock_uuid4: MagicMock):
        response: dict = self.client.execute(
            global_data.GENERATE_REGISTRATION_TOKEN_REQUEST, 
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        
        self.assertEqual(response, global_data.GENERATE_REGISTRATION_NOT_OWNER_RESPONSE)
        self.assertEqual(self.token_storage.tokens, data.EXPECTED_TOKEN_STORAGE_AFTER_NOT_OWNER_QUERY)

    @patch("api_server.auth.query.uuid.uuid4", side_effect=["not_expired_token", "92f3dcfc-6457-4248-8a29-18b164a2a29a"])
    def test_cant_generate_new_registration_token_when_viewer_queries_for_it(self, mock_uuid4: MagicMock):
        response: dict = self.client.execute(
            global_data.GENERATE_REGISTRATION_TOKEN_REQUEST, 
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        
        self.assertEqual(response, global_data.GENERATE_REGISTRATION_NOT_OWNER_RESPONSE)
        self.assertEqual(self.token_storage.tokens, data.EXPECTED_TOKEN_STORAGE_AFTER_NOT_OWNER_QUERY)