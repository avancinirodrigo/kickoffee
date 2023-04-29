from abc import ABC, abstractmethod
from typing import Any


class Session(ABC):

    @abstractmethod
    def add(self, obj: Any):
        '''add object'''

    @abstractmethod
    def close(self):
        '''abstract close a session'''

    @abstractmethod
    def commit(self):
        '''abstract commit session'''
