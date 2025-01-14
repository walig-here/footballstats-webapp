from api_server import constants


PLAYER_SORTING_ATTRIBUTES_REQUEST: str = """\
{
    playerSortingAttributes
}
"""
PLAYER_SORTING_ATTRIBUTES_RESPONSE: dict = {
    "data": {
        "playerSortingAttributes": list(constants.PLAYER_SORT_ATTRIBUTES.keys())
    }
}

PLAYER_FILTERING_ATTRIBUTES_REQUEST: str = """\
{
    playerFilteringAttributes
}
"""
PLAYER_FILTERING_ATTRIBUTES_RESPONSE: dict = {
    "data": {
        "playerFilteringAttributes": list(constants.PLAYER_FILTER_ATTRIBUTES.keys())
    }
}