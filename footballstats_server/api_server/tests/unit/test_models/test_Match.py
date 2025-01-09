from django.test import TestCase
from django.forms.models import model_to_dict

from api_server.constants import MatchEvents, Metrics, METRIC_UNDEFINED_VALUE
from api_server.models import Match, Player, Team, MatchEvent
from api_server.tests.unit.__data__ import Match as data
from api_server.tests.unit.testconf import create_match_with_no_events


class TestMatch(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_match_has_players_then_return_query_set_with_them(self) -> None:
        tested_match: Match = Match.objects.get(pk=2)
        actual_participants: tuple[Player] = tuple(tested_match.get_players().values())

        self.assertEqual(actual_participants, data.EXPECTED_MATCH_PLAYER_PARTICIPANTS)

    def test_when_match_has_team_then_return_query_with_them(self) -> None:
        tested_match: Match = Match.objects.get(pk=2)
        actual_teams: tuple[Team] = tuple(tested_match.get_teams().values())
        
        self.assertEqual(actual_teams, data.EXPECTED_MATCH_TEAM_PARTICIPANTS)

    def test_when_match_has_events_then_return_query_with_them(self) -> None:
        tested_match: Match = Match.objects.get(pk=2)
        actual_events: tuple[MatchEvent] = tuple(tested_match.get_events().values())

        self.assertEqual(actual_events, data.EXPECTED_MATCH_EVENTS)

    def test_when_match_has_no_events_then_return_empty_query(self):
        new_match: Match = create_match_with_no_events()

        actual_events: tuple[MatchEvent] = tuple(new_match.get_events().values())
        
        self.assertEqual(actual_events, ())

    def test_when_match_has_events_then_return_score(self):
        tested_match: Match = Match.objects.get(pk=2)
        actual_scores: tuple[tuple[dict, int]] = [
            (model_to_dict(team), score)
            for team, score in tested_match.get_result().items()
        ]
        
        self.assertEqual(actual_scores, data.EXPECTED_MATCH_RESULT)

    def test_when_match_has_no_events_then_return_0_to_0_score(self):
        tested_match: Match = Match.objects.get(pk=2)
        tested_match.get_events().delete()
        actual_scores: tuple[tuple[dict, int]] = [
            (model_to_dict(team), score)
            for team, score in tested_match.get_result().items()
        ]
        
        self.assertEqual(actual_scores, data.EXPECTED_MATCH_RESULT_NO_EVENTS)

    def test_when_match_exist_then_return_its_admin_actions(self):
        tested_match: Match = Match.objects.get(pk=2)
        actual_events: tuple[MatchEvent] = tuple(tested_match.get_admin_actions().values())

        self.assertEqual(actual_events, data.EXPECTED_MATCH_ADMIN_ACTIONS)


class TestMatch__calculate_metric__sum(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_match_has_events_then_return_metric_value(self):
        tested_match: Match = Match.objects.get(pk=2)
        actual_sum: float = tested_match.calculate_metric(Metrics.SUM, MatchEvents.SHOT_NOT_ON_TARGET, [])
        self.assertAlmostEqual(25.0, actual_sum)

    def test_when_match_has_no_events_then_return_value_0(self):
        tested_match: Match = create_match_with_no_events()
        actual_sum: float = tested_match.calculate_metric(Metrics.SUM, MatchEvents.SHOT_NOT_ON_TARGET, [])
        self.assertAlmostEqual(0.0, actual_sum)

    def test_when_match_has_events_and_has_not_needed_parameters_then_raise_ValueError(self):
        tested_match: Match = Match.objects.get(pk=2)
        with self.assertRaises(ValueError):
            tested_match.calculate_metric(Metrics.SUM, MatchEvents.SHOT_NOT_ON_TARGET, ["a", "b"])


class TestMatch__calculate_metric__average(TestCase):
    fixtures = ["5matches_2admins"]
    
    def test_when_match_has_events_then_return_metric_value(self):
        EXPECTED_VALUE: float = 25.0 / 90.0
        tested_match: Match = Match.objects.get(pk=2)
        actual_average: float = tested_match.calculate_metric(Metrics.AVERAGE, MatchEvents.SHOT_NOT_ON_TARGET, [])
        self.assertAlmostEqual(EXPECTED_VALUE, actual_average)

    def test_when_match_has_no_events_then_return_value_0(self):
        tested_match: Match = create_match_with_no_events()
        actual_average: float = tested_match.calculate_metric(Metrics.AVERAGE, MatchEvents.SHOT_NOT_ON_TARGET, [])
        self.assertAlmostEqual(0.0, actual_average)

    def test_when_match_has_events_and_has_not_needed_parameters_then_raise_ValueError(self):
        tested_match: Match = Match.objects.get(pk=2)
        with self.assertRaises(ValueError):
            tested_match.calculate_metric(Metrics.AVERAGE, MatchEvents.SHOT_NOT_ON_TARGET, ["a", "b"])


class TestMatch__calculate_metric__odds_for(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_match_has_events_then_return_metric_value(self):
        tested_match: Match = Match.objects.get(pk=2)
        actual_odds_for: float = tested_match.calculate_metric(Metrics.ODDS_FOR, MatchEvents.SHOT_ON_TARGET, [])
        self.assertAlmostEqual(actual_odds_for, 100.0)

    def test_when_match_has_no_events_then_return_value_0(self):
        tested_match: Match = create_match_with_no_events()
        actual_odds_for: float = tested_match.calculate_metric(Metrics.ODDS_FOR, MatchEvents.SHOT_NOT_ON_TARGET, [])
        self.assertAlmostEqual(0.0, actual_odds_for)

    def test_when_match_has_events_and_has_not_needed_parameters_then_raise_ValueError(self):
        tested_match: Match = Match.objects.get(pk=2)
        with self.assertRaises(ValueError):
            tested_match.calculate_metric(Metrics.ODDS_FOR, MatchEvents.SHOT_NOT_ON_TARGET, ["a", "b"])


class TestMatch__calculate_metric__odds_for_more_than(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_match_has_events_then_return_metric_value(self):
        tested_match: Match = Match.objects.get(pk=2)
        actual_odds_for_more_than: float = tested_match.calculate_metric(
            Metrics.ODDS_FOR_MORE_THAN, MatchEvents.SHOT_NOT_ON_TARGET, ["100"]
        )
        self.assertAlmostEqual(actual_odds_for_more_than, 0.0)

    def test_when_match_has_no_events_then_return_value_0(self):
        tested_match: Match = create_match_with_no_events()
        actual_odds_for_more_than: float = tested_match.calculate_metric(
            Metrics.ODDS_FOR_MORE_THAN, MatchEvents.SHOT_NOT_ON_TARGET, ["100"]
        )
        self.assertAlmostEqual(0.0, actual_odds_for_more_than)

    def test_when_match_has_events_and_textual_parameter_then_raise_ValueError(self):
        tested_match: Match = Match.objects.get(pk=2)
        with self.assertRaises(ValueError):
            tested_match.calculate_metric(Metrics.ODDS_FOR_MORE_THAN, MatchEvents.SHOT_NOT_ON_TARGET, ["text"])

    def test_when_match_has_events_and_too_many_parameters_then_raise_ValueError(self):
        tested_match: Match = Match.objects.get(pk=2)
        with self.assertRaises(ValueError):
            tested_match.calculate_metric(Metrics.ODDS_FOR_MORE_THAN, MatchEvents.SHOT_NOT_ON_TARGET, ["100", "51"])


class TestMatch__calculate_metric__minutes_until(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_match_has_events_then_return_value(self):
        tested_match: Match = Match.objects.get(pk=2)
        actual_minutes_until: float = tested_match.calculate_metric(
            Metrics.MINUTES_UNTIL, MatchEvents.SHOT_NOT_ON_TARGET, []
        )
        self.assertAlmostEqual(actual_minutes_until, 2.8)

    def test_when_match_has_no_events_then_return_value_undefined(self):
        tested_match: Match = create_match_with_no_events()
        actual_minutes_until: float = tested_match.calculate_metric(
            Metrics.MINUTES_UNTIL, MatchEvents.SHOT_NOT_ON_TARGET, []
        )
        self.assertAlmostEqual(METRIC_UNDEFINED_VALUE, actual_minutes_until)

    def test_when_match_has_events_and_too_much_parameters_then_raise_ValueError(self):
        tested_match: Match = Match.objects.get(pk=2)
        with self.assertRaises(ValueError):
            tested_match.calculate_metric(Metrics.MINUTES_UNTIL, MatchEvents.SHOT_NOT_ON_TARGET, ["100"])

class TestMatch__calculate_metric__odds_in_time_range(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_match_has_events_then_return_value(self):
        tested_match: Match = Match.objects.get(pk=2)
        actual_odds_in_time_range: float = tested_match.calculate_metric(
            Metrics.ODDS_IN_TIME_RANGE, MatchEvents.SHOT_NOT_ON_TARGET, ["15", "80"]
        )
        self.assertAlmostEqual(actual_odds_in_time_range, 0.64)

    def test_when_match_has_events_and_invalid_range_then_return_0(self):
        tested_match: Match = Match.objects.get(pk=2)
        actual_odds_in_time_range: float = tested_match.calculate_metric(
            Metrics.ODDS_IN_TIME_RANGE, MatchEvents.SHOT_NOT_ON_TARGET, ["80", "15"]
        )
        self.assertAlmostEqual(actual_odds_in_time_range, 0.0)

    def test_when_match_has_events_and_too_many_arguments_then_raise_ValueError(self):
        tested_match: Match = Match.objects.get(pk=2)
        with self.assertRaises(ValueError):
            tested_match.calculate_metric(
                Metrics.ODDS_IN_TIME_RANGE, MatchEvents.SHOT_NOT_ON_TARGET, ["15", "80", "45"]
            )

    def test_when_match_has_events_and_textual_argument_then_raise_ValueError(self):
        tested_match: Match = Match.objects.get(pk=2)
        with self.assertRaises(ValueError):
            tested_match.calculate_metric(
                Metrics.ODDS_IN_TIME_RANGE, MatchEvents.SHOT_NOT_ON_TARGET, ["15", "a"]
            )

    def test_when_match_has_no_events_then_return_value_0(self):
        tested_match: Match = create_match_with_no_events()
        actual_odds_in_time_range: float = tested_match.calculate_metric(
            Metrics.ODDS_IN_TIME_RANGE, MatchEvents.SHOT_NOT_ON_TARGET, ["15", "80"]
        )
        self.assertAlmostEqual(0.0, actual_odds_in_time_range)


class Test__automaticDelete(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_one_participating_team_is_not_represented_by_any_player_then_delete_match(self):
        Match.objects.get(pk=2).get_players().filter(playerinmatch__team_id=4).order_by('id').delete()
        self.assertEqual(len(Match.objects.filter(pk=2)), 0)

    def test_when_one_participating_team_not_exist_then_delete_match(self):
        Match.objects.get(pk=2).get_teams()[1].delete()
        self.assertEqual(len(Match.objects.filter(pk=2)), 0)