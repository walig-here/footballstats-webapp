from datetime import datetime
from typing import Literal

import graphene

class _RegistryTokenStorage:
    _shared_state: dict[Literal["tokens"] | list[tuple[str, datetime]]] = {
        "tokens": []
    }
    
    def __init__(self):
        self.__dict__ = _RegistryTokenStorage._shared_state
    
    @property
    def tokens(self) -> list[tuple[str, datetime]]:
        return self._shared_state["tokens"]


class AuthQuery(graphene.ObjectType):
    generate_registration_token = graphene.String()
    def resolve_generate_registration_token(self, info: graphene.ResolveInfo) -> str:
        raise NotImplementedError
