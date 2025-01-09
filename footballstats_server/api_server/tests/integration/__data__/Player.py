import datetime


EXPECTED_MATCHES: tuple[dict] = (
    {"id": 6, "game_date": datetime.date(1958,6,29), "league_season_id": 5},
    {"id": 7, "game_date": datetime.date(1958,6,24), "league_season_id": 5}
)

EXPECTED_MATCHES_FILTERED_BY_DATE: tuple[dict] = (
    {"id": 6, "game_date": datetime.date(1958,6,29), "league_season_id": 5},
)

EXPECTED_TEAMS: tuple[dict] = (
    {"id": 4, "name": "Argentyna U20", "logo_url": None, "country_of_origin_id": 10},
    {"id": 7, "name": "Argentyna", "logo_url": None, "country_of_origin_id": 10}
)

EXPECTED_TEAMS_FILTERED_BY_DATE: tuple[dict] = (
    {"id": 4, "name": "Argentyna U20", "logo_url": None, "country_of_origin_id": 10},
)