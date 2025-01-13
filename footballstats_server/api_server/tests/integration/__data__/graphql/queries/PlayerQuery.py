#-------------------------------------------------------------------------------------
# PLAYERS QUERIED + CONJUNCTION OF METRIC FILTERS
#-------------------------------------------------------------------------------------

LIST_OF_PLAYERS_QUERY__CONJUNCTION_OF_METRIC_FILTERS: str = '''\
query(
    $startDate: Date = "1900-01-01",
    $endDate: Date = "2200-01-01",
){
    playersList(
        startDate: $startDate,
        endDate: $endDate,
        page:0,
        metricFilters: [
            {
                metric: {
                    metricType: SUM,
                    targetMatchEvent: DEFENSE,
                    metricParams: []
                },
                filteringCriteria: NUMERIC_EQUALS,
                filterParams: [3]
            },
            {
                metric: {
                    metricType: MINUTES_UNTIL,
                    targetMatchEvent: DEFENSE,
                    metricParams: []
                },
                filteringCriteria: NUMERIC_IN_CLOSED_RANGE,
                filterParams: [20, 30]
            }
        ]
    ) {
        id
    }
}
'''
LIST_OF_PLAYERS_RESPONSE__CONJUNCTION_OF_METRIC_FILTERS: dict = {
    "data": {
        "playersList": [
            {"id": "1218"}
        ]
    }
}

#-------------------------------------------------------------------------------------
# PLAYERS QUERIED + NOT IN CLOSED RANGE FOR MINUTES UNTIL YELLOW CARD
#-------------------------------------------------------------------------------------

LIST_OF_PLAYERS_QUERY__FILTER_MINUTES_UNTIL_YELLOW_CARD_NOT_IN_CLOSED_RANGE: str = '''\
query(
    $startDate: Date = "1900-01-01",
    $endDate: Date = "2200-01-01",
){
    playersList(
        startDate: $startDate,
        endDate: $endDate,
        page: 0,
        metricFilters: [
            {
                metric: {
                    metricType: MINUTES_UNTIL,
                    targetMatchEvent: YELLOW_CARD,
                    metricParams: []
                },
                filteringCriteria: NUMERIC_NOT_IN_CLOSED_RANGE,
                filterParams: [10, 50]
            }
        ]
    ) {
        id
    }
}
'''
LIST_OF_PLAYERS_RESPONSE__FILTER_MINUTES_UNTIL_YELLOW_CARD_NOT_IN_CLOSED_RANGE: dict = {
    "data": {
        "playersList": [
            {"id": "1218"},
            {"id": "1194"},
            {"id": "122"},
            {"id": "103"},
            {"id": "1188"},
            {"id": "1183"},
            {"id": "1206"},
        ]
    }
}

#-------------------------------------------------------------------------------------
# PLAYERS QUERIED + IN CLOSED RANGE FILTER FOR ODDS FOR GOAL
#-------------------------------------------------------------------------------------

LIST_OF_PLAYERS_QUERY__FILTER_ODDS_FOR_GOAL_IN_CLOSED_RANGE: str = '''\
{
    playersList(
        startDate: "1900-01-01",
        endDate: "2200-01-01",
        page: 0,
        metricFilters: [
            {
                metric: {
                metricType: ODDS_FOR,
                targetMatchEvent: GOAL,
                metricParams: []
                },
                filteringCriteria: NUMERIC_IN_CLOSED_RANGE,
                filterParams: [40, 60]
            }
        ]
    ) {
        id
    }
}
'''
LIST_OF_PLAYERS_RESPONSE__FILTER_ODDS_FOR_GOAL_IN_CLOSED_RANGE: dict = {
    "data": {
        "playersList": [
            {"id": "55"},
            {"id": "254"},
            {"id": "253"},
        ]
    }
}

#-------------------------------------------------------------------------------------
# PLAYERS QUERIED + EQUALS SUM SHOT NOT ON TARGET
#-------------------------------------------------------------------------------------

