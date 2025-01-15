from datetime import date
from decimal import Decimal
from unittest.mock import patch, MagicMock

from django.test import TestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema
from api_server.models import MatchEvent, PlayerInMatch, Player, Team, Match

from api_server.tests.integration.__data__.graphql.mutation import remove as data
from api_server.tests import testconf as global_testconf


@patch("api_server.graphql.mutations.remove.user_has_permission", return_value = True)
class Test__RemoveEvent(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_delete_permission_delete_event(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.REMOVE_EVENT_QUERY,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.REMOVE_EVENT_RESPONSE)
        with self.assertRaises(MatchEvent.DoesNotExist):
            MatchEvent.objects.get(pk=925)


@patch("api_server.graphql.mutations.remove.user_has_permission", return_value = True)
class Test__RemovePlayerFromTeam(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_delete_permission_delete_player_from_team(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.REMOVE_PLAYER_FROM_TEAM_QUERY,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.REMOVE_PLAYER_FROM_TEAM_RESPONSE)
        self.assertEqual(PlayerInMatch.objects.filter(player=55, team=4).count(), 0)
        self.assertEqual(Match.objects.all().count(), 5)
        Player.objects.get(pk=55)
        Team.objects.get(pk=4)


@patch("api_server.graphql.mutations.remove.user_has_permission", return_value = True)
class Test__RemoveTeam(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_delete_permission_delete_team(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.REMOVE_TEAM_QUERY,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.REMOVE_TEAM_RESPONSE)
        with self.assertRaises(Team.DoesNotExist):
            Team.objects.get(pk=3)


@patch("api_server.graphql.mutations.remove.user_has_permission", return_value = True)
class Test__RemoveMatch(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_delete_permission_delete_match(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.REMOVE_MATCH_QUERY,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.REMOVE_MATCH_RESPONSE)
        with self.assertRaises(Match.DoesNotExist):
            Match.objects.get(pk=6)


@patch("api_server.graphql.mutations.remove.user_has_permission", return_value = True)
class Test__RemovePlayer(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_delete_permission_delete_player(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.REMOVE_PLAYER_QUERY,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.REMOVE_PLAYER_RESPONSE)
        with self.assertRaises(Match.DoesNotExist):
            Match.objects.get(pk=38)


@patch("api_server.graphql.mutations.remove.user_has_permission", return_value = True)
class Test__RemovePlayerFromMatch(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_delete_permission_delete_player_from_match(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.REMOVE_PLAYER_FROM_MATCH_QUERY,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.REMOVE_PLAYER_FROM_MATCH_RESPONSE)
        with self.assertRaises(PlayerInMatch.DoesNotExist):
            PlayerInMatch.objects.get(player=55, match=2)
        Player.objects.get(pk=55)
        Match.objects.get(pk=2)