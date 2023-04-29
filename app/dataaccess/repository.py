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

    @abstractmethod
    def delete(self, obj: Any, session: Session):
        '''delete from database'''

    @abstractmethod
    def update(self, obj: Any, objUp: Any, session: Session):
        '''update in database'''
