from datetime import date

from django.test import TestCase

from api_server.models import Team, Match, Player
from api_server.constants import MetricScope, Metrics, MatchEvents, MATCH_LENGTH_MINUTES, METRIC_UNDEFINED_VALUE
from api_server.tests.integration.__data__ import Team as data
from api_server.tests.integration.testconf import delete_all_events_for_team, delete_all_matches_for_team


ID_TEAM_WITH_MULTIPLE_MATCHES: int = 8
OLDEST_DATE: date = date(1958, 6, 24)
NEWEST_DATE: date = date(2022, 4, 29)


class Test__Team(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_team_has_matches_then_return_matches(self):
        player: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: tuple[Match] = tuple(player.get_matches(OLDEST_DATE, NEWEST_DATE).values())
        self.assertEqual(actual, data.EXPECTED_MATCHES)

    def test_when_team_no_matches_then_return_matches(self):
        player: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: tuple[Match] = tuple(player.get_matches(date.min, date.min).values())
        self.assertEqual(actual, ())

    def test_when_team_has_matches_within_date_range_then_return_them(self):
        player: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: tuple[Match] = tuple(player.get_matches(date(1958, 6, 25), NEWEST_DATE).values())
        self.assertEqual(actual, data.EXPECTED_MATCHES_FILTERED_BY_DATE)

    def test_when_team_has_matches_then_return_players(self):
        player: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: tuple[Player] = tuple(player.get_players(OLDEST_DATE, NEWEST_DATE).values())
        self.assertEqual(actual, data.EXPECTED_TEAM_REPRESENTANTS)

    def test_when_team_has_matches_within_date_range_then_return_players(self):
        player: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: tuple[Player] = tuple(player.get_players(date(1958, 6, 25), NEWEST_DATE).values())
        self.assertEqual(actual, data.EXPECTED_TEAM_REPRESENTANTS_FILTERED_BY_DATE)

    def test_when_team_no_matches_then_return_players(self):
        player: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: tuple[Player] = tuple(player.get_players(date.min, date.min).values())
        self.assertEqual(actual, ())


class Test__calculate_metric__odds_in_time_range(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_team_has_events_and_single_match_targeted_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            7,
            Metrics.ODDS_IN_TIME_RANGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["15", "55"]
        )
        self.assertAlmostEqual(actual, 137 / 359)

    def test_when_team_has_events_and_all_matches_targeted_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.ODDS_IN_TIME_RANGE,
            MatchEvents.SUCCESSFUL_PASS,
            ["15", "55"]
        )
        self.assertAlmostEqual(actual, 493 / 1130)

    def test_when_team_has_events_and_all_matches_targeted_and_filtered_by_date_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date(1960, 1, 1),
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.ODDS_IN_TIME_RANGE,
            MatchEvents.SUCCESSFUL_PASS, 
            ["15", "55"]
        )
        self.assertAlmostEqual(actual, 188 / 399)

    def test_when_team_has_no_events_and_all_matches_targeted_then_return_0(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        delete_all_events_for_team(team)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.ODDS_IN_TIME_RANGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["15", "55"]
        )
        self.assertAlmostEqual(actual, 0.0)

    def test_when_team_has_no_matches_and_all_matches_targeted_then_return_0(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.min,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.ODDS_IN_TIME_RANGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["15", "55"]
        )
        self.assertAlmostEqual(actual, 0.0)

    def test_when_team_has_events_and_all_matches_targeted_and_too_many_params_then_raised_ValueError(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        with self.assertRaises(ValueError):
            team.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES,
                Metrics.ODDS_IN_TIME_RANGE, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["15", "55", "1"]
            )

    def test_when_team_has_events_and_all_matches_targeted_and_too_little_params_then_raised_ValueError(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        with self.assertRaises(ValueError):
            team.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES,
                Metrics.ODDS_IN_TIME_RANGE, 
                MatchEvents.SUCCESSFUL_PASS, 
                []
            )

    def test_when_team_has_events_and_all_matches_targeted_and_textual_params_then_raised_ValueError(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        with self.assertRaises(ValueError):
            team.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES,
                Metrics.ODDS_IN_TIME_RANGE, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["a"]
            )


class Test__calculate_metric__odds_for_more_than(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_team_has_events_and_single_match_targeted_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            7,
            Metrics.ODDS_FOR_MORE_THAN, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["370"]
        )
        self.assertAlmostEqual(actual, 0.0)

    def test_when_team_has_events_and_all_matches_targeted_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.ODDS_FOR_MORE_THAN, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["370"]
        )
        self.assertAlmostEqual(actual, 2.0 / 3.0 * 100)

    def test_when_team_has_events_and_all_matches_targeted_and_filtered_by_date_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date(1960, 1, 1),
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.ODDS_FOR_MORE_THAN,
            MatchEvents.SUCCESSFUL_PASS, 
            ["370"]
        )
        self.assertAlmostEqual(actual, 100.0)

    def test_when_team_has_no_events_and_all_matches_targeted_then_return_0(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        delete_all_events_for_team(team)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.ODDS_FOR_MORE_THAN, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["370"]
        )
        self.assertAlmostEqual(actual, 0.0)

    def test_when_team_has_no_matches_and_all_matches_targeted_then_return_0(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.min,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.ODDS_FOR_MORE_THAN, 
            MatchEvents.SUCCESSFUL_PASS, 
            ["370"]
        )
        self.assertAlmostEqual(actual, 0.0)

    def test_when_team_has_events_and_all_matches_targeted_and_too_many_params_then_raised_ValueError(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        with self.assertRaises(ValueError):
            team.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES,
                Metrics.ODDS_FOR_MORE_THAN, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["370", "100"]
            )

    def test_when_team_has_events_and_all_matches_targeted_and_too_little_params_then_raised_ValueError(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        with self.assertRaises(ValueError):
            team.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES,
                Metrics.ODDS_FOR_MORE_THAN, 
                MatchEvents.SUCCESSFUL_PASS, 
                []
            )

    def test_when_team_has_events_and_all_matches_targeted_and_textual_params_then_raised_ValueError(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        with self.assertRaises(ValueError):
            team.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES,
                Metrics.ODDS_FOR_MORE_THAN, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["a"]
            )


