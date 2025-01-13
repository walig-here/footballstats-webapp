#-------------------------------------------------------------------------------------
# QUERY FOR LEAGUES
#-------------------------------------------------------------------------------------

LEAGUE_LIST_QUERY: str = """\
{
    leaguesList{
        name
    }
}
"""

LEAGUE_LIST_RESPONSE = {
    "data": {
        "leaguesList": [
            {"name": "FIFA U20 World Cup"},
            {"name": "FIFA World Cup"},
            {"name": "Ligue 1"},
        ]
    }
}

#-------------------------------------------------------------------------------------
# QUERY FOR LEAGUE SEASON
#-------------------------------------------------------------------------------------

LEAGUE_SEASON_LIST_QUERY: str = """\
{
    leagueSeasonsList(leagueId: 3){
        id,
        name,
    }
}
"""

LEAGUE_SEASON_LIST_RESPONSE = {
    "data": {
        "leagueSeasonsList": [
            {"id": "5", "name": "1958"},
            {"id": "4", "name": "1990"},
        ]
    }
}