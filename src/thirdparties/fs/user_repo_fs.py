from dataaccess.user_repo import UserRepo
from entities.user import User
from dataaccess.session import Session


class UserRepoFs(UserRepo):
    _users = {}

    def add(self, user: User, session: Session):
        self._users[user.email] = user

    def get(self, email: str, session: Session) -> User:
        return self._users[email]

    def delete(self, email: str, session: Session):
        '''TODO'''

    def update(self, email: str, user: User, session: Session):
        '''TODO'''
