from datetime import date
from decimal import Decimal
from unittest.mock import patch, MagicMock

from django.test import TestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema
from api_server.models import MatchEvent, LeagueSeason, League, Country, Team, Match, Player

from api_server.tests.integration.__data__.graphql.mutation import modify as data
from api_server.tests import testconf as global_testconf


@patch("api_server.graphql.mutations.modify.user_has_permission", return_value = True)
class Test__ModifyPlayerMatchContribution(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_modify_permission_modify_player_match_contribution(self, mock_has_permission: MagicMock):
        ...

    def test_cant_owner_modify_player_match_contribution_when_team_is_not_playing_in_match(self, mock_has_permission: MagicMock):
        ...

    def test_cant_owner_modify_player_match_contribution_when_player_is_team_last_player(self, mock_has_permission: MagicMock):
        ...


@patch("api_server.graphql.mutations.modify.user_has_permission", return_value = True)
class Test__ModifyPlayer(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_modify_permission_modify_player(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.MODIFY_PLAYER_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.MODIFY_PLAYER_RESPONSE)
        self.assertEqual(
            (
                Player.objects.get(pk=37).name, 
                Player.objects.get(pk=37).surname, 
                Player.objects.get(pk=37).nickname, 
                Player.objects.get(pk=37).profile_photo_url,
                Player.objects.get(pk=37).country_of_origin.pk
            ),
            (
                "Jan",
                "Kowalski",
                "Kowal",
                "https://placehold.co/600x400",
                9
            )
        )

    def test_cant_owner_modify_player_when_fullname_not_uniq(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_UNIQ_FULLNAME_MODIFY_PLAYER_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.NOT_UNIQ_FULLNAME_MODIFY_PLAYER_RESPONSE)
        self.assertEqual(
            (
                Player.objects.get(pk=37).name, 
                Player.objects.get(pk=37).surname, 
                Player.objects.get(pk=37).nickname, 
                Player.objects.get(pk=37).profile_photo_url,
                Player.objects.get(pk=37).country_of_origin.pk
            ),
            (
                "Viktor",
                "Chanov",
                None,
                None,
                11
            )
        )

    def test_cant_owner_modify_player_when_country_not_exists(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.COUNTRY_NOT_EXIST_MODIFY_PLAYER_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.COUNTRY_NOT_EXIST_MODIFY_PLAYER_RESPONSE)
        self.assertEqual(
            (
                Player.objects.get(pk=37).name, 
                Player.objects.get(pk=37).surname, 
                Player.objects.get(pk=37).nickname, 
                Player.objects.get(pk=37).profile_photo_url,
                Player.objects.get(pk=37).country_of_origin.pk
            ),
            (
                "Viktor",
                "Chanov",
                None,
                None,
                11
            )
        )


@patch("api_server.graphql.mutations.modify.user_has_permission", return_value = True)
class Test__ModifyMatch(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_modify_permission_modify_match(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.MODIFY_MATCH_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.MODIFY_MATCH_RESPONSE)
        self.assertEqual(
            (Match.objects.get(pk=2).game_date, Match.objects.get(pk=2).league_season.pk),
            (date(1800, 1, 1), 4)
        )

    def test_cant_owner_modify_match_when_season_not_exist(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_EXISTING_SEASON_MODIFY_MATCH_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.NOT_EXISTING_SEASON_MODIFY_MATCH_RESPONSE)
        self.assertEqual(
            (Match.objects.get(pk=2).game_date, Match.objects.get(pk=2).league_season.pk),
            (date(1979, 9, 7), 2)
        )


@patch("api_server.graphql.mutations.modify.user_has_permission", return_value = True)
class Test__ModifyTeam(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_modify_permission_modify_team(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.MODIFY_TEAM_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.MODIFY_TEAM_RESPONSE)
        self.assertEqual(
            (Team.objects.get(pk=3).name, Team.objects.get(pk=3).country_of_origin.pk, Team.objects.get(pk=3).logo_url),
            ("ZSRR", 10, "https://placehold.co/600x400")
        )

    def test_cant_owner_modify_team_with_not_uniq_name(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_UNIQ_NAME_MODIFY_TEAM_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.NOT_UNIQ_NAME_MODIFY_TEAM_RESPONSE)
        self.assertEqual(
            (Team.objects.get(pk=3).name, Team.objects.get(pk=3).country_of_origin.pk, Team.objects.get(pk=3).logo_url),
            ("Związek Radziecki U20", 9, None)
        )

    def test_cant_owner_modify_team_with_not_existing_country_of_origin(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_EXISTING_COUNTRY_MODIFY_TEAM_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.NOT_EXISTING_COUNTRY_MODIFY_TEAM_RESPONSE)
        self.assertEqual(
            (Team.objects.get(pk=3).name, Team.objects.get(pk=3).country_of_origin.pk, Team.objects.get(pk=3).logo_url),
            ("Związek Radziecki U20", 9, None)
        )


@patch("api_server.graphql.mutations.modify.user_has_permission", return_value = True)
class Test__ModifyCountry(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_modify_permission_modify_country(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.MODIFY_COUNTRY_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.MODIFY_COUNTRY_RESPONSE)
        self.assertEqual(
            (Country.objects.get(pk=10).name, Country.objects.get(pk=10).flag_url),
            ("Kanada", "https://placehold.co/600x400")
        )

    def test_cant_owner_modify_country_when_name_is_not_uniq(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_UNIQ_NAME_MODIFY_COUNTRY_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.NOT_UNIQ_NAME_MODIFY_COUNTRY_RESPONSE)
        self.assertEqual(
            (Country.objects.get(pk=10).name, Country.objects.get(pk=10).flag_url),
            ("Argentyna", None)
        )


@patch("api_server.graphql.mutations.modify.user_has_permission", return_value = True)
class Test__ModifyLeague(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_modify_permission_modify_league(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.MODIFY_LEAGUE_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.MODIFY_LEAGUE_RESPONSE)
        self.assertEqual(
            (League.objects.get(pk=4).name, League.objects.get(pk=4).country_of_origin.pk, League.objects.get(pk=4).logo_url),
            ("Nowa Liga", 8, "https://placehold.co/600x400")
        )

    def test_cant_owner_modify_league_when_name_not_uniq(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_UNIQ_NAME_MODIFY_LEAGUE_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.NOT_UNIQ_NAME_MODIFY_LEAGUE_RESPONSE)
        self.assertEqual(
            (League.objects.get(pk=4).name, League.objects.get(pk=4).country_of_origin.pk, League.objects.get(pk=4).logo_url),
            ("Ligue 1", 20, None)
        )

    def test_cant_owner_modify_league_when_country_of_origin_not_exist(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.COUNTRY_NOT_EXIST_MODIFY_LEAGUE_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.COUNTRY_NOT_EXIST_MODIFY_LEAGUE_RESPONSE)
        self.assertEqual(
            (League.objects.get(pk=4).name, League.objects.get(pk=4).country_of_origin.pk, League.objects.get(pk=4).logo_url),
            ("Ligue 1", 20, None)
        )


@patch("api_server.graphql.mutations.modify.user_has_permission", return_value = True)
class Test__ModifyLeagueSeason(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_modify_permission_modify_season(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.MODIFY_SEASON_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.MODIFY_SEASON_RESPONSE)
        self.assertEqual(
            (LeagueSeason.objects.get(pk=4).name,),
            ("1950",)
        )

    def test_cant_admin_without_modify_permission_modify_season(self, mock_has_permission: MagicMock):
        mock_has_permission.return_value = False

        response: dict = self.client.execute(
            data.MODIFY_SEASON_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.MODIFY_SEASON_RESPONSE_NO_PERMISSIONS)
        self.assertEqual(
            (LeagueSeason.objects.get(pk=4).name,),
            ("1990",)
        )

    def test_cant_viewer_modify_season(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.MODIFY_SEASON_REQUEST,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )

        self.assertEqual(response, data.MODIFY_SEASON_RESPONSE_NO_PERMISSIONS)
        self.assertEqual(
            (LeagueSeason.objects.get(pk=4).name,),
            ("1990",)
        )

    def test_can_owner_modify_season(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.MODIFY_SEASON_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.MODIFY_SEASON_RESPONSE)
        self.assertEqual(
            (LeagueSeason.objects.get(pk=4).name,),
            ("1950",)
        )

    def test_cant_owner_modify_season_when_name_is_not_uniq(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NAME_IS_NOT_UNIQ_MODIFY_SEASON_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.NAME_IS_NOT_UNIQ_MODIFY_SEASON_RESPONSE)
        self.assertEqual(
            (LeagueSeason.objects.get(pk=4).name,),
            ("1990",)
        )


@patch("api_server.graphql.mutations.modify.user_has_permission", return_value = True)
class Test__ModifyEventFromMatch(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_modify_permission_modify_event(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.MODIFY_MATCH_EVENT_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.MODIFY_MATCH_EVENT_RESPONSE)
        self.assertEqual(
            (MatchEvent.objects.get(pk=925).player.pk, MatchEvent.objects.get(pk=925).occurrence_minute),
            (40, 5.0)
        )

    def test_cant_admin_without_modify_permission_modify_event(self, mock_has_permission: MagicMock):
        mock_has_permission.return_value = False

        response: dict = self.client.execute(
            data.MODIFY_MATCH_EVENT_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.MODIFY_MATCH_EVENT_RESPONSE_NO_PERMISSIONS)
        self.assertEqual(
            (MatchEvent.objects.get(pk=925).player.pk, MatchEvent.objects.get(pk=925).occurrence_minute),
            (37, Decimal('8.983'))
        )

    def test_cant_viewer_modify_event(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.MODIFY_MATCH_EVENT_REQUEST,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )

        self.assertEqual(response, data.MODIFY_MATCH_EVENT_RESPONSE_NO_PERMISSIONS)
        self.assertEqual(
            (MatchEvent.objects.get(pk=925).player.pk, MatchEvent.objects.get(pk=925).occurrence_minute),
            (37, Decimal('8.983'))
        )

    def test_can_owner_modify_event(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.MODIFY_MATCH_EVENT_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.MODIFY_MATCH_EVENT_RESPONSE)
        self.assertEqual(
            (MatchEvent.objects.get(pk=925).player.pk, MatchEvent.objects.get(pk=925).occurrence_minute),
            (40, 5.0)
        )

    def test_cant_owner_modify_event_for_player_not_taking_part_in_match(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.PLAYER_NOT_TAKING_PART_IN_MATCH_MODIFY_MATCH_EVENT_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.PLAYER_NOT_TAKING_PART_IN_MATCH_MODIFY_MATCH_EVENT_RESPONSE)
        self.assertEqual(
            (MatchEvent.objects.get(pk=925).player.pk, MatchEvent.objects.get(pk=925).occurrence_minute),
            (37, Decimal('8.983'))
        )