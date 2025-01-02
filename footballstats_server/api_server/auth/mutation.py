"""
Authentication and authorization
"""
import graphene
import graphql_jwt

from api_server.graphql._types.models import UserType
from api_server import constants


class _RegisterUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        registration_token = graphene.String(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    def mutate(root, info: graphene.ResolveInfo, username: str, password: str, registration_token: str):
        raise NotImplementedError


class _GrantPermission(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        permission = graphene.Enum.from_enum(constants.PermissionType)()

    ok = graphene.Boolean()
    message = graphene.String()

    def mutate(root, info: graphene.ResolveInfo, username: str, permission: constants.PermissionType):
        raise NotImplementedError


class _RevokePermission(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        permission = graphene.Enum.from_enum(constants.PermissionType)()

    ok = graphene.Boolean()
    message = graphene.String()

    def mutate(root, info: graphene.ResolveInfo, username: str, permission: constants.PermissionType):
        raise NotImplementedError


class _RemoveUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

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
