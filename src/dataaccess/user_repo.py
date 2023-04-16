from entities.user import User
from .repository import Repository
from .session import Session


class UserRepo(Repository):
    def add(self, user: User, session: Session):
        '''add User'''

    def get(self, email: str, session: Session) -> User:
        '''get User'''
