class DictionaryObject:
    def __init__(self, context: dict):
        self.__dict__.update(context)


def get_graphql_context_with_owner_logged_in() -> dict:
    return DictionaryObject({
        "user": DictionaryObject({
            "is_authenticated": True,
            "is_superuser": True,
            "pk": 0
        }) 
    })


def get_graphql_context_with_admin_logged_in() -> dict:
    return DictionaryObject({
        "user": DictionaryObject({
            "is_authenticated": True,
            "is_superuser": False,
            "pk": 1
        })
    })


def get_graphql_context_with_viewer_user() -> dict:
    return DictionaryObject({
        "user": DictionaryObject({
            "is_authenticated": False,
            "is_superuser": False
        })
    })