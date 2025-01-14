from datetime import date

from django.test import TestCase

from api_server.models import Player, Match, Country, LeagueSeason
from api_server.tests.integration.__data__ import Player as data
from api_server.tests.integration.testconf import (
    delete_all_events_for_player, make_player_play_for_0_minutes_total, delete_all_matches_for_player
)
from api_server.constants import Metrics, MatchEvents, MetricScope, METRIC_UNDEFINED_VALUE


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


class Test__Player__odds_for_more_than(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_player_has_events_and_single_match_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            2, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_FOR_MORE_THAN, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["25"]
        )
        self.assertAlmostEqual(actual, 100.0)

    def test_when_player_has_events_and_all_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_FOR_MORE_THAN, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["25"]
        )
        self.assertAlmostEqual(actual, 50.0)

    def test_when_player_has_events_and_all_team_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            4, 
            Metrics.ODDS_FOR_MORE_THAN, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["25"]
        )
        self.assertAlmostEqual(actual, 100.0)

    def test_when_player_has_events_and_all_matches_targeted_with_date_filter_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual_sum: float = player.calculate_metric(
            date(1980, 1, 1),
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_FOR_MORE_THAN, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["25"]
        )
        self.assertAlmostEqual(actual_sum, 0.0)

    def test_when_player_has_no_events_all_matches_targeted_then_return_0(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        delete_all_events_for_player(player)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_FOR_MORE_THAN, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["25"]
        )
        self.assertAlmostEqual(actual, 0)

    def test_when_player_played_for_0_minutes_all_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        make_player_play_for_0_minutes_total(player)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value,
            MetricScope.METRIC_FOR_ANY_TEAM.value,
            Metrics.ODDS_FOR_MORE_THAN,
            MatchEvents.SUCCESSFUL_PASS,
            ["25"]
        )
        self.assertAlmostEqual(actual, 50.0)

    def test_when_player_no_matches_targeted_then_return_0(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.min,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_FOR_MORE_THAN, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["25"]
        )
        self.assertAlmostEqual(actual, 0.0)

    def test_when_player_has_events_and_all_matches_targeted_and_too_many_parameters_then_raise_ValueError(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        with self.assertRaises(ValueError):
            player.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES.value, 
                MetricScope.METRIC_FOR_ANY_TEAM.value, 
                Metrics.ODDS_FOR_MORE_THAN, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["24", "14"]
            )

    def test_when_player_has_events_and_all_matches_targeted_and_missing_parameters_then_raise_ValueError(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        with self.assertRaises(ValueError):
            player.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES.value, 
                MetricScope.METRIC_FOR_ANY_TEAM.value, 
                Metrics.ODDS_FOR_MORE_THAN, 
                MatchEvents.SUCCESSFUL_PASS, 
                []
            )

    def test_when_player_has_events_and_all_matches_targeted_and_textual_parameter_then_raise_ValueError(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        with self.assertRaises(ValueError):
            player.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES.value, 
                MetricScope.METRIC_FOR_ANY_TEAM.value, 
                Metrics.ODDS_FOR_MORE_THAN, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["a"]
            )


class Test__Player__minutes_until(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_player_has_events_and_single_match_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            2, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.MINUTES_UNTIL, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 2.683)

    def test_when_player_has_events_and_all_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.MINUTES_UNTIL, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0.667)

    def test_when_player_has_events_and_all_team_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            4, 
            Metrics.MINUTES_UNTIL, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 2.683)

    def test_when_player_has_events_and_all_matches_targeted_with_date_filter_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual_sum: float = player.calculate_metric(
            date(1980, 1, 1),
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.MINUTES_UNTIL, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual_sum, 0.667)

    def test_when_player_has_no_events_all_matches_targeted_then_return_undefined(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        delete_all_events_for_player(player)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.MINUTES_UNTIL, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, METRIC_UNDEFINED_VALUE)

    def test_when_player_played_for_0_minutes_all_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        make_player_play_for_0_minutes_total(player)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value,
            MetricScope.METRIC_FOR_ANY_TEAM.value,
            Metrics.MINUTES_UNTIL,
            MatchEvents.SUCCESSFUL_PASS,
            []
        )
        self.assertAlmostEqual(actual, 0.667)

    def test_when_player_no_matches_targeted_then_return_undefined(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.min,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.MINUTES_UNTIL, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, METRIC_UNDEFINED_VALUE)

    def test_when_player_has_events_and_all_matches_targeted_and_too_many_parameters_then_raise_ValueError(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        with self.assertRaises(ValueError):
            player.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES.value, 
                MetricScope.METRIC_FOR_ANY_TEAM.value, 
                Metrics.MINUTES_UNTIL, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["parameter"]
            )


