GENERATE_REGISTRATION_TOKEN_REQUEST: str = """\
query{
    generateRegistrationToken(token: "jwt")
}
"""
GENERATE_REGISTRATION_TOKEN_OWNER_RESPONSE: dict = {
    "data": {
        "generateRegistrationToken": "92f3dcfc-6457-4248-8a29-18b164a2a29a"
    }
}
GENERATE_REGISTRATION_NOT_OWNER_RESPONSE: dict = {
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
                'generateRegistrationToken'
            ]
        }
    ],
    'data': {
        'generateRegistrationToken': None
    }
}