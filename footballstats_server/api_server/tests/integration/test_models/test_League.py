from django.test import TestCase

from api_server.models import League, Match


class Test__League__automatic_delete(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_no_season_relates_to_league_then_delete_league(self):
        league: League = League.objects.all().first()
        league_id: int = league.pk
        Match.objects.filter(league_season__league=league).delete()
        self.assertEqual(len(League.objects.filter(pk=league_id)), 0)