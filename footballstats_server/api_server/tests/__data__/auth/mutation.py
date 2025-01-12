GRANT_PERMISSION_REQUEST__VALID_INPUTS: str = """\
mutation{
    grantPermission(
        permission: DELETE,
        username: "Jerzy",
        token: "44641fdcb4fd7d71d4ff86e84bb7826d747b7bef"
    ) {
        ok,
        messages
    }
}
"""
GRANT_PERMISSION_RESPONSE__VALID_INPUTS: dict = {
    "data": {
        "grantPermission": {
            "ok": True,
            "messages": []
        }
    }
}

GRANT_PERMISSION_REQUEST__ALREADY_GIVEN_PERMISSION: str = """\
mutation{
    grantPermission(
        permission: CREATE,
        username: "Jerzy",
        token: "44641fdcb4fd7d71d4ff86e84bb7826d747b7bef"
    ) {
        ok,
        messages
    }
}
"""
GRANT_PERMISSION_RESPONSE__ALREADY_GIVEN_PERMISSION: dict = {
    "data": {
        "grantPermission": {
            "ok": True,
            "messages": []
        }
    }
}

GRANT_PERMISSION_REQUEST__NOT_EXISTING_PERMISSION: str = """\
mutation{
    grantPermission(
        permission: NOT_EXISTING_PERMISSION,
        username: "Jerzy",
        token: "44641fdcb4fd7d71d4ff86e84bb7826d747b7bef"
    ) {
        ok,
        messages
    }
}
"""
GRANT_PERMISSION_RESPONSE__NOT_EXISTING_PERMISSION: dict = {
    "data": None,
    'errors': [
        {
            'locations': [
                {'column': 21, 'line': 3}
            ],
            'message': "Value 'NOT_EXISTING_PERMISSION' does not exist in 'PermissionType' enum."
        }
    ]
}

GRANT_PERMISSION_REQUEST__NOT_EXISTING_USER: str = """\
mutation{
    grantPermission(
        permission: CREATE,
        username: "Not-exisitng-user",
        token: "44641fdcb4fd7d71d4ff86e84bb7826d747b7bef"
    ) {
        ok,
        messages
    }
}
"""
GRANT_PERMISSION_RESPONSE__NOT_EXISTING_USER: dict = {
    "data": {
        "grantPermission": {
            "ok": False,
            "messages": ["Given user doesn't exist!"]
        }
    }
}

GRANT_PERMISSION_REQUEST__TARGETS_OWNER: str = """\
mutation{
    grantPermission(
        permission: CREATE,
        username: "owner",
        token: "44641fdcb4fd7d71d4ff86e84bb7826d747b7bef"
    ) {
        ok,
        messages
    }
}
"""
GRANT_PERMISSION_RESPONSE__TARGETS_OWNER: dict = {
    "data": {
        "grantPermission": {
            "ok": False,
            "messages": ["Can't change owner's permissions!"]
        }
    }
}

GRANT_PERMISSION_RESPONSE__NOT_OWNER: dict = {
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
                'grantPermission'
            ]
        }
    ],
    'data': {
        'grantPermission': None
    }
}

CREATORS_AND_MODIFIERS_ADMIN_ACTION_TYPES: list[str] = [
    "api_server.add_match",
    "api_server.add_matchevent",
    "api_server.add_player",
    "api_server.add_team",
    "api_server.change_country",
    "api_server.change_country_league",
    "api_server.change_country_player",
    "api_server.change_country_team",
    "api_server.change_league",
    "api_server.change_league_season",
    "api_server.change_match",
    "api_server.change_matchevent",
    "api_server.change_player",
    "api_server.change_playerinmatch",
    "api_server.change_team",
]

ALL_POSSIBLE_ADMIN_ACTION_TYPES: list[str] = [
    "api_server.add_match",
    "api_server.add_matchevent",
    "api_server.add_player",
    "api_server.add_team",
    "api_server.change_country",
    "api_server.change_country_league",
    "api_server.change_country_player",
    "api_server.change_country_team",
    "api_server.change_league",
    "api_server.change_league_season",
    "api_server.change_match",
    "api_server.change_matchevent",
    "api_server.change_player",
    "api_server.change_playerinmatch",
    "api_server.change_team",
    "api_server.delete_match",
    "api_server.delete_matchevent",
    "api_server.delete_player",
    "api_server.delete_playerinmatch",
    "api_server.delete_team",
    "api_server.delete_team_from_match",
]

# ========= RegisterUser ==========

REGISTER_USER_REQUEST_WITH_VALID_CREDENTIALS: str = """\
mutation{
    registerUser(
        username: "NewUser",
        password: "dnHx6J6icQDRE7V",
        registrationToken: "92f3dcfc-6457-4248-8a29-18b164a2a29a"
    ) {
        ok,
        messages
    }
}
"""
REGISTER_USER_RESPONSE_WITH_VALID_CREDENTIALS: str = {
    "data": {
        "registerUser": {
            "ok": True,
            "messages": []
        }
    }
}

REGISTER_USER_REQUEST_NOT_UNIQ_USERNAME: str = """\
mutation{
    registerUser(
        username: "owner",
        password: "dnHx6J6icQDRE7V",
        registrationToken: "92f3dcfc-6457-4248-8a29-18b164a2a29a"
    ) {
        ok,
        messages
    }
}
"""
REGISTER_USER_RESPONSE_NOT_UNIQ_USERNAME: str = {
    "data": {
        "registerUser": {
            "ok": False,
            "messages": [
                "Provided username is not uniq!"
            ]
        }
    }
}

REGISTER_USER_REQUEST_BLANK_USERNAME: str = """\
mutation{
    registerUser(
        username: "",
        password: "dnHx6J6icQDRE7V",
        registrationToken: "92f3dcfc-6457-4248-8a29-18b164a2a29a"
    ) {
        ok,
        messages
    }
}
"""
REGISTER_USER_RESPONSE_BLANK_USERNAME: str = {
    "data": {
        "registerUser": {
            "ok": False,
            "messages": [
                "Provided username is empty!"
            ]
        }
    }
}

REGISTER_USER_REQUEST_INVALID_TOKEN: str = """\
mutation{
    registerUser(
        username: "NewUser",
        password: "dnHx6J6icQDRE7V",
        registrationToken: "invalid-token"
    ) {
        ok,
        messages
    }
}
"""
REGISTER_USER_RESPONSE_INVALID_TOKEN: str = {
    "data": {
        "registerUser": {
            "ok": False,
            "messages": [
                "Provided registration token is invalid!"
            ]
        }
    }
}

REGISTER_USER_REQUEST_EXPIRED_TOKEN: str = """\
mutation{
    registerUser(
        username: "NewUser",
        password: "dnHx6J6icQDRE7V",
        registrationToken: "expired-token"
    ) {
        ok,
        messages
    }
}
"""
REGISTER_USER_RESPONSE_EXPIRED_TOKEN: str = {
    "data": {
        "registerUser": {
            "ok": False,
            "messages": [
                "Provided registration token is expired!"
            ]
        }
    }
}

REGISTER_USER_REQUEST_INVALID_TOKEN_NOT_UNIQ_USERNAME: str = """\
mutation{
    registerUser(
        username: "owner",
        password: "dnHx6J6icQDRE7V",
        registrationToken: "invalid-token"
    ) {
        ok,
        messages
    }
}
"""
REGISTER_USER_INVALID_TOKEN_NOT_UNIQ_USERNAME: str = {
    "data": {
        "registerUser": {
            "ok": False,
            "messages": [
                "Provided username is not uniq!",
            ]
        }
    }
}