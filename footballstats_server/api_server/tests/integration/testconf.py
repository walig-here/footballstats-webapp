from api_server.models import Match


def create_match_with_no_events() -> Match:
    new_match: Match = Match(game_date="2024-01-01", league_season_id=2)
    new_match.save()
    return new_match