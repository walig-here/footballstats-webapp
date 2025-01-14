from datetime import date
from unittest.mock import patch, MagicMock

from django.test import TestCase
from graphene.test import Client as GraphQlClient

from api_server.constants import AdminActions
from api_server.views import schema
from api_server.models import (
    Country, 
    League, 
    LeagueSeason, 
    Match, 
    Team, 
    Player, 
    PlayerInMatch, 
    MatchAdminAction, 
    TeamAdminAction,
    PlayerAdminAction
)

from api_server.tests.integration.__data__.graphql.mutation import create as data
from api_server.tests import testconf as global_testconf


@patch("api_server.graphql.mutations.create.user_has_permission", return_value = True)
class Test__CreateTeam(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_create_permission_create_team(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.CREATE_TEAM_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        
        Team.objects.get(name="Liverpool")
        self.assertEqual(response, data.CREATE_TEAM_RESPONSE_SUCCESS)

    def test_cant_admin_without_create_permission_create_team(self, mock_has_permission: MagicMock):
        mock_has_permission.return_value = False

        response: dict = self.client.execute(
            data.CREATE_TEAM_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.CREATE_TEAM_RESPONSE_NO_PERMISSIONS)
        with self.assertRaises(Team.DoesNotExist):
            Team.objects.get(name="Liverpool")

    def test_cant_viewer_create_team(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.CREATE_TEAM_REQUEST,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )

        self.assertEqual(response, data.CREATE_TEAM_RESPONSE_NO_PERMISSIONS)
        with self.assertRaises(Team.DoesNotExist):
            Team.objects.get(name="Liverpool")

    def test_can_owner_create_team(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.CREATE_TEAM_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        
        Team.objects.get(name="Liverpool")
        self.assertEqual(response, data.CREATE_TEAM_RESPONSE_SUCCESS)

    def test_cant_owner_create_team_with_not_uniq_name(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_UNIQ_NAME_CREATE_TEAM_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        
        self.assertEqual(response, data.NOT_UNIQ_NAME_CREATE_TEAM_RESPONSE_SUCCESS)
        self.assertEqual(Team.objects.filter(name="Argentyna").count(), 1)

    def test_cant_owner_create_team_with_not_existing_country_of_origin(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_EXISTING_COUNTRY_CREATE_TEAM_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.NOT_EXISTING_COUNTRY_CREATE_TEAM_RESPONSE_SUCCESS)
        with self.assertRaises(Team.DoesNotExist):
            Team.objects.get(name="Liverpool")


@patch("api_server.graphql.mutations.create.user_has_permission", return_value = True)
class Test__CreateMatch(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_create_permission_create_new_match(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.CREATE_MATCH_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        
        self.assertEqual(response, data.CREATE_MATCH_RESPONSE_SUCCESS)
        match: Match = Match.objects.get(game_date=date(2018, 5, 26), league_season__pk=2)
        Team.objects.get(pk=3).get_matches(date.min, date.max).get(pk=match.pk)
        Team.objects.get(pk=4).get_matches(date.min, date.max).get(pk=match.pk)
        Player.objects.get(pk=37).get_matches(date.min, date.max).get(pk=match.pk)
        Player.objects.get(pk=38).get_matches(date.min, date.max).get(pk=match.pk)
        Player.objects.get(pk=39).get_matches(date.min, date.max).get(pk=match.pk)
        Player.objects.get(pk=40).get_matches(date.min, date.max).get(pk=match.pk)
        PlayerInMatch.objects.get(player=37, team=3, match=match, minutes_played=45.1)
        PlayerInMatch.objects.get(player=39, team=3, match=match, minutes_played=34.5)
        PlayerInMatch.objects.get(player=38, team=4, match=match, minutes_played=1.5)
        PlayerInMatch.objects.get(player=40, team=4, match=match, minutes_played=90.0)

    def test_cant_admin_without_create_permission_create_new_match(self, mock_has_permission: MagicMock):
        mock_has_permission.return_value = False

        response: dict = self.client.execute(
            data.CREATE_MATCH_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.CREATE_MATCH_RESPONSE_NO_PERMISSIONS)
        with self.assertRaises(Match.DoesNotExist):
            Match.objects.get(game_date=date(2018, 5, 26), league_season__pk=2)
        self.assertEqual(PlayerInMatch.objects.all().count(), 208)
        self.assertEqual(PlayerAdminAction.objects.all().count(), 0)
        self.assertEqual(TeamAdminAction.objects.all().count(), 0)

    def test_cant_viewer_create_new_match(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.CREATE_MATCH_REQUEST,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )

        self.assertEqual(response, data.CREATE_MATCH_RESPONSE_NO_PERMISSIONS)
        with self.assertRaises(Match.DoesNotExist):
            Match.objects.get(game_date=date(2018, 5, 26), league_season__pk=2)
        self.assertEqual(PlayerInMatch.objects.all().count(), 208)
        self.assertEqual(PlayerAdminAction.objects.all().count(), 0)
        self.assertEqual(TeamAdminAction.objects.all().count(), 0)

    def test_can_owner_create_new_match(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.CREATE_MATCH_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        
        self.assertEqual(response, data.CREATE_MATCH_RESPONSE_SUCCESS)
        match: Match = Match.objects.get(game_date=date(2018, 5, 26), league_season__pk=2)
        Team.objects.get(pk=3).get_matches(date.min, date.max).get(pk=match.pk)
        Team.objects.get(pk=4).get_matches(date.min, date.max).get(pk=match.pk)
        Player.objects.get(pk=37).get_matches(date.min, date.max).get(pk=match.pk)
        Player.objects.get(pk=38).get_matches(date.min, date.max).get(pk=match.pk)
        Player.objects.get(pk=39).get_matches(date.min, date.max).get(pk=match.pk)
        Player.objects.get(pk=40).get_matches(date.min, date.max).get(pk=match.pk)
        PlayerInMatch.objects.get(player=37, team=3, match=match, minutes_played=45.1)
        PlayerInMatch.objects.get(player=39, team=3, match=match, minutes_played=34.5)
        PlayerInMatch.objects.get(player=38, team=4, match=match, minutes_played=1.5)
        PlayerInMatch.objects.get(player=40, team=4, match=match, minutes_played=90.0)

    def test_cant_owner_create_match_with_not_existing_season(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_EXISTING_SEASON_CREATE_MATCH_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.NOT_EXISTING_SEASON_CREATE_MATCH_RESPONSE)
        self.assertEqual(Match.objects.all().count(), 5)
        self.assertEqual(PlayerInMatch.objects.all().count(), 208)
        self.assertEqual(PlayerAdminAction.objects.all().count(), 0)
        self.assertEqual(TeamAdminAction.objects.all().count(), 0)

    def test_cant_owner_create_match_with_not_existing_home_team(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_EXISTING_HOME_TEAM_CREATE_MATCH_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.NOT_EXISTING_HOME_TEAM_CREATE_MATCH_RESPONSE)
        self.assertEqual(Match.objects.all().count(), 5)
        self.assertEqual(PlayerInMatch.objects.all().count(), 208)
        self.assertEqual(PlayerAdminAction.objects.all().count(), 0)
        self.assertEqual(TeamAdminAction.objects.all().count(), 0)

    def test_cant_owner_create_match_with_not_existing_away_team(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_EXISTING_AWAY_TEAM_CREATE_MATCH_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.NOT_EXISTING_AWAY_TEAM_CREATE_MATCH_RESPONSE)
        self.assertEqual(Match.objects.all().count(), 5)
        self.assertEqual(PlayerInMatch.objects.all().count(), 208)
        self.assertEqual(PlayerAdminAction.objects.all().count(), 0)
        self.assertEqual(TeamAdminAction.objects.all().count(), 0)

    def test_cant_owner_create_match_with_not_existing_away_player(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_EXISTING_AWAY_PLAYER_CREATE_MATCH_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.NOT_EXISTING_AWAY_PLAYER_CREATE_MATCH_RESPONSE)
        self.assertEqual(Match.objects.all().count(), 5)
        self.assertEqual(PlayerInMatch.objects.all().count(), 208)
        self.assertEqual(PlayerAdminAction.objects.all().count(), 0)
        self.assertEqual(TeamAdminAction.objects.all().count(), 0)

    def test_cant_owner_create_match_with_not_existing_home_player(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_EXISTING_HOME_PLAYER_CREATE_MATCH_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.NOT_EXISTING_HOME_PLAYER_CREATE_MATCH_RESPONSE)
        self.assertEqual(Match.objects.all().count(), 5)
        self.assertEqual(PlayerInMatch.objects.all().count(), 208)
        self.assertEqual(PlayerAdminAction.objects.all().count(), 0)
        self.assertEqual(TeamAdminAction.objects.all().count(), 0)

    def test_cant_owner_create_match_with_player_that_does_not_have_minutes_played(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.PLAYER_HAVE_NO_MINUTES_PLAYED_CREATE_MATCH_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.PLAYER_HAVE_NO_MINUTES_PLAYED_CREATE_MATCH_RESPONSE)
        self.assertEqual(Match.objects.all().count(), 5)
        self.assertEqual(PlayerInMatch.objects.all().count(), 208)
        self.assertEqual(PlayerAdminAction.objects.all().count(), 0)
        self.assertEqual(TeamAdminAction.objects.all().count(), 0)

    def test_cant_owner_create_match_with_player_that_has_non_numeric_minutes_played(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.PLAYER_HAVE_NOT_NUMERIC_MINUTES_PLAYED_CREATE_MATCH_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.PLAYER_HAVE_NOT_NUMERIC_MINUTES_PLAYED_CREATE_MATCH_RESPONSE)
        self.assertEqual(Match.objects.all().count(), 5)
        self.assertEqual(PlayerInMatch.objects.all().count(), 208)
        self.assertEqual(PlayerAdminAction.objects.all().count(), 0)
        self.assertEqual(TeamAdminAction.objects.all().count(), 0)


@patch("api_server.graphql.mutations.create.user_has_permission", return_value = True)
class Test__CreateLeagueSeason(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_create_permission_create_new_season(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.CREATE_LEAGUE_SEASON_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        
        LeagueSeason.objects.get(name="2017/2018", league__name="FIFA U20 World Cup")
        self.assertEqual(response, data.CREATE_LEAGUE_SEASON_RESPONSE_SUCCESS)

    def test_cant_admin_without_create_permission_create_new_season(self, mock_has_permission: MagicMock):
        mock_has_permission.return_value = False

        response: dict = self.client.execute(
            data.CREATE_LEAGUE_SEASON_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.CREATE_LEAGUE_SEASON_RESPONSE_NO_PERMISSIONS)
        with self.assertRaises(LeagueSeason.DoesNotExist):
            LeagueSeason.objects.get(name="2017/2018", league__name="FIFA U20 World Cup")

    def test_cant_viewer_create_new_season(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.CREATE_LEAGUE_SEASON_REQUEST,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )

        self.assertEqual(response, data.CREATE_LEAGUE_SEASON_RESPONSE_NO_PERMISSIONS)
        with self.assertRaises(LeagueSeason.DoesNotExist):
            LeagueSeason.objects.get(name="2017/2018", league__name="FIFA U20 World Cup")

    def test_can_owner_create_new_season(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.CREATE_LEAGUE_SEASON_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        
        LeagueSeason.objects.get(name="2017/2018", league__name="FIFA U20 World Cup")
        self.assertEqual(response, data.CREATE_LEAGUE_SEASON_RESPONSE_SUCCESS)

    def test_can_owner_create_season_with_not_uniq_name_globally_but_uniq_within_league(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NAME_UNIQ_WITHIN_LEAGUE_ONLY_CREATE_LEAGUE_SEASON_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        
        LeagueSeason.objects.get(name="1990", league__name="FIFA U20 World Cup")
        self.assertEqual(response, data.CREATE_LEAGUE_SEASON_RESPONSE_SUCCESS)

    def test_cant_owner_create_season_with_not_uniq_name_when_taken_withing_league(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_UNIQ_NAME_WITHIN_LEAGUE_CREATE_LEAGUE_SEASON_REQUEST,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )

        self.assertEqual(response, data.NOT_UNIQ_NAME_WITHIN_LEAGUE_CREATE_LEAGUE_SEASON_RESPONSE)
        self.assertEqual(LeagueSeason.objects.filter(name="1979", league__name="FIFA U20 World Cup").count(), 1)

    def test_cant_owner_create_season_with_not_existing_league(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOTE_EXISTING_LEAGUE_CREATE_LEAGUE_SEASON_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.NOTE_EXISTING_LEAGUE_CREATE_LEAGUE_SEASON_RESPONSE)
        with self.assertRaises(LeagueSeason.DoesNotExist):
            LeagueSeason.objects.get(name="2017/2018")


@patch("api_server.graphql.mutations.create.user_has_permission", return_value = True)
class Test__CreateLeague(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_create_permission_create_new_league(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.CREATE_LEAGUE_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        created_league: League = League.objects.get(name="Champions League")
        country_of_origin: Country = created_league.country_of_origin

        self.assertEqual(response, data.CREATE_LEAGUE_RESPONSE_SUCCESS)
        self.assertEqual(created_league.name, "Champions League")
        self.assertEqual(country_of_origin.name, "Polska")

    def test_cant_admin_with_no_permission_create_new_league(self, mock_has_permission: MagicMock):
        mock_has_permission.return_value = False

        response: dict = self.client.execute(
            data.CREATE_LEAGUE_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.CREATE_LEAGUE_RESPONSE_NO_PERMISSIONS)
        with self.assertRaises(League.DoesNotExist):
            League.objects.get(name="Champions League")

    def test_cant_viewer_create_new_league(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.CREATE_LEAGUE_REQUEST,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )

        self.assertEqual(response, data.CREATE_LEAGUE_RESPONSE_NO_PERMISSIONS)
        with self.assertRaises(League.DoesNotExist):
            League.objects.get(name="Champions League")

    def test_can_owner_create_new_league(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.CREATE_LEAGUE_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        created_league: League = League.objects.get(name="Champions League")
        country_of_origin: Country = created_league.country_of_origin

        self.assertEqual(response, data.CREATE_LEAGUE_RESPONSE_SUCCESS)
        self.assertEqual(created_league.name, "Champions League")
        self.assertEqual(country_of_origin.name, "Polska")

    def test_cant_owner_create_new_league_with_not_uniq_name(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_UNIQ_NAME_CREATE_LEAGUE_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(response, data.NOT_UNIQ_NAME_CREATE_LEAGUE_RESPONSE)
        self.assertEqual(League.objects.filter(name="FIFA World Cup").count(), 1)

    def test_cant_owner_create_new_league_with_not_existing_country_of_origin(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_EXISTING_COUNTRY_CREATE_LEAGUE_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        self.assertEqual(response, data.NOT_EXISTING_COUNTRY_CREATE_LEAGUE_RESPONSE)
        with self.assertRaises(League.DoesNotExist):
            League.objects.get(name="Champions League")


@patch("api_server.graphql.mutations.create.user_has_permission", return_value = True)
class Test__CreateCountry(TestCase):
    fixtures = ["5matches_2admins"]

    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_can_admin_with_create_permission_create_new_country(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.VALID_CREATE_COUNTRY_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )
        created_country: tuple[dict] = tuple(Country.objects.filter(name="Europa").values('name', 'flag_url'))

        self.assertEqual(response, data.VALID_CREATE_COUNTRY_RESPONSE_SUCCESS)
        self.assertEqual(created_country, data.CREATED_COUNTRY)

    def test_cant_admin_without_create_permission_create_new_country(self, mock_has_permission: MagicMock):
        mock_has_permission.return_value = False

        response: dict = self.client.execute(
            data.VALID_CREATE_COUNTRY_REQUEST,
            context=global_testconf.get_graphql_context_with_admin_logged_in()
        )

        self.assertEqual(response, data.VALID_CREATE_COUNTRY_RESPONSE_NO_PERMISSIONS)
        with self.assertRaises(Country.DoesNotExist):
            Country.objects.get(name="Europa")

    def test_cant_viewer_create_new_country(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.VALID_CREATE_COUNTRY_REQUEST,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )

        self.assertEqual(response, data.VALID_CREATE_COUNTRY_RESPONSE_NO_PERMISSIONS)
        with self.assertRaises(Country.DoesNotExist):
            Country.objects.get(name="Europa")

    def test_can_owner_create_new_country(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.VALID_CREATE_COUNTRY_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )
        created_country: tuple[dict] = tuple(Country.objects.filter(name="Europa").values('name', 'flag_url'))

        self.assertEqual(response, data.VALID_CREATE_COUNTRY_RESPONSE_SUCCESS)
        self.assertEqual(created_country, data.CREATED_COUNTRY)

    def test_cant_create_country_with_not_uniq_name(self, mock_has_permission: MagicMock):
        response: dict = self.client.execute(
            data.NOT_UNIQ_NAME_CREATE_COUNTRY_REQUEST,
            context=global_testconf.get_graphql_context_with_owner_logged_in()
        )

        self.assertEqual(Country.objects.count(), 24)
        self.assertEqual(response, data.NOT_UNIQ_NAME_CREATE_COUNTRY_RESPONSE)