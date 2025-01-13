from api_server import constants


#-------------------------------------------------------------------------------------
# QUERY TEAM SORTING ATTRIBUTES
#-------------------------------------------------------------------------------------

TEAM_SORTING_ATTRIBUTES_QUERY: str = """\
{
    teamSortingAttributes
}
"""

TEAM_SORTING_ATTRIBUTES_RESPONSE: dict = {
    "data": {
        "teamSortingAttributes": list(constants.TEAM_SORT_ATTRIBUTES)
    }
}

#-------------------------------------------------------------------------------------
# QUERY TEAM FILTERING ATTRIBUTES
#-------------------------------------------------------------------------------------

TEAM_FILTERING_ATTRIBUTES_QUERY: str = """\
{
    teamFilteringAttributes
}
"""

TEAM_FILTERING_ATTRIBUTES_RESPONSE: dict = {
    "data": {
        "teamFilteringAttributes": list(constants.TEAM_FILTER_ATTRIBUTES)
    }
}

#-------------------------------------------------------------------------------------
# QUERY TEAM OWN DATA
#-------------------------------------------------------------------------------------

TEAM_OWN_DATA_QUERY: str = """\
{
    team(id: 7) {
        id,
        name,
        logoUrl
    }
}
"""

TEAM_OWN_DATA_RESPONSE: dict = {
    "data": {
        "team": {
            "id": "7", 
            "name": "Argentyna", 
            "logoUrl": None,
        }
    }
}

#-------------------------------------------------------------------------------------
# QUERY TEAM COUNTRY OF ORIGIN DATA
#-------------------------------------------------------------------------------------

TEAM_COUNTRY_OF_ORIGIN_QUERY: str = """\
{
    team(id: 7){
        countryOfOrigin {
            name,
            flagUrl
        }
    }
}
"""

TEAM_COUNTRY_OF_ORIGIN_RESPONSE: dict = {
    "data": {
        "team": {
            "countryOfOrigin": {
                "name": "Argentyna",
                "flagUrl": None
            }
        }
    }
}

#-------------------------------------------------------------------------------------
# QUERY TEAM SUM FOR SUCCESSFUL PASS SINGLE MATCH
#-------------------------------------------------------------------------------------

TEAM_SUCCESSFUL_PASS_SUM_FOR_SINGLE_MARCH_QUERY: str = """\
{
    team(id: 8){
        calculateMetric(
            startDate: "1900-01-01",
            endDate: "2200-01-01",
            match: 7,
            metric: {
                metricType: SUM,
                targetMatchEvent: SUCCESSFUL_PASS,
                metricParams: []
            }
        )
    }
}
"""

TEAM_SUCCESSFUL_PASS_SUM_FOR_SINGLE_MARCH_RESPONSE: dict = {
    "data": {
        "team": {
            "calculateMetric": 359
        }
    }
}

#-------------------------------------------------------------------------------------
# QUERY TEAM AVERAGE FOR SUCCESSFUL PASS ALL MATCHES
#-------------------------------------------------------------------------------------

TEAM_SUCCESSFUL_PASS_AVERAGE_ALL_MATCHES_QUERY: str = """\
{
    team(id: 8){
        calculateMetric(
            startDate: "1900-01-01",
            endDate: "2200-01-01",
            match: -1,
            metric: {
                metricType: AVERAGE,
                targetMatchEvent: SUCCESSFUL_PASS,
                metricParams: []
            }
        )
    }
}
"""

TEAM_SUCCESSFUL_PASS_AVERAGE_ALL_MATCHES_RESPONSE: dict = {
    "data": {
        "team": {
            "calculateMetric": 1130 / (3 * constants.MATCH_LENGTH_MINUTES)
        }
    }
}

#-------------------------------------------------------------------------------------
# QUERY TEAM ODDS FOR FOR SUCCESSFUL PASS ALL MATCHES
#-------------------------------------------------------------------------------------

TEAM_SUCCESSFUL_PASS_ODDS_FOR_ALL_MATCHES_QUERY: str = """\
{
    team(id: 8){
        calculateMetric(
            startDate: "1900-01-01",
            endDate: "2200-01-01",
            match: -1,
            metric: {
                metricType: ODDS_FOR,
                targetMatchEvent: SUCCESSFUL_PASS,
                metricParams: []
            }
        )
    }
}
"""

TEAM_SUCCESSFUL_PASS_ODDS_FOR_ALL_MATCHES_RESPONSE: dict = {
    "data": {
        "team": {
            "calculateMetric": 100.0
        }
    }
}

#-------------------------------------------------------------------------------------
# QUERY TEAM ODDS FOR MORE THAN FOR SUCCESSFUL PASS SINGLE MATCH
#-------------------------------------------------------------------------------------

TEAM_SUCCESSFUL_PASS_ODDS_FOR_MORE_THAN_SINGLE_MARCH_QUERY: str = """\
{
    team(id: 8){
        calculateMetric(
            startDate: "1900-01-01",
            endDate: "2200-01-01",
            match: 7,
            metric: {
                metricType: ODDS_FOR_MORE_THAN,
                targetMatchEvent: SUCCESSFUL_PASS,
                metricParams: ["370"]
            }
        )
    }
}
"""

