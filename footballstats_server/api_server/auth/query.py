import uuid

import graphene
from graphql_jwt.decorators import superuser_required

from api_server.auth._registration_tokens import RegistrationTokenStorage


class AuthQuery(graphene.ObjectType):
    generate_registration_token = graphene.String(token=graphene.String(required=True))
    @superuser_required
    def resolve_generate_registration_token(self, info: graphene.ResolveInfo, **kwargs) -> str:
        """
        A GraphQL query. Generates a registration token and remembers it in system. 
        It also deletes from system all tokens older than their expiration date.
        
        This action cannot be invoked by a user that is not an owner.
        
        Params
        - `info` (`graphene.ResolveInfo`): GraphQL query context.
        
        Return
        - GraphQL response with `String` Field that contains generated token.
        """
        token_storage: RegistrationTokenStorage = RegistrationTokenStorage()
        token_storage.delete_expired_tokens()
        new_token: str = ""
        while True:
            new_token = uuid.uuid4()
            print(new_token)
            if token_storage.add_token(new_token):
                break
        return new_token
