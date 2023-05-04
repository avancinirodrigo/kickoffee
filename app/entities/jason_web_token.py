from abc import ABC, abstractmethod


class JsonWebToken(ABC):

    @abstractmethod
    def create_token(self, identity: str, additional_claims: dict) -> str:
        '''abstract create jwt'''
