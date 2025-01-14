from api_server import constants


#-------------------------------------------------------------------------------------
# QUERY MATCH FILTERING ATTRIBUTES
#-------------------------------------------------------------------------------------
MATCH_FILTERING_ATTRIBUTES_QUERY: str = """\
{
    matchFilteringAttributes
}
"""

MATCH_FILTERING_ATTRIBUTES_RESPONSE: dict = {
    "data": {
        "matchFilteringAttributes": list(constants.MATCH_FILTER_ATTRIBUTES)
    }
}

#-------------------------------------------------------------------------------------
# QUERY MATCH SORTING ATTRIBUTES
#-------------------------------------------------------------------------------------
MATCH_SORTING_ATTRIBUTES_QUERY: str = """\
{
    matchSortingAttributes
}
"""

MATCH_SORTING_ATTRIBUTES_RESPONSE: dict = {
    "data": {
        "matchSortingAttributes": list(constants.MATCH_SORT_ATTRIBUTES)
    }
}

#-------------------------------------------------------------------------------------
# QUERY MATCH OWN DATA
#-------------------------------------------------------------------------------------
MATCH_OWN_DATA_QUERY: str = """\
{
    match(id: 2){
        id
        gameDate,
    }
}
"""

MATCH_OWN_DATA_RESPONSE: dict = {
    "data": {
        "match": {
            "id": "2",
            "gameDate": "1979-09-07"
        }
    }
}

#-------------------------------------------------------------------------------------
# QUERY TEAM SCORES
#-------------------------------------------------------------------------------------
MATCH_TEAM_SCORES_QUERY: str = """\
{
    match(id: 2){
        teamsScores{
            score,
            teamId
        }
    }
}
"""

MATCH_TEAM_SCORES_RESPONSE: dict = {
    "data": {
        "match": {
            "teamsScores": [
                {"score": 3, "teamId": 4},
                {"score": 1, "teamId": 3},
            ]
        }
    }
}

#-------------------------------------------------------------------------------------
# QUERY ALL MATCH LIST
#-------------------------------------------------------------------------------------
ALL_MATCHES_LIST_QUERY: str = """\
query(
    $startDate: Date = "1900-01-01",
    $endDate: Date = "2200-01-01"
){
    matchesList(
        startDate: $startDate,
        endDate: $endDate,
        page: 0,
    ) {
        id,
        gameDate
    }
}
"""

ALL_MATCHES_LIST_RESPONSE: dict = {
    "data": {
        "matchesList": [
            {"id": "9", "gameDate": "2022-04-29"},
            {"id": "4", "gameDate": "1990-06-24"},
            {"id": "2", "gameDate": "1979-09-07"},
            {"id": "6", "gameDate": "1958-06-29"},
            {"id": "7", "gameDate": "1958-06-24"},
        ]
    }
}


#-------------------------------------------------------------------------------------
# QUERY MATCH EVENTS
#-------------------------------------------------------------------------------------
MATCH_EVENTS_QUERY: str = """\
{
    match(id: 2){
        events{
            occurrenceMinute,
        }
    }
}
"""

#-------------------------------------------------------------------------------------
# QUERY MATCH LEAGUE AND SEASON 
#-------------------------------------------------------------------------------------
MATCH_LEAGUE_SEASON_QUERY: str = """\
{
    match(id: 2){
        leagueSeason{
            name,
            league{
                name,
                countryOfOrigin{
                    name
                }
            }
        }
    }
}
"""

MATCH_LEAGUE_SEASON_RESPONSE: dict = {
    "data": {
        "match": {
            "leagueSeason": {
                "name": "1979",
                "league": {
                    "name": "FIFA U20 World Cup",
                    "countryOfOrigin": {
                        "name": "Międzynarodowy"
                    }
                }
            }
        }
    }
}

#-------------------------------------------------------------------------------------
# PLAYER MATCH LIST
#-------------------------------------------------------------------------------------

PLAYER_MATCHES_LIST_QUERY: str = """\
query(
    $startDate: Date = "1900-01-01",
    $endDate: Date = "2200-01-01"
){
    matchesList(
        startDate: $startDate,
        endDate: $endDate,
        page: 0,
        playerInvolved: 55
    ) {
        id,
        gameDate,
    },
}
"""

PLAYER_MATCHES_LIST_RESPONSE: dict = {
    "data": {
        "matchesList": [
            {"id": "4", "gameDate": "1990-06-24"},
            {"id": "2", "gameDate": "1979-09-07"},
        ]
    }
}

#-------------------------------------------------------------------------------------
# TEAM MATCH LIST
#-------------------------------------------------------------------------------------

