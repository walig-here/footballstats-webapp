from django.test import TestCase

from api_server.models import MatchEvent, PlayerInMatch, Player


class Test__MatchEvent__automatic_delete(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_player_not_exist_in_match_then_delete_event(self):
        match_event: MatchEvent = MatchEvent.objects.all().first()
        match_event_id: int = match_event.pk
        PlayerInMatch.objects.get(player=match_event.player, match=match_event.match).delete()
        self.assertEqual(len(MatchEvent.objects.filter(pk=match_event_id)), 0)

    def test_when_player_not_exist_in_system_then_delete_event(self):
        match_event: MatchEvent = MatchEvent.objects.all().first()
        match_event_id: int = match_event.pk
        match_event.player.delete()
        self.assertEqual(len(MatchEvent.objects.filter(pk=match_event_id)), 0)

    def test_when_match_not_exist_in_system_then_delete_event(self):
        match_event: MatchEvent = MatchEvent.objects.all().first()
        match_event_id: int = match_event.pk
        match_event.match.delete()
        self.assertEqual(len(MatchEvent.objects.filter(pk=match_event_id)), 0)