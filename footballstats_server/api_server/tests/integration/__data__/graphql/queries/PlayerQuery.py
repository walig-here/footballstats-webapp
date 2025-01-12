LIST_OF_PLAYERS_FROM_TEAM_QUERY_AND_MATCH__NO_FILTER: str = '''\
{
    playersList(
        startDate: "1900-01-01",
        endDate: "2500-01-01",
        page: 0,
        representingTeam: 8,
        playingInMatch: 6
    ) {
        id,
    }
}
'''
LIST_OF_PLAYERS_FROM_TEAM_AND_MATCH_RESPONSE__NO_FILTER: dict = {
    "data": {
        "playersList": [
            {"id": "250"},
            {"id": "236"},
            {"id": "246"},
            {"id": "237"},
            {"id": "242"},
            {"id": "252"},
            {"id": "249"},
            {"id": "245"},
            {"id": "239"},
            {"id": "233"},
            {"id": "241"},
            {"id": "234"},
            {"id": "248"},
            {"id": "254"},
            {"id": "251"},
            {"id": "244"},
            {"id": "235"},
            {"id": "240"},
            {"id": "243"},
            {"id": "247"},
            {"id": "238"},
            {"id": "253"},
        ]
    }
}


LIST_OF_PLAYERS_FROM_TEAM_QUERY__NO_FILTER: str = '''\
{
    playersList(
        startDate: "1900-01-01",
        endDate: "2500-01-01",
        page: 0,
        representingTeam: 4
    ) {
        id,
    }
}
'''
LIST_OF_PLAYERS_FROM_TEAM_RESPONSE__NO_FILTER: dict = {
    "data": {
        "playersList": [
            {"id": "61"},
            {"id": "68"},
            {"id": "57"},
            {"id": "62"},
            {"id": "59"},
            {"id": "58"},
            {"id": "60"},
            {"id": "72"},
            {"id": "55"},
            {"id": "65"},
            {"id": "70"},
            {"id": "67"},
            {"id": "64"},
            {"id": "63"},
            {"id": "66"},
            {"id": "56"},
            {"id": "69"},
            {"id": "71"},
        ]
    }
}


LIST_OF_PLAYERS_FROM_MATCH_QUERY__NO_FILTER: str = '''\
{
    playersList(
        startDate: "1900-01-01",
        endDate: "2500-01-01",
        page: 0,
        playingInMatch: 2
    ) {
        id
    }
}
'''
LIST_OF_PLAYERS_FROM_MATCH_RESPONSE__NO_FILTER: dict = {
    "data": {
        "playersList": [
            {"id": "61"},
            {"id": "68"},
            {"id": "57"},
            {"id": "62"},
            {"id": "37"},
            {"id": "59"},
            {"id": "42"},
            {"id": "58"},
            {"id": "60"},
            {"id": "49"},
            {"id": "46"},
            {"id": "41"},
            {"id": "48"},
            {"id": "72"},
            {"id": "55"},
            {"id": "65"},
            {"id": "70"},
            {"id": "52"},
            {"id": "51"},
            {"id": "40"},
            {"id": "67"},
            {"id": "39"},
            {"id": "43"},
            {"id": "44"},
            {"id": "64"},
        ]
    }
}

FULL_LIST_OF_PLAYERS_QUERY__COUNTRY_NOT_IN_SET_FILTER: str = '''\
{
    playersList(
        startDate: "1900-01-01",
        endDate: "2500-01-01",
        page: 2,
        textualFilters: [
            {
                targetAttributeName: "country_of_origin__name",
                filteringCriteria: TEXTUAL_NOT_IN_SET,
                filterParams: ["Brazylia", "Argentyna"]
            }
        ],
    ) {
        id
    }
}
'''
FULL_LIST_OF_PLAYERS_RESPONSE__COUNTRY_NOT_IN_SET_FILTER: dict = {
    "data": {
        "playersList": [
            {"id": "230"},
            {"id": "1184"},
            {"id": "903"},
            {"id": "1207"},
            {"id": "910"},
            {"id": "223"},
            {"id": "1200"},
            {"id": "1201"},
            {"id": "52"},
            {"id": "1191"},
            {"id": "911"},
            {"id": "1210"},
            {"id": "227"},
            {"id": "225"},
            {"id": "51"},
            {"id": "918"},
            {"id": "40"},
            {"id": "214"},
            {"id": "904"},
            {"id": "1196"},
            {"id": "1219"},
            {"id": "906"},
            {"id": "39"},
            {"id": "43"},
            {"id": "1209"},
        ]
    }
}