TEAM_MATCHES_LIST_QUERY: str = """\
query(
    $startDate: Date = "1900-01-01",
    $endDate: Date = "2200-01-01"
){
    matchesList(
        startDate: $startDate,
        endDate: $endDate,
        page: 0,
        teamInvolved: 3
    ) {
        id,
        gameDate,
    },
}
"""

TEAM_MATCHES_LIST_RESPONSE: dict = {
    "data": {
        "matchesList": [
            {"id": "2", "gameDate": "1979-09-07"},
        ]
    }
}

#-------------------------------------------------------------------------------------
# MATCH SUM SHOT NOT ON TARGET
#-------------------------------------------------------------------------------------

MATCH_SUM_SHOT_NOT_ON_TARGET_QUERY: str = """\
{
    match(id: 2){
        calculateMetric(
            metric: {
                metricType: SUM,
                targetMatchEvent: SHOT_NOT_ON_TARGET,
                metricParams: []
            }
        )
    }
}
"""

MATCH_SUM_SHOT_NOT_ON_TARGET_RESPONSE: dict = {
    "data": {
        "match": {
        "calculateMetric": 25
        }
    }
}

#-------------------------------------------------------------------------------------
# MATCH AVERAGE SHOT NOT ON TARGET
#-------------------------------------------------------------------------------------

MATCH_AVERAGE_SHOT_NOT_ON_TARGET_QUERY: str = """\
{
    match(id: 2){
        calculateMetric(
            metric: {
                metricType: AVERAGE,
                targetMatchEvent: SHOT_NOT_ON_TARGET,
                metricParams: []
            }
        )
    }
}
"""

MATCH_AVERAGE_SHOT_NOT_ON_TARGET_RESPONSE: dict = {
    "data": {
        "match": {
        "calculateMetric": 25.0 / 90.0
        }
    }
}

#-------------------------------------------------------------------------------------
# MATCH ODDS_FOR SHOT NOT ON TARGET
#-------------------------------------------------------------------------------------

MATCH_ODDS_FOR_SHOT_NOT_ON_TARGET_QUERY: str = """\
{
    match(id: 2){
        calculateMetric(
            metric: {
                metricType: ODDS_FOR,
                targetMatchEvent: SHOT_NOT_ON_TARGET,
                metricParams: []
            }
        )
    }
}
"""

MATCH_ODDS_FOR_SHOT_NOT_ON_TARGET_RESPONSE: dict = {
    "data": {
        "match": {
        "calculateMetric": 100.0
        }
    }
}

#-------------------------------------------------------------------------------------
# MATCH ODDS_FOR_MORE_THAN SHOT NOT ON TARGET
#-------------------------------------------------------------------------------------

MATCH_ODDS_FOR_MORE_THAN_SHOT_NOT_ON_TARGET_QUERY: str = """\
{
    match(id: 2){
        calculateMetric(
            metric: {
                metricType: ODDS_FOR_MORE_THAN,
                targetMatchEvent: SHOT_NOT_ON_TARGET,
                metricParams: ["100"]
            }
        )
    }
}
"""

MATCH_ODDS_FOR_MORE_THAN_SHOT_NOT_ON_TARGET_RESPONSE: dict = {
    "data": {
        "match": {
        "calculateMetric": 0.0
        }
    }
}

#-------------------------------------------------------------------------------------
# MATCH MINUTES_UNTIL SHOT NOT ON TARGET
#-------------------------------------------------------------------------------------

MATCH_MINUTES_UNTIL_SHOT_NOT_ON_TARGET_QUERY: str = """\
{
    match(id: 2){
        calculateMetric(
            metric: {
                metricType: MINUTES_UNTIL,
                targetMatchEvent: SHOT_NOT_ON_TARGET,
                metricParams: []
            }
        )
    }
}
"""

MATCH_MINUTES_UNTIL_SHOT_NOT_ON_TARGET_RESPONSE: dict = {
    "data": {
        "match": {
        "calculateMetric": 2.8
        }
    }
}

#-------------------------------------------------------------------------------------
# MATCH ODDS_IN_TIME_RANGE SHOT NOT ON TARGET
#-------------------------------------------------------------------------------------

MATCH_ODDS_IN_TIME_RANGE_SHOT_NOT_ON_TARGET_QUERY: str = """\
{
    match(id: 2){
        calculateMetric(
            metric: {
                metricType: ODDS_IN_TIME_RANGE,
                targetMatchEvent: SHOT_NOT_ON_TARGET,
                metricParams: ["15", "80"]
            }
        )
    }
}
"""

MATCH_ODDS_IN_TIME_RANGE_SHOT_NOT_ON_TARGET_RESPONSE: dict = {
    "data": {
        "match": {
        "calculateMetric": 64.0
        }
    }
}