LIST_OF_PLAYERS_QUERY__FILTER_SUM_SHOT_NOT_ON_TARGET_EQUALS: str = '''\
{
    playersList(
        startDate: "1900-01-01",
        endDate: "2200-01-01",
        page: 0,
        metricFilters: [
            {
                metric: {
                    metricType: SUM,
                    targetMatchEvent: SHOT_NOT_ON_TARGET,
                    metricParams: []
                },
                filteringCriteria: NUMERIC_EQUALS,
                filterParams: [2]
            }
        ]
    ) {
        id,
    }
}
'''
LIST_OF_PLAYERS_RESPONSE__FILTER_SUM_SHOT_NOT_ON_TARGET_EQUALS: dict = {
    "data": {
        "playersList": [
            {"id": "61"},
            {"id": "57"},
            {"id": "1188"},
            {"id": "115"},
            {"id": "39"},
            {"id": "43"},
            {"id": "219"},
            {"id": "101"},
        ]
    }
}

#-------------------------------------------------------------------------------------
# PLAYERS QUERIED + NOT IN SET FILTER FOR LEAGUE NAME
#-------------------------------------------------------------------------------------

LIST_OF_PLAYERS_QUERY__NOT_IN_SET_LEAGUE_NAME: str = '''\
{
    playersList(
        startDate: "1900-01-01",
        endDate: "2200-01-01",
        page: 0,
        textualFilters: [
            {
                targetAttributeName: "playerinmatch__match__league_season__league__name",
                filteringCriteria: TEXTUAL_NOT_IN_SET,
                filterParams: ["FIFA World Cup"]
            }
        ]
    ) {
        id,
    }
}
'''
LIST_OF_PLAYERS_RESPONSE__NOT_IN_SET_LEAGUE_NAME: dict = {
    "data": {
        "playersList": [
            {"id": "1187"},
            {"id": "1202"},
            {"id": "1212"},
            {"id": "61"},
            {"id": "68"},
            {"id": "1218"},
            {"id": "1216"},
            {"id": "62"},
            {"id": "37"},
            {"id": "1189"},
            {"id": "1192"},
            {"id": "1217"},
            {"id": "1221"},
            {"id": "59"},
            {"id": "1204"},
            {"id": "1194"},
            {"id": "42"},
            {"id": "1198"},
            {"id": "58"},
            {"id": "1214"},
            {"id": "1193"},
            {"id": "1211"},
            {"id": "60"},
            {"id": "1190"},
            {"id": "49"},
        ]
    }
}

#-------------------------------------------------------------------------------------
# PLAYERS QUERIED + IN SET FILTER FOR LEAGUE NAME
#-------------------------------------------------------------------------------------

LIST_OF_PLAYERS_QUERY__IN_SET_LEAGUE_NAME: str = '''\
{
    playersList(
        startDate: "1900-01-01",
        endDate: "2200-01-01",
        page: 3,
        textualFilters: [
            {
                targetAttributeName: "playerinmatch__match__league_season__league__name",
                filteringCriteria: TEXTUAL_IN_SET,
                filterParams: ["Ligue 1", "FIFA World Cup"]
            }
        ]
    ) {
        id,
    }
}
'''
LIST_OF_PLAYERS_RESPONSE__IN_SET_LEAGUE_NAME: dict = {
    "data": {
        "playersList": [
            {"id": "1206"},
            {"id": "230"},
            {"id": "102"},
            {"id": "1184"},
            {"id": "252"},
            {"id": "55"},
            {"id": "903"},
            {"id": "1207"},
            {"id": "910"},
            {"id": "249"},
            {"id": "245"},
            {"id": "223"},
            {"id": "1200"},
            {"id": "1201"},
            {"id": "239"},
            {"id": "99"},
            {"id": "1191"},
            {"id": "911"},
            {"id": "127"},
            {"id": "116"},
            {"id": "233"},
            {"id": "241"},
            {"id": "234"},
            {"id": "1210"},
            {"id": "227"},
        ]
    }
}

