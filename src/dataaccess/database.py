from abc import ABC, abstractmethod
from .session import Session


class Database(ABC):
    @abstractmethod
    def connect(self, url: str):
        '''abstract connect'''

    @abstractmethod
    def create(self, name: str):
        '''abstract database create'''

    @abstractmethod
    def drop(self, name: str):
        '''abstract database drop'''

    @abstractmethod
    def exists(self, name: str) -> bool:
        '''abstract check if database exists'''

    @abstractmethod
    def close(self):
        '''abstract database close'''

    @abstractmethod
    def session(self) -> Session:
        '''abstract create session'''
