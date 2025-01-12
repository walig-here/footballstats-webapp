from unittest.mock import patch, MagicMock

from django.test import SimpleTestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema
from api_server.tests import testconf as global_testconf
from api_server.tests.__data__.auth import mutation as global_data


@patch("api_server.auth.mutation.User.objects.get")
@patch("api_server.auth.mutation.Group.objects.filter")
@patch("api_server.auth.mutation._is_username_claimed")
class Test__GrantPermission(SimpleTestCase):
    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema)

    def test_when_owner_provides_valid_username_and_permission_then_return_success_response(
        self,
        mock_is_username_claimed: MagicMock,
        mock_user_get: MagicMock,
        mock_group_filter: MagicMock
    ):
        mock_is_username_claimed.return_value = True
        response: dict = self.client.execute(
            global_data.GRANT_PERMISSION_REQUEST__VALID_INPUTS,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        self.assertEqual(response, global_data.GRANT_PERMISSION_RESPONSE__VALID_INPUTS)

    def test_when_admin_provides_valid_username_and_permission_then_return_error_response(
        self,
        mock_is_username_claimed: MagicMock,
        mock_user_get: MagicMock,
        mock_group_filter: MagicMock
    ):
        mock_is_username_claimed.return_value = True
        response: dict = self.client.execute(
            global_data.GRANT_PERMISSION_REQUEST__VALID_INPUTS,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        self.assertEqual(response, global_data.GRANT_PERMISSION_RESPONSE__NOT_OWNER)

    def test_when_viewer_provides_valid_username_and_permission_then_return_error_response(
        self,
        mock_is_username_claimed: MagicMock,
        mock_user_get: MagicMock,
        mock_group_filter: MagicMock
    ):
        mock_is_username_claimed.return_value = True
        response: dict = self.client.execute(
            global_data.GRANT_PERMISSION_REQUEST__VALID_INPUTS,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, global_data.GRANT_PERMISSION_RESPONSE__NOT_OWNER)

    def test_when_owner_provided_permission_that_user_already_has_then_return_success_response(
        self,
        mock_is_username_claimed: MagicMock,
        mock_user_get: MagicMock,
        mock_group_filter: MagicMock
    ):
        mock_is_username_claimed.return_value = True
        response: dict = self.client.execute(
            global_data.GRANT_PERMISSION_REQUEST__ALREADY_GIVEN_PERMISSION,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        self.assertEqual(response, global_data.GRANT_PERMISSION_RESPONSE__ALREADY_GIVEN_PERMISSION)

    def test_when_owner_provided_permission_that_doesnt_exist_then_return_error_response(
        self,
        mock_is_username_claimed: MagicMock,
        mock_user_get: MagicMock,
        mock_group_filter: MagicMock
    ):
        mock_is_username_claimed.return_value = True
        response: dict = self.client.execute(
            global_data.GRANT_PERMISSION_REQUEST__NOT_EXISTING_PERMISSION,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        self.assertEqual(response, global_data.GRANT_PERMISSION_RESPONSE__NOT_EXISTING_PERMISSION)

    def test_when_owner_provided_permission_to_not_existing_user_then_return_error_response(
        self,
        mock_is_username_claimed: MagicMock,
        mock_user_get: MagicMock,
        mock_group_filter: MagicMock
    ):
        mock_is_username_claimed.return_value = False
        response: dict = self.client.execute(
            global_data.GRANT_PERMISSION_REQUEST__NOT_EXISTING_USER,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        self.assertEqual(response, global_data.GRANT_PERMISSION_RESPONSE__NOT_EXISTING_USER)

    def test_when_owner_provided_permission_to_owner_then_return_error_response(
        self,
        mock_is_username_claimed: MagicMock,
        mock_user_get: MagicMock,
        mock_group_filter: MagicMock
    ):
        mock_is_username_claimed.return_value = True
        response: dict = self.client.execute(
            global_data.GRANT_PERMISSION_REQUEST__TARGETS_OWNER,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        self.assertEqual(response, global_data.GRANT_PERMISSION_RESPONSE__TARGETS_OWNER)


@patch("api_server.auth.mutation.RegistrationTokenStorage.use_token")
@patch("api_server.auth.mutation._is_username_claimed")
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