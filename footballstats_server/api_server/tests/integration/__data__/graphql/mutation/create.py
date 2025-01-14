#-------------------------------------------------------------------------------------
# CREATE TEAM
#-------------------------------------------------------------------------------------

CREATE_TEAM_REQUEST: str = """\
mutation{
    createTeam(
        input: {
            name: "Liverpool",
            countryOfOrigin: 10,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

CREATE_TEAM_RESPONSE_SUCCESS: dict = {
    "data": {
        "createTeam": {
            "errors": []
        }
    }
}

CREATE_TEAM_RESPONSE_NO_PERMISSIONS: dict = {
    'errors': [
        {
            'message': 'You do not have permission to perform this action',
            'locations': [
                {
                    'line': 2,
                    'column': 5
                }
            ], 
            'path': [
                'createTeam'
            ]
        }
    ], 
    'data': {
        'createTeam': None
    }
}

NOT_UNIQ_NAME_CREATE_TEAM_REQUEST: str = """\
mutation{
    createTeam(
        input: {
            name: "Argentyna",
            countryOfOrigin: 10,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_UNIQ_NAME_CREATE_TEAM_RESPONSE_SUCCESS: dict = {
    "data": {
        "createTeam": {
            "errors": [
                {
                    "field": "name",
                    "messages": [
                        "Team with this Name already exists."
                    ]
                }
            ]
        }
    }
}

NOT_EXISTING_COUNTRY_CREATE_TEAM_REQUEST: str = """\
mutation{
    createTeam(
        input: {
            name: "Liverpool",
            countryOfOrigin: -1,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_EXISTING_COUNTRY_CREATE_TEAM_RESPONSE_SUCCESS: dict = {
    "data": {
        "createTeam": {
            "errors": [
                {
                    "field": "countryOfOrigin",
                    "messages": [
                        "Select a valid choice. That choice is not one of the available choices."
                    ]
                }
            ]
        }
    }
}

#-------------------------------------------------------------------------------------
# CREATE MATCH
#-------------------------------------------------------------------------------------

CREATE_MATCH_REQUEST: str = """\
mutation{
    createMatch(
        input: {
            gameDate: "2018-05-26",
            leagueSeason: 2,
            homeTeam: 3,
            awayTeam: 4,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            homeTeamPlayers: "37=45.1 39=34.5",
            awayTeamPlayers: "38=1.5 40=90.0",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

CREATE_MATCH_RESPONSE_SUCCESS: dict = {
    "data": {
        "createMatch": {
            "errors": []
        }
    }
}

CREATE_MATCH_RESPONSE_NO_PERMISSIONS: dict = {
    'errors': [
        {
            'message': 'You do not have permission to perform this action',
            'locations': [
                {
                    'line': 2,
                    'column': 5
                }
            ], 
            'path': [
                'createMatch'
            ]
        }
    ], 
    'data': {
        'createMatch': None
    }
}

NOT_EXISTING_SEASON_CREATE_MATCH_REQUEST: str = """\
mutation{
    createMatch(
        input: {
            gameDate: "2018-05-26",
            leagueSeason: -1,
            homeTeam: 3,
            awayTeam: 4,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            homeTeamPlayers: "37=45.1 39=34.5",
            awayTeamPlayers: "38=1.5 40=90.0",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_EXISTING_SEASON_CREATE_MATCH_RESPONSE: dict = {
    "data": {
        "createMatch": {
            "errors": [
                {
                    "field": "leagueSeason",
                    "messages": [
                        "Select a valid choice. That choice is not one of the available choices."
                    ]
                }
            ]
        }
    }
}

NOT_EXISTING_HOME_TEAM_CREATE_MATCH_REQUEST: str = """\
mutation{
    createMatch(
        input: {
            gameDate: "2018-05-26",
            leagueSeason: 2,
            homeTeam: -1,
            awayTeam: 4,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            homeTeamPlayers: "37=45.1 39=34.5",
            awayTeamPlayers: "38=1.5 40=90.0",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_EXISTING_HOME_TEAM_CREATE_MATCH_RESPONSE: dict = {
    "data": {
        "createMatch": {
            "errors": [
                {
                    "field": "homeTeam",
                    "messages": [
                        "Team matching query does not exist."
                    ]
                }
            ]
        }
    }
}

NOT_EXISTING_AWAY_TEAM_CREATE_MATCH_REQUEST: str = """\
mutation{
    createMatch(
        input: {
            gameDate: "2018-05-26",
            leagueSeason: 2,
            homeTeam: 3,
            awayTeam: -1,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            homeTeamPlayers: "37=45.1 39=34.5",
            awayTeamPlayers: "38=1.5 40=90.0",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_EXISTING_AWAY_TEAM_CREATE_MATCH_RESPONSE: dict = {
    "data": {
        "createMatch": {
            "errors": [
                {
                    "field": "awayTeam",
                    "messages": [
                        "Team matching query does not exist."
                    ]
                }
            ]
        }
    }
}

NOT_EXISTING_AWAY_PLAYER_CREATE_MATCH_REQUEST: str = """\
mutation{
    createMatch(
        input: {
            gameDate: "2018-05-26",
            leagueSeason: 2,
            homeTeam: 3,
            awayTeam: 4,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            homeTeamPlayers: "37=45.1 39=34.5",
            awayTeamPlayers: "-1=1.5 40=90.0",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_EXISTING_AWAY_PLAYER_CREATE_MATCH_RESPONSE: dict = {
    "data": {
        "createMatch": {
            "errors": [
                {
                    "field": "awayTeamPlayers",
                    "messages": [
                        "Player matching query does not exist."
                    ]
                }
            ]
        }
    }
}

NOT_EXISTING_HOME_PLAYER_CREATE_MATCH_REQUEST: str = """\
mutation{
    createMatch(
        input: {
            gameDate: "2018-05-26",
            leagueSeason: 2,
            homeTeam: 3,
            awayTeam: 4,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            homeTeamPlayers: "-1=45.1 39=34.5",
            awayTeamPlayers: "38=1.5 40=90.0",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_EXISTING_HOME_PLAYER_CREATE_MATCH_RESPONSE: dict = {
    "data": {
        "createMatch": {
            "errors": [
                {
                    "field": "homeTeamPlayers",
                    "messages": [
                        "Player matching query does not exist."
                    ]
                }
            ]
        }
    }
}

PLAYER_HAVE_NO_MINUTES_PLAYED_CREATE_MATCH_REQUEST: str = """\
mutation{
    createMatch(
        input: {
            gameDate: "2018-05-26",
            leagueSeason: 2,
            homeTeam: 3,
            awayTeam: 4,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            homeTeamPlayers: "37 39=34.5",
            awayTeamPlayers: "38=1.5 40=90.0",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

PLAYER_HAVE_NO_MINUTES_PLAYED_CREATE_MATCH_RESPONSE: dict = {
    "data": {
        "createMatch": {
            "errors": [
                {
                    "field": "homeTeamPlayers",
                    "messages": [
                        "Player have no minutes played info!"
                    ]
                }
            ]
        }
    }
}

PLAYER_HAVE_NOT_NUMERIC_MINUTES_PLAYED_CREATE_MATCH_REQUEST: str = """\
mutation{
    createMatch(
        input: {
            gameDate: "2018-05-26",
            leagueSeason: 2,
            homeTeam: 3,
            awayTeam: 4,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            homeTeamPlayers: "37=a 39=34.5",
            awayTeamPlayers: "38=1.5 40=90.0",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

PLAYER_HAVE_NOT_NUMERIC_MINUTES_PLAYED_CREATE_MATCH_RESPONSE: dict = {
    "data": {
        "createMatch": {
            "errors": [
                {
                    "field": "homeTeamPlayers",
                    "messages": [
                        "Player's data contains non-numeric id or minutes played!"
                    ]
                }
            ]
        }
    }
}

#-------------------------------------------------------------------------------------
# CREATE SEASON
#-------------------------------------------------------------------------------------

CREATE_LEAGUE_SEASON_REQUEST: str = """\
mutation{
    createLeagueSeason(
        input: {
            name: "2017/2018",
            league: 2,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

CREATE_LEAGUE_SEASON_RESPONSE_SUCCESS: dict = {
    "data": {
        "createLeagueSeason": {
            "errors": []
        }
    }
}

CREATE_LEAGUE_SEASON_RESPONSE_NO_PERMISSIONS: dict = {
    'errors': [
        {
            'message': 'You do not have permission to perform this action',
            'locations': [
                {
                    'line': 2,
                    'column': 5
                }
            ], 
            'path': [
                'createLeagueSeason'
            ]
        }
    ], 
    'data': {
        'createLeagueSeason': None
    }
}

NAME_UNIQ_WITHIN_LEAGUE_ONLY_CREATE_LEAGUE_SEASON_REQUEST: str = """\
mutation{
    createLeagueSeason(
        input: {
            name: "1990",
            league: 2,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_UNIQ_NAME_WITHIN_LEAGUE_CREATE_LEAGUE_SEASON_REQUEST: str = """\
mutation{
    createLeagueSeason(
        input: {
            name: "1979",
            league: 2,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_UNIQ_NAME_WITHIN_LEAGUE_CREATE_LEAGUE_SEASON_RESPONSE: dict = {
    "data": {
        "createLeagueSeason": {
            "errors": [
                {
                    "field": "_All__",
                    "messages": [
                        "League season with this Name and League already exists."
                    ]
                }
            ]
        }
    }
}

NOTE_EXISTING_LEAGUE_CREATE_LEAGUE_SEASON_REQUEST: str = """\
mutation{
    createLeagueSeason(
        input: {
            name: "2017/2018",
            league: -1,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOTE_EXISTING_LEAGUE_CREATE_LEAGUE_SEASON_RESPONSE: dict = {
    "data": {
        "createLeagueSeason": {
            "errors": [
                {
                    "field": "league",
                    "messages": [
                        "Select a valid choice. That choice is not one of the available choices."
                    ]
                }
            ]
        }
    }
}

#-------------------------------------------------------------------------------------
# CREATE LEAGUE
#-------------------------------------------------------------------------------------

CREATE_LEAGUE_REQUEST: str = """\
mutation{
    createLeague(
        input: {
            name: "Champions League",
            countryOfOrigin: 109,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

CREATE_LEAGUE_RESPONSE_SUCCESS: dict = {
    "data": {
        "createLeague": {
            "errors": []
        }
    }
}

CREATE_LEAGUE_RESPONSE_NO_PERMISSIONS: dict = {
    'errors': [
        {
            'message': 'You do not have permission to perform this action',
            'locations': [
                {
                    'line': 2,
                    'column': 5
                }
            ], 
            'path': [
                'createLeague'
            ]
        }
    ], 
    'data': {
        'createLeague': None
    }
}

NOT_UNIQ_NAME_CREATE_LEAGUE_REQUEST: str = """\
mutation{
    createLeague(
        input: {
            name: "FIFA World Cup",
            countryOfOrigin: 109,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_UNIQ_NAME_CREATE_LEAGUE_RESPONSE: dict = {
    "data": {
        "createLeague": {
            "errors": [
                {
                    "field": "name",
                    "messages": [
                        "League with this Name already exists."
                    ]
                }
            ]
        }
    }
}

NOT_EXISTING_COUNTRY_CREATE_LEAGUE_REQUEST: str = """\
mutation{
    createLeague(
        input: {
            name: "Champions League",
            countryOfOrigin: -1,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_EXISTING_COUNTRY_CREATE_LEAGUE_RESPONSE: dict = {
    "data": {
        "createLeague": {
            "errors": [
                {
                    "field": "countryOfOrigin",
                    "messages": [
                        "Select a valid choice. That choice is not one of the available choices."
                    ]
                }
            ]
        }
    }
}

#-------------------------------------------------------------------------------------
# CREATE COUNTRY
#-------------------------------------------------------------------------------------

VALID_CREATE_COUNTRY_REQUEST: str = """\
mutation{
    createCountry(
        input: {
            name: "Europa",
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        }
    ){
        name,
        flagUrl,
        errors {
            field,
            messages
        }
    }
}
"""

VALID_CREATE_COUNTRY_RESPONSE_SUCCESS: dict = {
    "data": {
        "createCountry": {
            "name": "Europa",
            "flagUrl": None,
            "errors": []
        }
    }
}

VALID_CREATE_COUNTRY_RESPONSE_NO_PERMISSIONS: dict = {
    'errors': [
        {
            'message': 'You do not have permission to perform this action',
            'locations': [
                {
                    'line': 2,
                    'column': 5
                }
            ], 
            'path': [
                'createCountry'
            ]
        }
    ], 
    'data': {
        'createCountry': None
    }
}

CREATED_COUNTRY: tuple[dict] = (
    {"name": "Europa", "flag_url": None},
)

NOT_UNIQ_NAME_CREATE_COUNTRY_REQUEST: str = """\
mutation{
    createCountry(
        input: {
            name: "Włochy",
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        }
    ){
        name,
        flagUrl,
        errors {
            field,
            messages
        }
    }
}
"""

NOT_UNIQ_NAME_CREATE_COUNTRY_RESPONSE: dict = {
    "data": {
        "createCountry": {
            "name": "Włochy",
            "flagUrl": None,
            "errors": [
                {
                    "field": "name",
                    "messages": [
                        "Country with this Name already exists."
                    ]
                }
            ]
        }
    }
}