from datetime import date
from django.db import models

from api_server.models import Match, Player, MatchEvent, PlayerInMatch, Team


def delete_all_events_for_team(team: Team) -> None:
    team_players: models.QuerySet[Player] = team.get_players(date.min, date.max)
    MatchEvent.objects.filter(player__in=team_players).delete()

def delete_all_matches_for_player(player: Player) -> None:
    PlayerInMatch.objects.filter(player=player).delete()


def delete_all_matches_for_team(team: Team) -> None:
    PlayerInMatch.objects.filter(team=team).delete()


def make_player_play_for_0_minutes_total(player: Player) -> None:
    for player_in_match in PlayerInMatch.objects.filter(player=player):
        player_in_match.minutes_played = 0.0
        player_in_match.save()


def delete_all_events_for_player(player: Player) -> None:
    MatchEvent.objects.filter(player=player).delete()


def create_match_with_no_events() -> Match:
    new_match: Match = Match(game_date="2024-01-01", league_season_id=2)
    new_match.save()
    return new_match