class Test__Player__odds_in_time_range(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_player_has_events_and_single_match_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            2, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_IN_TIME_RANGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["15", "55"]
        )
        self.assertAlmostEqual(actual, 11.0 / 28.0 * 100)

    def test_when_player_has_events_and_all_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_IN_TIME_RANGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["15", "55"]
        )
        self.assertAlmostEqual(actual, 19.0 / 52.0 * 100)

    def test_when_player_has_events_and_all_team_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            4, 
            Metrics.ODDS_IN_TIME_RANGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["15", "55"]
        )
        self.assertAlmostEqual(actual, 11.0 / 28.0 * 100)

    def test_when_player_has_events_and_all_matches_targeted_with_date_filter_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual_sum: float = player.calculate_metric(
            date(1980, 1, 1),
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_IN_TIME_RANGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["15", "55"]
        )
        self.assertAlmostEqual(actual_sum, 8.0 / 24.0 * 100)

    def test_when_player_has_no_events_all_matches_targeted_then_return_0(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        delete_all_events_for_player(player)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_IN_TIME_RANGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["15", "55"]
        )
        self.assertAlmostEqual(actual, 0.0)

    def test_when_player_played_for_0_minutes_all_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        make_player_play_for_0_minutes_total(player)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value,
            MetricScope.METRIC_FOR_ANY_TEAM.value,
            Metrics.ODDS_IN_TIME_RANGE,
            MatchEvents.SUCCESSFUL_PASS,
            ["15", "55"]
        )
        self.assertAlmostEqual(actual, 19.0 / 52.0 * 100)

    def test_when_player_no_matches_targeted_then_return_0(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.min,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_IN_TIME_RANGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["15", "55"]
        )
        self.assertAlmostEqual(actual, 0)

    def test_when_player_has_events_and_all_matches_targeted_and_too_many_parameters_then_raise_ValueError(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        with self.assertRaises(ValueError):
            player.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES.value, 
                MetricScope.METRIC_FOR_ANY_TEAM.value, 
                Metrics.ODDS_IN_TIME_RANGE, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["15", "55", "66"]
            )

    def test_when_player_has_events_and_all_matches_targeted_and_too_little_parameters_then_raise_ValueError(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        with self.assertRaises(ValueError):
            player.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES.value, 
                MetricScope.METRIC_FOR_ANY_TEAM.value, 
                Metrics.ODDS_IN_TIME_RANGE, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["15"]
            )

    def test_when_player_has_events_and_all_matches_targeted_and_textual_parameter_then_raise_ValueError(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        with self.assertRaises(ValueError):
            player.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES.value, 
                MetricScope.METRIC_FOR_ANY_TEAM.value, 
                Metrics.ODDS_IN_TIME_RANGE, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["15", "a"]
            )

    def test_when_player_has_events_and_all_matches_targeted_and_inverted_range_then_return_0(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.min,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_IN_TIME_RANGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["55", "15"]
        )
        self.assertAlmostEqual(actual, 0)


