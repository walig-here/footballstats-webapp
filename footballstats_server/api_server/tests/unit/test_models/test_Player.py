from datetime import date

from django.test import TestCase

from api_server.models import Player, Match, MatchEvent
from api_server.tests.unit.__data__ import Player as data
from api_server.constants import Metrics, MatchEvents, MetricScope


ID_PLAYER_WITH_MULTIPLE_MATCHES: int = 239
ID_PLAYER_WITH_MULTIPLE_TEAMS: int = 55
OLDEST_DATE: date = date(1958, 6, 24)
NEWEST_DATE: date = date(2022, 4, 29)


class Test__Player(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_player_has_matches_then_return_matches(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_MATCHES)
        actual_matches: tuple[Match] = tuple(player.get_matches(OLDEST_DATE, NEWEST_DATE).values())
        self.assertEqual(actual_matches, data.EXPECTED_MATCHES)

    def test_when_player_has_matches_and_date_range_strict_then_return_matches(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_MATCHES)
        actual_matches: tuple[Match] = tuple(player.get_matches(date(1958, 6, 27), NEWEST_DATE).values())
        self.assertEqual(actual_matches, data.EXPECTED_MATCHES_FILTERED_BY_DATE)

    def test_when_player_has_teams_then_return_teams(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual_teams: tuple[Match] = tuple(player.get_teams(OLDEST_DATE, NEWEST_DATE).values())
        self.assertEqual(actual_teams, data.EXPECTED_TEAMS)

    def test_when_player_has_teams_and_date_range_strict_then_return_teams(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual_teams: tuple[Match] = tuple(player.get_teams(OLDEST_DATE, date(1980, 1, 1)).values())
        self.assertEqual(actual_teams, data.EXPECTED_TEAMS_FILTERED_BY_DATE)


class Test__Player__average(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_player_has_events_and_single_match_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            2, 
            MetricScope.METRIC_FOR_ANY_TEAM, 
            Metrics.AVERAGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 28.0 / 90.0)

    def test_when_player_has_events_and_all_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES, 
            MetricScope.METRIC_FOR_ANY_TEAM, 
            Metrics.AVERAGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 52.0 / 180.0)

    def test_when_player_has_events_and_all_team_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES, 
            4, 
            Metrics.AVERAGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 28.0 / 90.0)

    def test_when_player_has_events_and_all_matches_targeted_with_date_filter_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual_sum: float = player.calculate_metric(
            date(1980, 1, 1),
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES, 
            MetricScope.METRIC_FOR_ANY_TEAM, 
            Metrics.AVERAGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual_sum, 24.0 / 90.0)

    def test_when_player_has_no_events_and_single_match_targeted_then_return_0(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        MatchEvent.objects.filter(player=player).delete()
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            2, 
            MetricScope.METRIC_FOR_ANY_TEAM, 
            Metrics.AVERAGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0)


class Test__Player__sum(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_player_has_events_and_single_match_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual_sum: float = player.calculate_metric(
            date.min,
            date.max,
            2, 
            MetricScope.METRIC_FOR_ANY_TEAM, 
            Metrics.SUM, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual_sum, 28)

    def test_when_player_has_events_and_all_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual_sum: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES, 
            MetricScope.METRIC_FOR_ANY_TEAM, 
            Metrics.SUM, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual_sum, 52)

    def test_when_player_has_events_and_all_team_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual_sum: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES, 
            4, 
            Metrics.SUM, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual_sum, 28)

    def test_when_player_has_events_and_all_matches_targeted_with_date_filter_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual_sum: float = player.calculate_metric(
            date(1980, 1, 1),
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES, 
            MetricScope.METRIC_FOR_ANY_TEAM, 
            Metrics.SUM, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual_sum, 24)

    def test_when_player_has_no_events_and_single_match_targeted_then_return_0(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        MatchEvent.objects.filter(player=player).delete()
        actual_sum: float = player.calculate_metric(
            date.min,
            date.max,
            2, 
            MetricScope.METRIC_FOR_ANY_TEAM, 
            Metrics.SUM, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual_sum, 0)