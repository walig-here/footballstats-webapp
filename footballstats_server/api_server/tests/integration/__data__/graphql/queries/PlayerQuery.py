PLAYER_QUERY__OWN_DATA: str = """\
{
    player(id: 55){
        id,
        name,
        surname,
        nickname,
        profilePhotoUrl,
    }
}
"""
PLAYER_QUERY_RESPONSE__OWN_DATA: dict = {
    "data": {
        "player": {
            "id": "55",
            "name": "Diego Armando",
            "surname": "Maradona",
            "nickname": None,
            "profilePhotoUrl": None
        }
    }
}


PLAYER_QUERY__COUNTRY_OF_ORIGIN_DATA: str = """\
{
    player(id: 55){
        countryOfOrigin {
            id,
            name,
            flagUrl,
        }
    }
}
"""
PLAYER_QUERY_RESPONSE__COUNTRY_OF_ORIGIN_DATA: dict = {
    "data": {
        "player": {
            "countryOfOrigin": {
                "id": "10",
                "name": "Argentyna",
                "flagUrl": None
            }
        }
    }
}


PLAYER_QUERY__ADMIN_ACTIONS: str = """\
{
    player(id: 55){
        adminActions {
            adminAction {
                actionType {
                    name
                },
                user {
                username,
                isSuperuser,
                username
                }
            }
        }
    },
}
"""
PLAYER_QUERY_RESPONSE__ADMIN_ACTIONS: dict = {
    "data": {
        "player": {
            "adminActions": []
        }
    }
}


PLAYER_QUERY__SUM_FOR_SUCCESSFUL_PASS_IN_MATCH: str = """\
{
    player(id: 55){
        calculateMetric(
            startDate: "1900-01-01", 
            endDate: "2500-01-01",
            match: 2,
            team: -2,
            metric: {
                metricType: SUM,
                targetMatchEvent: SUCCESSFUL_PASS,
                metricParams: []
            }
        )
    }
}
"""
PLAYER_QUERY_RESPONSE__SUM_FOR_SUCCESSFUL_PASS_IN_MATCH: dict = {
    "data": {
        "player": {
            "calculateMetric": 28.0
        }
    }
}


PLAYER_QUERY__AVERAGE_FOR_SUCCESSFUL_PASS_IN_TEAM_MATCHES: str = """\
{
    player(id: 55){
        calculateMetric(
            startDate: "1900-01-01", 
            endDate: "2500-01-01",
            match: -1,
            team: 4,
            metric: {
                metricType: AVERAGE,
                targetMatchEvent: SUCCESSFUL_PASS,
                metricParams: []
            }
        )
	}
}
"""
PLAYER_QUERY_RESPONSE__AVERAGE_FOR_SUCCESSFUL_PASS_IN_TEAM_MATCHES: dict = {
    "data": {
        "player": {
            "calculateMetric": 28.0 / 90.0
        }
    }
}


PLAYER_QUERY__ODDS_FOR_SUCCESSFUL_PASS_IN_ALL_MATCHES: str = """\
{
    player(id: 55){
        calculateMetric(
            startDate: "1900-01-01", 
            endDate: "2500-01-01",
            match: -1,
            team: -2,
            metric: {
                metricType: ODDS_FOR,
                targetMatchEvent: SUCCESSFUL_PASS,
                metricParams: []
            }
        )
	}
}
"""
PLAYER_QUERY_RESPONSE__ODDS_FOR_SUCCESSFUL_PASS_IN_ALL_MATCHES: dict = {
    "data": {
        "player": {
            "calculateMetric": 100.0
        }
    }
}


PLAYER_QUERY__ODDS_FOR_MORE_THAN_SUCCESSFUL_PASS_IN_ALL_MATCHES: str = """\
{
    player(id: 55){
        calculateMetric(
            startDate: "1900-01-01", 
            endDate: "2500-01-01",
            match: -1,
            team: -2,
            metric: {
                metricType: ODDS_FOR_MORE_THAN,
                targetMatchEvent: SUCCESSFUL_PASS,
                metricParams: ["25"]
            }
        )
    }
}
"""
PLAYER_QUERY_RESPONSE__ODDS_FOR_MORE_THAN_SUCCESSFUL_PASS_IN_ALL_MATCHES: dict = {
    "data": {
        "player": {
            "calculateMetric": 50.0
        }
    }
}


PLAYER_QUERY__MINUTES_UNTIL_SUCCESSFUL_PASS_IN_MATCH: str = """\
{
    player(id: 55){
        calculateMetric(
            startDate: "1900-01-01", 
            endDate: "2500-01-01",
            match: 2,
            team: -2,
            metric: {
                metricType: MINUTES_UNTIL,
                targetMatchEvent: SUCCESSFUL_PASS,
                metricParams: []
            }
        )
    }
}
"""
PLAYER_QUERY_RESPONSE__MINUTES_UNTIL_SUCCESSFUL_PASS_IN_MATCH: dict = {
    "data": {
        "player": {
            "calculateMetric": 2.683
        }
    }
}


PLAYER_QUERY__ODDS_IN_TIME_RANGE_SUCCESSFUL_PASS_IN_TEAM_MATCHES: str = """\
{
    player(id: 55){
        calculateMetric(
            startDate: "1900-01-01", 
            endDate: "2500-01-01",
            match: -1
            team: 4
            metric: {
                metricType: ODDS_IN_TIME_RANGE,
                targetMatchEvent: SUCCESSFUL_PASS,
                metricParams: ["15", "55"]
            }
        )
    }
}
"""
PLAYER_QUERY_RESPONSE__ODDS_IN_TIME_RANGE_SUCCESSFUL_PASS_IN_TEAM_MATCHES: dict = {
    "data": {
        "player": {
            "calculateMetric": 11.0 / 28.0 * 100
        }
    }
}


PLAYER_QUERY__METRIC_HISTORY: str = """\
{
    player(id: 55){
        metricHistory(
            startDate: "1900-01-01",
            endDate: "2500-01-01",
            metric: {
                metricType: SUM,
                targetMatchEvent: SUCCESSFUL_PASS,
                metricParams: []
            }
        ) {
            value,
            time
        }
	}
}
"""
PLAYER_QUERY_RESPONSE__METRIC_HISTORY: dict = {
    "data": {
        "player": {
            "metricHistory": [
                {
                    "value": 0,
                    "time": "1900-01-01",
                },
                {
                    "value": 28,
                    "time": "1979-09-07",
                },
                {
                    "value": 52,
                    "time": "1990-06-24",
                },
                {
                    "value": 52,
                    "time": "2500-01-01",
                },
            ]
        }
    }
}