class Test__Player__odds_for(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_player_has_events_and_single_match_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            2, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_FOR, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 100.0)

    def test_when_player_has_events_and_all_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_FOR, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 100.0)

    def test_when_player_has_events_and_all_team_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            4, 
            Metrics.ODDS_FOR, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 100.0)

    def test_when_player_has_events_and_all_matches_targeted_with_date_filter_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual_sum: float = player.calculate_metric(
            date(1980, 1, 1),
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_FOR, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual_sum, 100.0)

    def test_when_player_has_no_events_all_matches_targeted_then_return_0(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        delete_all_events_for_player(player)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_FOR, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0)

    def test_when_player_played_for_0_minutes_all_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        make_player_play_for_0_minutes_total(player)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value,
            MetricScope.METRIC_FOR_ANY_TEAM.value,
            Metrics.ODDS_FOR,
            MatchEvents.SUCCESSFUL_PASS,
            []
        )
        self.assertAlmostEqual(actual, 100.0)

    def test_when_player_no_matches_targeted_then_return_0(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.min,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.ODDS_FOR, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0)

    def test_when_player_has_events_and_all_matches_targeted_and_too_many_parameters_then_raise_ValueError(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        with self.assertRaises(ValueError):
            player.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES.value, 
                MetricScope.METRIC_FOR_ANY_TEAM.value, 
                Metrics.ODDS_FOR, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["parameter"]
            )


class Test__Player__average(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_player_has_events_and_single_match_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            2, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
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
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
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
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
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
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.AVERAGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual_sum, 24.0 / 90.0)

    def test_when_player_has_no_events_all_matches_targeted_then_return_0(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        delete_all_events_for_player(player)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.AVERAGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0)

    def test_when_player_played_for_0_minutes_all_matches_targeted_then_return_0(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        make_player_play_for_0_minutes_total(player)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.AVERAGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0)

    def test_when_player_no_matches_targeted_then_return_0(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.min,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.AVERAGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0)

    def test_when_player_has_events_and_all_matches_targeted_and_too_many_parameters_then_raise_ValueError(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        with self.assertRaises(ValueError):
            player.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES.value, 
                MetricScope.METRIC_FOR_ANY_TEAM.value, 
                Metrics.AVERAGE, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["parameter"]
            )


class Test__Player__sum(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_player_has_events_and_single_match_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual_sum: float = player.calculate_metric(
            date.min,
            date.max,
            2, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
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
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
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
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
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
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.SUM, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual_sum, 24)

    def test_when_player_has_no_events_and_all_matches_targeted_then_return_0(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        delete_all_events_for_player(player)
        actual_sum: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.SUM, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual_sum, 0)

    def test_when_player_played_for_0_minutes_all_matches_targeted_then_return_value(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        make_player_play_for_0_minutes_total(player)
        actual: float = player.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.SUM, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 52)

    def test_when_player_no_matches_targeted_then_return_0(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        actual: float = player.calculate_metric(
            date.min,
            date.min,
            MetricScope.METRIC_FOR_ALL_MATCHES.value, 
            MetricScope.METRIC_FOR_ANY_TEAM.value, 
            Metrics.SUM, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0)

    def test_when_player_has_events_and_all_matches_targeted_and_too_many_parameters_then_raise_ValueError(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_TEAMS)
        with self.assertRaises(ValueError):
            player.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES.value, 
                MetricScope.METRIC_FOR_ANY_TEAM.value, 
                Metrics.SUM, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["parameter"]
            )


class Test__Player_automatic_delete(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_player_not_participating_in_any_match_then_delete_it_after_match_delete(self):
        player: Player = Player.objects.get(pk=ID_PLAYER_WITH_MULTIPLE_MATCHES)
        delete_all_matches_for_player(player)
        self.assertEqual(len(Player.objects.filter(pk=ID_PLAYER_WITH_MULTIPLE_MATCHES)), 0)

    def test_when_player_not_participating_in_any_match_then_delete_it_after_match_created(self):
        country: Country = Country.objects.get(pk=10)
        league_season: LeagueSeason = LeagueSeason.objects.get(pk=2)
        Player(name="a", surname="a", country_of_origin=country).save()
        Match(game_date=date(1000, 1, 1), league_season=league_season).save()
        self.assertEqual(len(Player.objects.filter(name="a", surname="a")), 0)