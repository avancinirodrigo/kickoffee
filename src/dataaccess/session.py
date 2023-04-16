from abc import ABC, abstractmethod
from typing import Any, List


class Session(ABC):

    @abstractmethod
    def execute(self, query: str):
        '''abstract execute a query'''

    @abstractmethod
    def close(self):
        '''abstract close a session'''

    @abstractmethod
    def fetchone(self) -> Any:
        '''abstract fetch one row of a table'''

    @abstractmethod
    def fetchall(self) -> List[Any]:
        '''abstract fetch all rows of a table'''