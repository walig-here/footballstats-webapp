#-------------------------------------------------------------------------------------
# MODIFY PLAYER
#-------------------------------------------------------------------------------------

MODIFY_PLAYER_MATCH_CONTRIBUTION_REQUEST: str = """\
mutation{
    modifyPlayerMatchContribution(
        input: {
            playerId: 37, 
            matchId: 2,
            team: 4,
            minutesPlayed: 45,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

MODIFY_PLAYER_MATCH_CONTRIBUTION_RESPONSE: dict = {
    "data": {
        "modifyPlayerMatchContribution": {
            "errors": []
        }
    }
}

TEAM_NOT_PLAYING_IN_MATCH_MODIFY_PLAYER_MATCH_CONTRIBUTION_REQUEST: str = """\
mutation{
    modifyPlayerMatchContribution(
        input: {
            playerId: 37, 
            matchId: 2,
            team: 7,
            minutesPlayed: 45,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

TEAM_NOT_PLAYING_IN_MATCH_MODIFY_PLAYER_MATCH_CONTRIBUTION_RESPONSE: dict = {
    "data": {
        "modifyPlayerMatchContribution": {
            "errors": [
                {
                    "field": "team",
                    "messages": [
                        "Team is not taking part in that match!"
                    ]
                }
            ]
        }
    }
}

PLAYER_IS_TEAM_LAST_PLAYER_MODIFY_PLAYER_MATCH_CONTRIBUTION_REQUEST: str = """\
mutation{
    modifyPlayerMatchContribution(
        input: {
            playerId: 37, 
            matchId: 2,
            team: 4,
            minutesPlayed: 45,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

PLAYER_IS_TEAM_LAST_PLAYER_MODIFY_PLAYER_MATCH_CONTRIBUTION_RESPONSE: dict = {
    "data": {
        "modifyPlayerMatchContribution": {
            "errors": [
                {
                    "field": "All",
                    "messages": [
                        "Can't reassign team's last player!"
                    ]
                }
            ]
        }
    }
}

#-------------------------------------------------------------------------------------
# MODIFY PLAYER
#-------------------------------------------------------------------------------------

MODIFY_PLAYER_REQUEST: str = """\
mutation{
    modifyPlayer(
        input: {
            playerId: 37, 
            name: "Jan",
            surname: "Kowalski",
            nickname: "Kowal",
            profilePhotoUrl: "https://placehold.co/600x400",
            countryOfOrigin: 9,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

MODIFY_PLAYER_RESPONSE: dict = {
    "data": {
        "modifyPlayer": {
            "errors": []
        }
    }
}

NOT_UNIQ_FULLNAME_MODIFY_PLAYER_REQUEST: str = """\
mutation{
    modifyPlayer(
        input: {
            playerId: 37, 
            name: "Aleksandr",
            surname: "Polukarov",
            nickname: "Kowal",
            profilePhotoUrl: "https://placehold.co/600x400",
            countryOfOrigin: 9,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_UNIQ_FULLNAME_MODIFY_PLAYER_RESPONSE: dict = {
    "data": {
        "modifyPlayer": {
            "errors": [
                {
                    "field": "_All__",
                    "messages": [
                        "Player with this Name and Surname already exists."
                    ]
                }
            ]
        }
    }
}

COUNTRY_NOT_EXIST_MODIFY_PLAYER_REQUEST: str = """\
mutation{
    modifyPlayer(
        input: {
            playerId: 37, 
            name: "Jan",
            surname: "Kowalski",
            nickname: "Kowal",
            profilePhotoUrl: "https://placehold.co/600x400",
            countryOfOrigin: -1,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

COUNTRY_NOT_EXIST_MODIFY_PLAYER_RESPONSE: dict = {
    "data": {
        "modifyPlayer": {
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
# MODIFY MATCH
#-------------------------------------------------------------------------------------

MODIFY_MATCH_REQUEST: str = """\
mutation{
    modifyMatch(
        input: {
            matchId: 2, 
            gameDate: "1800-01-01",
            leagueSeason: 4,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

MODIFY_MATCH_RESPONSE: dict = {
    "data": {
        "modifyMatch": {
            "errors": []
        }
    }
}

NOT_EXISTING_SEASON_MODIFY_MATCH_REQUEST: str = """\
mutation{
    modifyMatch(
        input: {
            matchId: 2, 
            gameDate: "1800-01-01",
            leagueSeason: -1,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_EXISTING_SEASON_MODIFY_MATCH_RESPONSE: dict = {
    "data": {
        "modifyMatch": {
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

#-------------------------------------------------------------------------------------
# MODIFY TEAM
#-------------------------------------------------------------------------------------

MODIFY_TEAM_REQUEST: str = """\
mutation{
    modifyTeam(
        input: {
            teamId: 3, 
            name: "ZSRR",
            logoUrl: "https://placehold.co/600x400",
            countryOfOrigin: 10,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

MODIFY_TEAM_RESPONSE: dict = {
    "data": {
        "modifyTeam": {
            "errors": []
        }
    }
}

NOT_UNIQ_NAME_MODIFY_TEAM_REQUEST: str = """\
mutation{
    modifyTeam(
        input: {
            teamId: 3, 
            name: "Francja",
            logoUrl: "https://placehold.co/600x400",
            countryOfOrigin: 10,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_UNIQ_NAME_MODIFY_TEAM_RESPONSE: dict = {
    "data": {
        "modifyTeam": {
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

NOT_EXISTING_COUNTRY_MODIFY_TEAM_REQUEST: str = """\
mutation{
    modifyTeam(
        input: {
            teamId: 3, 
            name: "ZSRR",
            logoUrl: "https://placehold.co/600x400",
            countryOfOrigin: -1,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_EXISTING_COUNTRY_MODIFY_TEAM_RESPONSE: dict = {
    "data": {
        "modifyTeam": {
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
# MODIFY COUNTRY
#-------------------------------------------------------------------------------------

MODIFY_COUNTRY_REQUEST: str = """\
mutation{
    modifyCountry(
        input: {
            countryId: 10, 
            name: "Kanada",
            flagUrl: "https://placehold.co/600x400"
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

MODIFY_COUNTRY_RESPONSE: dict = {
    "data": {
        "modifyCountry": {
            "errors": []
        }
    }
}

NOT_UNIQ_NAME_MODIFY_COUNTRY_REQUEST: str = """\
mutation{
    modifyCountry(
        input: {
            countryId: 10, 
            name: "Armenia",
            flagUrl: "https://placehold.co/600x400"
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_UNIQ_NAME_MODIFY_COUNTRY_RESPONSE: dict = {
    "data": {
        "modifyCountry": {
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

#-------------------------------------------------------------------------------------
# MODIFY LEAGUE
#-------------------------------------------------------------------------------------

MODIFY_LEAGUE_REQUEST: str = """\
mutation{
    modifyLeague(
        input: {
            leagueId: 4, 
            name: "Nowa Liga",
            countryOfOrigin: 8,
            logoUrl: "https://placehold.co/600x400",
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

MODIFY_LEAGUE_RESPONSE: dict = {
    "data": {
        "modifyLeague": {
            "errors": []
        }
    }
}

NOT_UNIQ_NAME_MODIFY_LEAGUE_REQUEST: str = """\
mutation{
    modifyLeague(
        input: {
            leagueId: 4, 
            name: "FIFA World Cup",
            countryOfOrigin: 8,
            logoUrl: "https://placehold.co/600x400",
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NOT_UNIQ_NAME_MODIFY_LEAGUE_RESPONSE: dict = {
    "data": {
        "modifyLeague": {
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

COUNTRY_NOT_EXIST_MODIFY_LEAGUE_REQUEST: str = """\
mutation{
    modifyLeague(
        input: {
            leagueId: 4, 
            name: "Nowa Liga",
            countryOfOrigin: -1,
            logoUrl: "https://placehold.co/600x400",
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

COUNTRY_NOT_EXIST_MODIFY_LEAGUE_RESPONSE: dict = {
    "data": {
        "modifyLeague": {
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
# MODIFY SEASON
#-------------------------------------------------------------------------------------

MODIFY_SEASON_REQUEST: str = """\
mutation{
    modifyLeagueSeason(
        input: {
            leagueSeasonId: 4, 
            name: "1950",
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

MODIFY_SEASON_RESPONSE: dict = {
    "data": {
        "modifyLeagueSeason": {
            "errors": []
        }
    }
}

MODIFY_SEASON_RESPONSE_NO_PERMISSIONS: dict = {
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
                'modifyLeagueSeason'
            ]
        }
    ], 
    'data': {
        'modifyLeagueSeason': None
    }
}

NAME_IS_NOT_UNIQ_MODIFY_SEASON_REQUEST: str = """\
mutation{
    modifyLeagueSeason(
        input: {
            leagueSeasonId: 4, 
            name: "1958",
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

NAME_IS_NOT_UNIQ_MODIFY_SEASON_RESPONSE: dict = {
    "data": {
        "modifyLeagueSeason": {
            "errors": [
                {
                    "field": "name",
                    "messages": [
                        "Season name is not uniq within league!"
                    ]
                }
            ]
        }
    }
}

#-------------------------------------------------------------------------------------
# MODIFY EVENT
#-------------------------------------------------------------------------------------

MODIFY_MATCH_EVENT_REQUEST: str = """\
mutation{
    modifyEventFromMatch(
        input: {
            eventId: 925, 
            player: 40,
            occurrenceMinute: 5,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

MODIFY_MATCH_EVENT_RESPONSE: dict = {
    "data": {
        "modifyEventFromMatch": {
            "errors": []
        }
    }
}

MODIFY_MATCH_EVENT_RESPONSE_NO_PERMISSIONS: dict = {
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
                'modifyEventFromMatch'
            ]
        }
    ], 
    'data': {
        'modifyEventFromMatch': None
    }
}

PLAYER_NOT_TAKING_PART_IN_MATCH_MODIFY_MATCH_EVENT_REQUEST: str = """\
mutation{
    modifyEventFromMatch(
        input: {
            eventId: 925, 
            player: 90,
            occurrenceMinute: 5,
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

PLAYER_NOT_TAKING_PART_IN_MATCH_MODIFY_MATCH_EVENT_RESPONSE: dict = {
    "data": {
        "modifyEventFromMatch": {
            "errors": [
                {
                    "field": "player",
                    "messages": [
                        "Player is not taking part in this match!"
                    ]
                }
            ]
        }
    }
}