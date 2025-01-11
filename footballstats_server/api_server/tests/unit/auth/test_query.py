from unittest.mock import patch, MagicMock
from datetime import datetime

from django.test import SimpleTestCase
from freezegun import freeze_time
from graphene.test import Client as GraphQlClient

from api_server.auth.query import _RegistrationTokenStorage
from api_server.views import schema
from api_server.tests.__data__.auth import query as data
from api_server.tests import testconf as global_testconf


class Test__AuthQuery__generate_registration_token(SimpleTestCase):
    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema)

    @patch("api_server.auth.query._RegistrationTokenStorage.add_token", return_value=True)
    @patch("api_server.auth.query.uuid.uuid4", return_value="92f3dcfc-6457-4248-8a29-18b164a2a29a")
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


@freeze_time("2025-01-04 12:00:00")
class Test__RegistryTokenStorage__delete_expired_tokens(SimpleTestCase):
    def setUp(self):
        self.token_storage: _RegistrationTokenStorage = _RegistrationTokenStorage()
        self.token_storage.tokens.clear()

    def test_when_one_token_before_expiration_date_and_one_token_after_then_remove_this_after_expiration_date(self):
        self.token_storage.tokens.append(("not_expired_token", datetime(2025, 1, 6)))
        self.token_storage.tokens.append(("expired_token", datetime(2025, 1, 3)))

        self.token_storage.delete_expired_tokens()

        self.assertEqual([("not_expired_token", datetime(2025, 1, 6))], self.token_storage.tokens)

    def test_when_one_token_before_expiration_date_and_one_token_after_then_return_1(self):
        self.token_storage.tokens.append(("not_expired_token", datetime(2025, 1, 6)))
        self.token_storage.tokens.append(("expired_token", datetime(2025, 1, 3)))

        number_of_expired_tokens: int = self.token_storage.delete_expired_tokens()

        self.assertEqual(number_of_expired_tokens, 1)


@freeze_time("2025-01-01 12:00:00")
class Test__RegistryTokenStorage__add_token(SimpleTestCase):
    def setUp(self):
        self.token_storage: _RegistrationTokenStorage = _RegistrationTokenStorage()
        self.token_storage.tokens.clear()

    def test_when_storage_is_empty_then_add_token_with_its_expiration_date(self):
        token: str = "token"
        expected_expiration_date: datetime = datetime(2025, 1, 4, 12, 0, 0)
        
        self.token_storage.add_token(token)
        
        self.assertEqual([(token, expected_expiration_date)], self.token_storage.tokens)

    def test_when_storage_is_empty_then_return_True(self):
        token: str = "token"
        
        uniq: bool = self.token_storage.add_token(token)
        
        self.assertTrue(uniq)

    def test_when_storage_is_not_empty_and_new_uniq_token_added_then_add_token_with_its_expiration_date(self):
        self.token_storage.add_token("token_1")
        expected_expiration_date: datetime = datetime(2025, 1, 4, 12, 0, 0)
        token: str = "token_2"

        self.token_storage.add_token(token)
        
        self.assertIn((token, expected_expiration_date), self.token_storage.tokens)

    def test_when_storage_is_not_empty_and_new_uniq_token_added_then_return_True(self):
        self.token_storage.add_token("token_1")
        token: str = "token_2"

        uniq: bool = self.token_storage.add_token(token)
        
        self.assertTrue(uniq)

    def test_when_storage_is_not_empty_and_the_same_token_added_then_not_add_token_with_its_expiration_date(self):
        self.token_storage.add_token("token_1")
        token: str = "token_1"

        self.token_storage.add_token(token)
        
        self.assertEqual(
            [("token_1", datetime(2025, 1, 4, 12, 0, 0))], 
            self.token_storage.tokens
        )

    def test_when_storage_is_not_empty_and_the_same_token_added_then_return_False(self):
        self.token_storage.add_token("token_1")
        token: str = "token_1"

        uniq: bool = self.token_storage.add_token(token)
        
        self.assertFalse(uniq)