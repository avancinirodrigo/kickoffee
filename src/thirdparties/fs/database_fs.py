from dataaccess.session import Session
from dataaccess.database import Database
from dataaccess.user_repo import UserRepo
from thirdparties.fs.user_repo_fs import UserRepoFs
from .session_fs import SessionFs


class DatabaseFs(Database):
    def connect(self, url: str):
        '''connect'''

    def create(self, name: str):
        '''database create'''

    def drop(self, name: str):
        '''database drop'''

    def exists(self, name: str) -> bool:
        '''check if database exists'''

    def close(self):
        '''database close'''

    def session(self) -> Session:
        '''create session'''
        return SessionFs()

    def user_repo(self) -> UserRepo:
        '''create UserRepo'''
        return UserRepoFs()
