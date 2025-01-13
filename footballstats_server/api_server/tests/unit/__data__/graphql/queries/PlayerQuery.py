#-----------------------------------------------------------------
# QUERY FOR NOT EXISTING PLAYER
#-----------------------------------------------------------------

PLAYER_QUERY__PLAYER_NOT_EXIST: str = """\
{
    player(id: 1222){
        id
    }
}
"""
PLAYER_RESPONSE__PLAYER_NOT_EXIST: dict = {
    "errors": [
        {
            "message": "Player matching query does not exist.",
            "locations": [
                {
                "line": 2,
                "column": 5
                }
            ],
            "path": [
                "player"
            ]
        }
    ],
    "data": {
        "player": None
    }
}

#-----------------------------------------------------------------
# QUERIES LIST OF PLAYERS INVALID NUMBERS FULL TEX SEARCH PARAMS
#-----------------------------------------------------------------

LIST_OF_PLAYERS_QUERY__FULL_TEXT_FILTER_TOO_MANY_PARAMETERS: str = """\
{
    playersList(
        startDate: "1900-01-01",
        endDate: "2200-01-01",
        page: 0,
        textualFilters: [
            {
                targetAttributeName: "name",
                filteringCriteria: TEXTUAL_FULL_TEXT_SEARCH,
                filterParams: ["A", "B"]
            }
        ]
    ) {
        id
    }
}
"""
LIST_OF_PLAYERS_QUERY__FULL_TEXT_FILTER_TOO_LITTLE_PARAMETERS: str = """\
{
    playersList(
        startDate: "1900-01-01",
        endDate: "2200-01-01",
        page: 0,
        textualFilters: [
            {
                targetAttributeName: "name",
                filteringCriteria: TEXTUAL_FULL_TEXT_SEARCH,
                filterParams: []
            }
        ]
    ) {
        id
    }
}
"""
LIST_OF_PLAYERS_RESPONSE__FULL_TEXT_FILTER_INVALID_NUMBER_OF_PARAMETERS: dict = {
    'errors': [
        {
            'message': 'Invalid number of parameters passed for filter!', 
            'locations': [
                {
                    'line': 2, 
                    'column': 5
                    }
                ], 
            'path': [
                'playersList'
            ]
        }
    ], 
    'data': {
        'playersList': None
    }
}