from unittest.mock import patch, MagicMock

from django.test import SimpleTestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema
from api_server.tests import testconf as global_testconf
from api_server.tests.__data__.auth import mutation as global_data


@patch("api_server.auth.mutation.RegistrationTokenStorage.use_token", return_value=(False, True))
@patch("api_server.auth.mutation._is_username_claimed", return_value=True)
@patch("api_server.auth.mutation.User")
class Test__RegisterUser(SimpleTestCase):
    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema)

    def test_when_client_sends_valid_credentials_then_return_success_response(
        self, 
        mock_User: MagicMock,
        mock_is_username_claimed: MagicMock,
        mock_use_token: MagicMock,
    ):
        mock_is_username_claimed.return_value = False
        mock_use_token.return_value=(True, True)

        response: dict = self.client.execute(
            global_data.REGISTER_USER_REQUEST_WITH_VALID_CREDENTIALS, 
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, global_data.REGISTER_USER_RESPONSE_WITH_VALID_CREDENTIALS)

    def test_when_client_sends_not_uniq_username_then_return_error_response(
        self,
        mock_User: MagicMock,
        mock_is_username_claimed: MagicMock,
        mock_use_token: MagicMock,
    ):
        mock_is_username_claimed.return_value = True
        mock_use_token.return_value=(True, True)

        response: dict = self.client.execute(
            global_data.REGISTER_USER_REQUEST_NOT_UNIQ_USERNAME, 
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        self.assertEqual(response, global_data.REGISTER_USER_RESPONSE_NOT_UNIQ_USERNAME)

    def test_when_client_sends_not_blank_username_then_return_error_response(
        self,
        mock_User: MagicMock,
        mock_is_username_claimed: MagicMock,
        mock_use_token: MagicMock,
    ):
        mock_is_username_claimed.return_value = False
        mock_use_token.return_value=(True, True)

        response: dict = self.client.execute(
            global_data.REGISTER_USER_REQUEST_BLANK_USERNAME, 
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        self.assertEqual(response, global_data.REGISTER_USER_RESPONSE_BLANK_USERNAME)

    def test_when_client_sends_invalid_token_then_return_error_response(
        self,
        mock_User: MagicMock,
        mock_is_username_claimed: MagicMock,
        mock_use_token: MagicMock,
    ):
        mock_is_username_claimed.return_value = False
        mock_use_token.return_value=(False, True)

        response: dict = self.client.execute(
            global_data.REGISTER_USER_REQUEST_INVALID_TOKEN, 
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        self.assertEqual(response, global_data.REGISTER_USER_RESPONSE_INVALID_TOKEN)

    def test_when_client_sends_valid_but_expired_token_then_return_error_response(
        self,
        mock_User: MagicMock,
        mock_is_username_claimed: MagicMock,
        mock_use_token: MagicMock,
    ):
        mock_is_username_claimed.return_value = False
        mock_use_token.return_value=(True, False)

        response: dict = self.client.execute(
            global_data.REGISTER_USER_REQUEST_EXPIRED_TOKEN, 
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        self.assertEqual(response, global_data.REGISTER_USER_RESPONSE_EXPIRED_TOKEN)

    def test_when_client_sends_invalid_token_but_not_uniq_username_then_return_error_response(
        self,
        mock_User: MagicMock,
        mock_is_username_claimed: MagicMock,
        mock_use_token: MagicMock,
    ):
        mock_is_username_claimed.return_value = True
        mock_use_token.return_value=(False, True)

        response: dict = self.client.execute(
            global_data.REGISTER_USER_REQUEST_INVALID_TOKEN_NOT_UNIQ_USERNAME, 
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        self.assertEqual(response, global_data.REGISTER_USER_INVALID_TOKEN_NOT_UNIQ_USERNAME)