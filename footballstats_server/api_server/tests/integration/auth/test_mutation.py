from datetime import datetime

from freezegun import freeze_time
from django.contrib.auth.models import User
from django.test import TestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema
from api_server.auth._registration_tokens import RegistrationTokenStorage
from api_server.auth.mutation import _is_username_claimed

from api_server.tests import testconf as global_testconf
from api_server.tests.__data__.auth import mutation as global_data
from api_server.tests.integration.__data__.auth import mutation as data


class Test__is_username_claimed(TestCase):
    fixtures = ["initial_data"]

    def test_can_tell_if_username_is_claimed(self):
        is_claimed: bool = _is_username_claimed("owner")
        self.assertTrue(is_claimed)

    def test_can_tell_if_username_is_not_claimed(self):
        is_claimed: bool = _is_username_claimed("not-claimed-username")
        self.assertFalse(is_claimed)



@freeze_time("2025-01-01")
class Test__RegisterUser__RegistrationTokenStorage__User(TestCase):
    fixtures = ["initial_data"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema)
        RegistrationTokenStorage().add_token("92f3dcfc-6457-4248-8a29-18b164a2a29a")

    def test_can_register_new_admin_for_valid_credentials(self):
        response: dict = self.client.execute(
            global_data.REGISTER_USER_REQUEST_WITH_VALID_CREDENTIALS,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        actual_users: tuple[dict] = tuple(User.objects.all().values('username'))
        
        self.assertEqual(response, global_data.REGISTER_USER_RESPONSE_WITH_VALID_CREDENTIALS)
        self.assertEqual(actual_users, data.USERS_AFTER_REGISTERING_NEW_USER)
        self.assertEqual(RegistrationTokenStorage().tokens, [])

    def test_cant_register_new_admin_for_invalid_credentials(self):
        response: dict = self.client.execute(
            global_data.REGISTER_USER_REQUEST_INVALID_TOKEN_NOT_UNIQ_USERNAME,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        actual_users: tuple[dict] = tuple(User.objects.all().values('username'))

        self.assertEqual(response, global_data.REGISTER_USER_INVALID_TOKEN_NOT_UNIQ_USERNAME)
        self.assertEqual(actual_users, data.USERS_BEFORE_REGISTERING_NEW_USER)
        self.assertEqual(
            RegistrationTokenStorage().tokens, 
            [("92f3dcfc-6457-4248-8a29-18b164a2a29a", datetime(2025, 1, 4))]
        )

    def test_cant_register_new_admin_for_invalid_login_but_valid_token(self):
        response: dict = self.client.execute(
            global_data.REGISTER_USER_REQUEST_BLANK_USERNAME,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        actual_users: tuple[dict] = tuple(User.objects.all().values('username'))

        self.assertEqual(response, global_data.REGISTER_USER_RESPONSE_BLANK_USERNAME)
        self.assertEqual(actual_users, data.USERS_BEFORE_REGISTERING_NEW_USER)
        self.assertEqual(
            RegistrationTokenStorage().tokens, 
            [("92f3dcfc-6457-4248-8a29-18b164a2a29a", datetime(2025, 1, 4))]
        )