class Test__calculate_metric__minutes_until(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_team_has_events_and_single_match_targeted_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            7,
            Metrics.MINUTES_UNTIL, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0.233)

    def test_when_team_has_events_and_all_matches_targeted_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.MINUTES_UNTIL, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0.0)

    def test_when_team_has_events_and_all_matches_targeted_and_filtered_by_date_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date(1960, 1, 1),
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.MINUTES_UNTIL,
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0.0)

    def test_when_team_has_no_events_and_all_matches_targeted_then_return_undefined(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        delete_all_events_for_team(team)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.MINUTES_UNTIL, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, METRIC_UNDEFINED_VALUE)

    def test_when_team_has_no_matches_and_all_matches_targeted_then_return_undefined(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.min,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.MINUTES_UNTIL, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, METRIC_UNDEFINED_VALUE)

    def test_when_team_has_events_and_all_matches_targeted_and_too_many_params_then_raised_ValueError(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        with self.assertRaises(ValueError):
            team.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES,
                Metrics.MINUTES_UNTIL, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["1"]
            )


class Test__calculate_metric__odds_for(TestCase):
    fixtures = ["5matches_2admins"]
    
    def test_when_team_has_events_and_single_match_targeted_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            7,
            Metrics.ODDS_FOR, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 100.0)

    def test_when_team_has_events_and_all_matches_targeted_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.ODDS_FOR, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 100.00)

    def test_when_team_has_events_and_all_matches_targeted_and_filtered_by_date_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date(1960, 1, 1),
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.ODDS_FOR,
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 100.0)

    def test_when_team_has_no_events_and_all_matches_targeted_then_return_0(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        delete_all_events_for_team(team)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.ODDS_FOR, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0.0)

    def test_when_team_has_no_matches_and_all_matches_targeted_then_return_0(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.min,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.ODDS_FOR, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0.0)

    def test_when_team_has_events_and_all_matches_targeted_and_too_many_params_then_raised_ValueError(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        with self.assertRaises(ValueError):
            team.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES,
                Metrics.ODDS_FOR, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["1"]
            )

class Test__calculate_metric__average(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_team_has_events_and_single_match_targeted_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            7,
            Metrics.AVERAGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 359 / (1 * MATCH_LENGTH_MINUTES))

    def test_when_team_has_events_and_all_matches_targeted_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.AVERAGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 1130 / (3 * MATCH_LENGTH_MINUTES))

    def test_when_team_has_events_and_all_matches_targeted_and_filtered_by_date_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date(1960, 1, 1),
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.AVERAGE,
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 399 / (1 * MATCH_LENGTH_MINUTES))

    def test_when_team_has_no_events_and_all_matches_targeted_then_return_0(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        delete_all_events_for_team(team)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.AVERAGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0.0)

    def test_when_team_has_no_matches_and_all_matches_targeted_then_return_0(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.min,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.AVERAGE, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0.0)

    def test_when_team_has_events_and_all_matches_targeted_and_too_many_params_then_raised_ValueError(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        with self.assertRaises(ValueError):
            team.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES,
                Metrics.AVERAGE, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["1"]
            )


class Test__calculate_metric__sum(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_team_has_events_and_single_match_targeted_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            7,
            Metrics.SUM, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 359)

    def test_when_team_has_events_and_all_matches_targeted_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.SUM, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 1130)

    def test_when_team_has_events_and_all_matches_targeted_and_filtered_by_date_then_return_value(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date(1960, 1, 1),
            date.max,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.SUM, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 399)

    def test_when_team_has_no_events_and_all_matches_targeted_then_return_0(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        delete_all_events_for_team(team)
        actual: float = team.calculate_metric(
            date.min,
            date.max,
            7,
            Metrics.SUM, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0)

    def test_when_team_has_no_matches_and_all_matches_targeted_then_return_0(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        actual: float = team.calculate_metric(
            date.min,
            date.min,
            MetricScope.METRIC_FOR_ALL_MATCHES,
            Metrics.SUM, 
            MatchEvents.SUCCESSFUL_PASS, 
            []
        )
        self.assertAlmostEqual(actual, 0)

    def test_when_team_has_events_and_all_matches_targeted_and_too_many_params_then_raised_ValueError(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        with self.assertRaises(ValueError):
            team.calculate_metric(
                date.min,
                date.max,
                MetricScope.METRIC_FOR_ALL_MATCHES,
                Metrics.SUM, 
                MatchEvents.SUCCESSFUL_PASS, 
                ["1"]
            )


class Test__Team__automatic_delete(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_team_does_not_participate_in_matches_then_delete_it(self):
        team: Team = Team.objects.get(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)
        delete_all_matches_for_team(team)
        self.assertEqual(len(Team.objects.filter(pk=ID_TEAM_WITH_MULTIPLE_MATCHES)), 0)