TEAM_SUCCESSFUL_PASS_ODDS_FOR_MORE_THAN_SINGLE_MARCH_RESPONSE: dict = {
    "data": {
        "team": {
            "calculateMetric": 0.0
        }
    }
}

#-------------------------------------------------------------------------------------
# QUERY TEAM MINUTES UNTIL FOR SUCCESSFUL PASS ALL MATCHES
#-------------------------------------------------------------------------------------

TEAM_SUCCESSFUL_PASS_MINUTES_UNTIL_ALL_MATCHES_QUERY: str = """\
{
    team(id: 8){
        calculateMetric(
            startDate: "1900-01-01",
            endDate: "2200-01-01",
            match: -1,
            metric: {
                metricType: MINUTES_UNTIL,
                targetMatchEvent: SUCCESSFUL_PASS,
                metricParams: []
            }
        )
    }
}
"""

TEAM_SUCCESSFUL_PASS_MINUTES_UNTIL_ALL_MATCHES_RESPONSE: dict = {
    "data": {
        "team": {
            "calculateMetric": 0.0
        }
    }
}

#-------------------------------------------------------------------------------------
# QUERY TEAM MINUTES ODDS FOR IN TIME RANGE SUCCESSFUL PASS SINGLE MATCH
#-------------------------------------------------------------------------------------

TEAM_SUCCESSFUL_ODDS_INT_TIME_RANGE_SINGLE_MATCH_QUERY: str = """\
{
    team(id: 8){
        calculateMetric(
            startDate: "1900-01-01",
            endDate: "2200-01-01",
            match: -1,
            metric: {
                metricType: ODDS_IN_TIME_RANGE,
                targetMatchEvent: SUCCESSFUL_PASS,
                metricParams: ["15", "55"]
            }
        )
    }
}
"""

TEAM_SUCCESSFUL_ODDS_INT_TIME_RANGE_SINGLE_MATCH_RESPONSE: dict = {
    "data": {
        "team": {
            "calculateMetric": 493 / 1130 * 100
        }
    }
}

#-------------------------------------------------------------------------------------
# QUERY TEAM METRIC HISTORY FOR ODDS IN TIME RANGE FOR SUCCESSFUL PASS
#-------------------------------------------------------------------------------------

TEAM_METRIC_HISTORY_SUM_SUCCESSFUL_PASS_QUERY: str = """\
{
    team(id: 8){
        metricHistory(
            startDate: "1900-01-01",
            endDate: "2500-01-01",
            metric: {
                metricType: SUM,
                targetMatchEvent: SUCCESSFUL_PASS,
                metricParams: []
            }
        ) {
            time,
            value
        }
    }
}
"""

TEAM_METRIC_HISTORY_SUM_SUCCESSFUL_PASS_RESPONSE: dict = {
    "data": {
        "team": {
            "metricHistory": [
                {"time": "1900-01-01", "value": 0.0},
                {"time": "1958-06-24", "value": 359.0},
                {"time": "1958-06-29", "value": 731.0},
                {"time": "1990-06-24", "value": 1130.0},
                {"time": "2500-01-01", "value": 1130.0},
            ]
        }
    }
}

#-------------------------------------------------------------------------------------
# QUERY ALL TEAMS LIST
#-------------------------------------------------------------------------------------

ALL_TEAMS_QUERY: str = """\
query(
    $startDate: Date = "1900-01-01",
    $endDate: Date = "2500-01-01"
){
    teamsList(
        startDate: $startDate,
        endDate: $endDate,
        page: 0,
    ) {
        id
    }
}
"""

ALL_TEAMS_RESPONSE: dict = {
    "data": {
        "teamsList": [
            {"id": "7"},
            {"id": "4"},
            {"id": "8"},
            {"id": "16"},
            {"id": "17"},
            {"id": "18"},
            {"id": "12"},
            {"id": "3"},
        ]
    }
}

#-------------------------------------------------------------------------------------
# QUERY MATCH TEAMS LIST
#-------------------------------------------------------------------------------------

MATCH_TEAMS_QUERY: str = """\
query(
    $startDate: Date = "1900-01-01",
    $endDate: Date = "2500-01-01"
){
    teamsList(
        startDate: $startDate,
        endDate: $endDate,
        page: 0,
        playingInMatch: 4
    ) {
        id
    }
}
"""

MATCH_TEAMS_RESPONSE: dict = {
    "data": {
        "teamsList": [
            {"id": "7"},
            {"id": "8"},
        ]
    }
}

#-------------------------------------------------------------------------------------
# QUERY PLAYER TEAMS LIST
#-------------------------------------------------------------------------------------

PLAYER_TEAMS_QUERY: str = """\
query(
    $startDate: Date = "1900-01-01",
    $endDate: Date = "2500-01-01"
){
    teamsList(
        startDate: $startDate,
        endDate: $endDate,
        page: 0,
        representedByPlayer: 55
    ) {
        id
    }
}
"""

PLAYER_TEAMS_RESPONSE: dict = {
    "data": {
        "teamsList": [
            {"id": "7"},
            {"id": "4"},
        ]
    }
}