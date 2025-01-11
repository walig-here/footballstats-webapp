import uuid
from datetime import datetime, timedelta
from typing import Literal

import graphene
from graphql_jwt.decorators import superuser_required

class _RegistrationTokenStorage:
    TOKEN_EXPIRATION_TIME_HOURS: int = 72
    _shared_state: dict[Literal["tokens"] | list[tuple[str, datetime]]] = {
        "tokens": []
    }

    def __init__(self):
        self.__dict__ = _RegistrationTokenStorage._shared_state

    def add_token(self, token: str) -> bool:
        """
        Tries to adds new token to storage.
        
        Params
        - `token` (`str`): New token.
        
        Return
        - `True`: When registration token has been properly added to storage.
        - `False`: When token couldn't have been added to storage because its not uniq.
        """
        if any([token == token_data[0] for token_data in self.tokens]):
            return False
        expiration_date: datetime = datetime.now() + timedelta(hours=self.TOKEN_EXPIRATION_TIME_HOURS)
        self.tokens.append((token, expiration_date))
        return True

    def delete_expired_tokens(self) -> int:
        """
        Deletes all tokens that expired.
        
        Return
        - `int`: Number of deleted tokens.
        """
        not_expired_tokens_list: list[tuple[str, datetime]] = []
        number_of_expired_tokens: int = 0
        for token_data in self.tokens:
            if token_data[1] > datetime.now():
                not_expired_tokens_list.append(token_data) 
            else:
                number_of_expired_tokens += 1
        self._shared_state["tokens"] = not_expired_tokens_list
        return number_of_expired_tokens

    @property
    def tokens(self) -> list[tuple[str, datetime]]:
        return self._shared_state["tokens"]


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
        token_storage: _RegistrationTokenStorage = _RegistrationTokenStorage()
        token_storage.delete_expired_tokens()
        new_token: str = ""
        while True:
            new_token = uuid.uuid4()
            print(new_token)
            if token_storage.add_token(new_token):
                break
        return new_token
