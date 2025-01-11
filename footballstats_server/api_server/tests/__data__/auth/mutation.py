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