FULL_LIST_OF_PLAYERS_QUERY__COUNTRY_IN_SET_FILTER: str = '''\
{
    playersList(
        startDate: "1900-01-01",
        endDate: "2500-01-01",
        page: 1,
        textualFilters: [
            {
                targetAttributeName: "country_of_origin__name",
                filteringCriteria: TEXTUAL_IN_SET,
                filterParams: ["Brazylia", "Argentyna"]
            }
        ],
    ) {
        id
    }
}
'''
FULL_LIST_OF_PLAYERS_RESPONSE__COUNTRY_IN_SET_FILTER: dict = {
    "data": {
        "playersList": [
            {"id": "58"},
            {"id": "98"},
            {"id": "117"},
            {"id": "129"},
            {"id": "118"},
            {"id": "124"},
            {"id": "122"},
            {"id": "60"},
            {"id": "92"},
            {"id": "103"},
            {"id": "1182"},
            {"id": "1188"},
            {"id": "72"},
            {"id": "115"},
            {"id": "102"},
            {"id": "252"},
            {"id": "55"},
            {"id": "65"},
            {"id": "249"},
            {"id": "245"},
            {"id": "70"},
            {"id": "239"},
            {"id": "99"},
            {"id": "127"},
            {"id": "116"},
        ]
    }
}


FULL_LIST_OF_PLAYERS_QUERY__COUNTRY_FULL_TEXT_SEARCH_FILTER: str = '''\
{
    playersList(
        startDate: "1900-01-01",
        endDate: "2500-01-01",
        page: 0,
        textualFilters: [
            {
                targetAttributeName: "country_of_origin__name",
                filteringCriteria: TEXTUAL_FULL_TEXT_SEARCH,
                filterParams: ["B"]
            }
        ],
    ) {
        id
    }
}
'''
FULL_LIST_OF_PLAYERS_RESPONSE__COUNTRY_FULL_TEXT_SEARCH_FILTER: dict = {
    "data": {
        "playersList": [
            {"id": "123"},
            {"id": "128"},
            {"id": "236"},
            {"id": "119"},
            {"id": "246"},
            {"id": "114"},
            {"id": "237"},
            {"id": "242"},
            {"id": "1189"},
            {"id": "109"},
            {"id": "117"},
            {"id": "129"},
            {"id": "118"},
            {"id": "124"},
            {"id": "122"},
            {"id": "49"},
            {"id": "46"},
            {"id": "1188"},
            {"id": "115"},
            {"id": "252"},
            {"id": "249"},
            {"id": "245"},
            {"id": "239"},
            {"id": "127"},
            {"id": "116"},
        ]
    }
}


FULL_LIST_OF_PLAYERS_QUERY__UNFILTERED: str = """\
{
    playersList(
        startDate: "1900-01-01",
        endDate: "2500-01-01",
        page: 0,
    ) {
        name,
        surname
    }
}
"""
FULL_LIST_OF_PLAYERS_RESPONSE__UNFILTERED: dict = {
    "data": {
        "playersList": [
            {"name": "Claude", "surname": "Abbes"},
            {"name": "Ander Herrera", "surname": "Agüera"},
            {"name": "Jean Eudès", "surname": "Aholou"},
            {"name": "Ludovic", "surname": "Ajorque"},
            {"name": "José João", "surname": "Altafini"},
            {"name": "Hugo", "surname": "Alvez"},
            {"name": "José Carlos da Costa", "surname": "Araújo"},
            {"name": "Sven", "surname": "Axbom"},
            {"name": "Marcelo", "surname": "Bachino"},
            {"name": "Abel Eduardo", "surname": "Balbo"},
            {"name": "Acácio Cordeiro", "surname": "Barreto"},
            {"name": "José Horacio", "surname": "Basualdo"},
            {"name": "Sergio Daniel", "surname": "Batista"},
            {"name": "Edgardo", "surname": "Bauza"},
            {"name": "Jean-Ricner", "surname": "Bellegarde"},
            {"name": "Hideraldo Luis", "surname": "Bellini"},
            {"name": "Raymond", "surname": "Bellot"},
            {"name": "Ernst Orvar", "surname": "Bergmark"},
            {"name": "Bengt", "surname": "Berndtsson"},
            {"name": "Reino", "surname": "Borjesson"},
            {"name": "Ricardo Rogério de", "surname": "Brito"},
            {"name": "Stéphane", "surname": "Bruey"},
            {"name": "Jorge Luis", "surname": "Burruchaga"},
            {"name": "Anthony", "surname": "Caci"},
            {"name": "Zózimo Alves", "surname": "Calazães"},
        ]
    }
}


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