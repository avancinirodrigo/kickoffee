from abc import abstractmethod
from app.entities.user import User
from .repository import Repository
from .session import Session


class UserRepo(Repository):
    @abstractmethod
    def add(self, user: User, session: Session):
        '''add User'''

    @abstractmethod
    def get(self, email: str, session: Session) -> User:
        '''get User'''

    @abstractmethod
    def delete(self, email: str, session: Session):
        '''delete from database'''

    @abstractmethod
    def update(self, email: str, user: User, session: Session):
        '''update in database'''
