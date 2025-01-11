from datetime import datetime, timedelta
from typing import Literal


TOKEN_EXPIRATION_TIME_HOURS: int = 72


class RegistrationTokenStorage:
    _shared_state: dict[Literal["tokens"] | list[tuple[str, datetime]]] = {
        "tokens": []
    }

    def __init__(self):
        self.__dict__ = RegistrationTokenStorage._shared_state

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
        expiration_date: datetime = datetime.now() + timedelta(hours=TOKEN_EXPIRATION_TIME_HOURS)
        self.tokens.append((token, expiration_date))
        return True

    def use_token(self, token: str) -> tuple[bool, bool]:
        """
        Checks if given token is not valid and not expired. Token would be removed from the storage 
        only when it's valid.
        
        Params
        - `token`: Registration token.
        
        Return
        - `tuple[bool, bool]`:
            - [0]: Informs wether token was valid.
            - [1]: Informs wether token was not expired.
        """
        for token_data in self.tokens:
            if token_data[0] != token:
                continue
            if token_data[1] < datetime.now():
                return (True, False)
            self.tokens.clear()
            return (True, True)
        return (False, False)

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