"""
Authentication and authorization
"""
import graphene
import graphql_jwt

from django.contrib.auth.models import User

from api_server import constants
from api_server.auth._registration_tokens import RegistrationTokenStorage


ERROR_USERNAME_NOT_UNIQ: str = "Provided username is not uniq!"
ERROR_USERNAME_BLANK: str = "Provided username is empty!"
ERROR_REGISTRATION_TOKEN_INVALID: str = "Provided registration token is invalid!"
ERROR_REGISTRATION_TOKEN_EXPIRED: str = "Provided registration token is expired!"


def _is_username_claimed(username: str) -> bool:
    """
    Checks if given username is already claimed by some user.
    
    Params
    - `username` (`str`): Username.
    
    Return
    - `True`: Username is claimed.
    - `False`: Username is not claimed.
    """
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        return False
    return True


class _RegisterUser(graphene.Mutation):
    """
    Registers new administrator's account with given username and password.
    
    Params
    - `username` (`str`): New admin's username. Must be uniq and not blank!
    - `password` (`str`): New admin's password. Must be not blank.
    - `registration_token`: Registration token provided by new admin.
    
    Return
    - Object that contains following fields:
        - `ok`: Information wether registration succeeded.
        - `message`: Additional information about errors that occurred during registration process.
    """
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        registration_token = graphene.String(required=True)

    ok = graphene.Boolean()
    messages = graphene.List(graphene.String)

    def mutate(root, info: graphene.ResolveInfo, username: str, password: str, registration_token: str):
        messages: list[str] = []
        
        username_not_blank: bool = username != ""
        username_uniq: bool = not _is_username_claimed(username) if username_not_blank else True
        if not username_not_blank:
            messages.append(ERROR_USERNAME_BLANK)
        if not username_uniq:
            messages.append(ERROR_USERNAME_NOT_UNIQ)
        username_ok: bool = all([username_uniq, username_not_blank])

        token_valid: bool = False
        token_not_expired: bool = False
        if username_ok:
            token_valid, token_not_expired = RegistrationTokenStorage().use_token(registration_token)
            if not token_valid:
                messages.append(ERROR_REGISTRATION_TOKEN_INVALID)
            if not token_not_expired:
                messages.append(ERROR_REGISTRATION_TOKEN_EXPIRED)

        ok: bool = all([username_uniq, username_not_blank, token_valid, token_not_expired])
        if ok:
            new_user: User = User(username=username)
            new_user.set_password(password)
            new_user.save()
        
        return _RegisterUser(
            ok=ok, 
            messages=messages
        )


class _GrantPermission(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        permission = graphene.Enum.from_enum(constants.PermissionType)()

    ok = graphene.Boolean()
    messages = graphene.List(graphene.String)

    def mutate(root, info: graphene.ResolveInfo, username: str, permission: constants.PermissionType):
        raise NotImplementedError


class _RevokePermission(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        permission = graphene.Enum.from_enum(constants.PermissionType)()

    ok = graphene.Boolean()
    messages = graphene.List(graphene.String)

    def mutate(root, info: graphene.ResolveInfo, username: str, permission: constants.PermissionType):
        raise NotImplementedError


class _RemoveUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)

    ok = graphene.Boolean()
    messages = graphene.List(graphene.String)

    def mutate(root, info: graphene.ResolveInfo, username: str):
        raise NotImplementedError


class AuthMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    register_user = _RegisterUser.Field()
    grant_permission = _GrantPermission.Field()
    revoke_permission = _RevokePermission.Field()
    remove_user = _RemoveUser.Field()
