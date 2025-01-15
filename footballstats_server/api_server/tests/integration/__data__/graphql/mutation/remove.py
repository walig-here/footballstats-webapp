#-------------------------------------------------------------------------------------
# REMOVE PLAYER FROM MATCH
#-------------------------------------------------------------------------------------

REMOVE_PLAYER_FROM_MATCH_QUERY: str = """\
mutation{
    removePlayerFromMatch(
        input: {
            player: 55,
            match: 2,
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

REMOVE_PLAYER_FROM_MATCH_RESPONSE: dict = {
    "data": {
        "removePlayerFromMatch": {
            "errors": []
        }
    }
}

#-------------------------------------------------------------------------------------
# REMOVE PLAYER
#-------------------------------------------------------------------------------------

REMOVE_PLAYER_QUERY: str = """\
mutation{
    removePlayer(
        input: {
            playerId: 38,
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

REMOVE_PLAYER_RESPONSE: dict = {
    "data": {
        "removePlayer": {
            "errors": []
        }
    }
}

#-------------------------------------------------------------------------------------
# REMOVE MATCH
#-------------------------------------------------------------------------------------

REMOVE_MATCH_QUERY: str = """\
mutation{
    removeMatch(
        input: {
            matchId: 6,
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

REMOVE_MATCH_RESPONSE: dict = {
    "data": {
        "removeMatch": {
            "errors": []
        }
    }
}

#-------------------------------------------------------------------------------------
# REMOVE TEAM
#-------------------------------------------------------------------------------------

REMOVE_TEAM_QUERY: str = """\
mutation{
    removeTeam(
        input: {
            teamId: 3,
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

REMOVE_TEAM_RESPONSE: dict = {
    "data": {
        "removeTeam": {
            "errors": []
        }
    }
}

#-------------------------------------------------------------------------------------
# REMOVE PLAYER FROM TEAM
#-------------------------------------------------------------------------------------

REMOVE_PLAYER_FROM_TEAM_QUERY: str = """\
mutation{
    removePlayerFromTeam(
        input: {
            playerId: 55,
            teamId: 4,
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

REMOVE_PLAYER_FROM_TEAM_RESPONSE: dict = {
    "data": {
        "removePlayerFromTeam": {
            "errors": []
        }
    }
}

#-------------------------------------------------------------------------------------
# REMOVE MATCH EVENT
#-------------------------------------------------------------------------------------

REMOVE_EVENT_QUERY: str = """\
mutation{
    removeEventFromMatch(
        input: {
            eventId: 925, 
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ98",
        }
    ) {
        errors{
            field,
            messages
        }
    }
}
"""

REMOVE_EVENT_RESPONSE: dict = {
    "data": {
        "removeEventFromMatch": {
            "errors": []
        }
    }
}