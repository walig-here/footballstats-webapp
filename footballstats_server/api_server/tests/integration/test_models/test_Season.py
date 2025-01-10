from django.test import TestCase

from api_server.models import LeagueSeason, Match


class Test__Season__automatic_delete(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_no_season_relates_to_league_then_delete_league(self):
        season: LeagueSeason = LeagueSeason.objects.all().first()
        season_id: int = season.pk
        Match.objects.filter(league_season=season).delete()
        self.assertEqual(len(LeagueSeason.objects.filter(pk=season_id)), 0)