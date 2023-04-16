from abc import ABC, abstractmethod
from typing import Any
from .session import Session


class Repository(ABC):
    @abstractmethod
    def add(self, obj: Any, session: Session):
        '''add in database'''

    @abstractmethod
    def get(self, obj: Any, session: Session):
        '''get from database'''