#-------------------------------------------------------------------------------------
# PLAYERS QUERIED + FULL TEXT SEARCH FILTER FOR LEAGUE NAME
#-------------------------------------------------------------------------------------

LIST_OF_PLAYERS_QUERY__FULL_TEXT_SEARCH_LEAGUE_NAME: str = '''\
{
    playersList(
        startDate: "1900-01-01",
        endDate: "2200-01-01",
        page: 1,
        textualFilters: [
            {
                targetAttributeName: "playerinmatch__match__league_season__league__name",
                filteringCriteria: TEXTUAL_FULL_TEXT_SEARCH,
                filterParams: ["Li"]
            }
        ]
    ) {
        id
    }
}
'''
LIST_OF_PLAYERS_RESPONSE__FULL_TEXT_SEARCH_LEAGUE_NAME: dict = {
    "data": {
        "playersList": [
            {"id": "1200"},
            {"id": "1201"},
            {"id": "1191"},
            {"id": "1210"},
            {"id": "1196"},
            {"id": "1219"},
            {"id": "1209"},
            {"id": "1220"},
            {"id": "1215"},
            {"id": "1199"},
            {"id": "1213"},
            {"id": "1208"},
            {"id": "1197"},
            {"id": "1185"},
            {"id": "1186"},
        ]
    }
}

#-------------------------------------------------------------------------------------
# PLAYERS QUERIED + DATE RANGE LIMITED
#-------------------------------------------------------------------------------------

LIST_OF_PLAYERS_QUERY__LIMITED_DATE_RANGE: str = '''\
{
    playersList(
        startDate: "1960-01-01",
        endDate: "2000-01-01",
        page: 0,
    ) {
        id,
    }
}
'''
LIST_OF_PLAYERS_RESPONSE__LIMITED_DATE_RANGE: dict = {
    "data": {
        "playersList": [
            {"id": "61"},
            {"id": "123"},
            {"id": "68"},
            {"id": "96"},
            {"id": "128"},
            {"id": "100"},
            {"id": "90"},
            {"id": "105"},
            {"id": "119"},
            {"id": "91"},
            {"id": "57"},
            {"id": "114"},
            {"id": "107"},
            {"id": "97"},
            {"id": "62"},
            {"id": "37"},
            {"id": "106"},
            {"id": "109"},
            {"id": "108"},
            {"id": "59"},
            {"id": "42"},
            {"id": "58"},
            {"id": "98"},
            {"id": "117"},
            {"id": "129"},
        ]
    }
}

#-------------------------------------------------------------------------------------
# PLAYERS QUERIED FOR TEAM & MATCH + NO ADDITIONAL FILTERS
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYERS QUERIED FOR TEAM + NO ADDITIONAL FILTERS
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYERS QUERIED FOR MATCH + NO ADDITIONAL FILTERS
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYERS QUERIED WIH FULL TEXT SEARCH FILTER FOR COUNTRY
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYERS QUERIED WIH IN SET FILTER FOR COUNTRY
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYERS QUERIED WIH NOT IN SET FILTER FOR COUNTRY
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# ALL PLAYERS QUERIED
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYER QUERY OWN DATA
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYER QUERY COUNTRY OF ORIGIN
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYER QUERY ADMIN ACTION
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYER QUERY FOR SUM METRIC - SUCCESSFUL PASS
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYER QUERY FOR AVERAGE METRIC - SUCCESSFUL PASS
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYER QUERY FOR ODDS FOR METRIC - PASS IN MATCH
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYER QUERY FOR ODDS FOR MORE THAN METRIC - PASS IN MATCH
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYER QUERY FOR MINUTES UNTIL METRIC - PASS IN MATCH
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYER QUERY FOR ODDS IN TIME RANGE METRIC - PASS IN MATCH
#-------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------
# PLAYER QUERY FOR METRIC HISTORY - SUM - SUCCESSFUL PASS
#-------------------------------------------------------------------------------------

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