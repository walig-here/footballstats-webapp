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


class Test__GrantPermission__User(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema)

    def test_can_grant_permission_to_user_when_owner_request_is_valid(self):
        response: dict = self.client.execute(
            global_data.GRANT_PERMISSION_REQUEST__VALID_INPUTS,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        target_user = User.objects.get(username="Jerzy")
        user_permissions: list[str] = list(target_user.get_group_permissions())
        user_permissions.sort()

        self.assertEqual(response, global_data.GRANT_PERMISSION_RESPONSE__VALID_INPUTS)
        self.assertEqual(
            [group.name for group in target_user.groups.all().order_by('name')],
            ["Creators", "Modifiers", "Removers"]
        )
        self.assertEqual(
            user_permissions,
            global_data.ALL_POSSIBLE_ADMIN_ACTION_TYPES
        )

    def test_can_grant_already_given_permission_to_user_when_owner_request_is_valid(self):
        response: dict = self.client.execute(
            global_data.GRANT_PERMISSION_REQUEST__ALREADY_GIVEN_PERMISSION,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        target_user = User.objects.get(username="Jerzy")
        user_permissions: list[str] = list(target_user.get_group_permissions())
        user_permissions.sort()

        self.assertEqual(response, global_data.GRANT_PERMISSION_RESPONSE__ALREADY_GIVEN_PERMISSION)
        self.assertEqual(
            [group.name for group in target_user.groups.all().order_by('name')],
            ["Creators", "Modifiers"]
        )
        self.assertEqual(
            user_permissions,
            global_data.CREATORS_AND_MODIFIERS_ADMIN_ACTION_TYPES
        )


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
        self.assertEqual(
            [group.name for group in User.objects.get(username="NewUser").groups.all().order_by('name')],
            []
        )
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