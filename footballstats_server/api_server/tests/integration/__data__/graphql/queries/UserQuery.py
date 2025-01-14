from api_server import constants


#-------------------------------------------------------------------------------------
# QUERY FOR USER FILTERING ATTRIBUTES
#-------------------------------------------------------------------------------------

USER_FILTERING_ATTRIBUTES_QUERY: str = """\
{
    userFilteringAttributes
}
"""

USER_FILTERING_ATTRIBUTES_RESPONSE: dict = {
    "data": {
        "userFilteringAttributes": list(constants.USER_FILTER_ATTRIBUTES.keys())
    }
}

#-------------------------------------------------------------------------------------
# QUERY FOR USER SORTING ATTRIBUTES
#-------------------------------------------------------------------------------------

USER_SORTING_ATTRIBUTES_QUERY: str = """\
{
    userSortingAttributes
}
"""

USER_SORTING_ATTRIBUTES_RESPONSE: dict = {
    "data": {
        "userSortingAttributes": list(constants.USER_SORT_ATTRIBUTES.keys())
    }
}

#-------------------------------------------------------------------------------------
# QUERY FOR USERS
#-------------------------------------------------------------------------------------

USERS_LIST_QUERY: str = """\
{
    usersList(page: 0, token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"){
        id,
        username
    }
}
"""

USERS_LIST_RESPONSE_FOR_OWNER: dict = {
    "data": {
        "usersList": [
            {"id": "3", "username": "Adam"},
            {"id": "2", "username": "Jerzy"},
        ]
    }
}

USERS_LIST_RESPONSE_FOR_NOT_OWNER: dict = {
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
                'usersList'
            ]
        }
    ],
    'data': {
        'usersList': None
    }
}

#-------------------------------------------------------------------------------------
# QUERY FOR USER PERMISSIONS
#-------------------------------------------------------------------------------------

USER_PERMISSIONS_QUERY: str = """\
{
    usersList(
        page: 0,
        token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
    ){
        id,
        username
        hasCreatePermission,
        hasModifyPermission,
        hasDeletePermission
    }
}
"""

USER_PERMISSIONS_RESPONSE: dict = {
    "data": {
        "usersList": [
            {
                "id": "3",
                "username": "Adam",
                "hasCreatePermission": False,
                "hasModifyPermission": False,
                "hasDeletePermission": True
            },
            {
                "id": "2",
                "username": "Jerzy",
                "hasCreatePermission": True,
                "hasModifyPermission": True,
                "hasDeletePermission": False
            }
        ]
    }
}