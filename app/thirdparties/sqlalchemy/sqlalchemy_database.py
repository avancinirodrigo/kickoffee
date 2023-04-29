from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database, drop_database
from app.dataaccess.session import Session
from app.dataaccess.database import Database
from app.dataaccess.user_repo import UserRepo
from .sqlalchemy_session import SqlAlchemySession
from .sqlalchemy_base import Base
from .sqlalchemy_repo import UserOrmRepo


class SqlAlchemyDatabase(Database):
    def connect(self, url: str):
        self._engine = create_engine(url, pool_pre_ping=True)
        self._session = scoped_session(sessionmaker(bind=self._engine))
        self._url = url

    def session(self) -> Session:
        return SqlAlchemySession(self._session())

    def create(self, name: str = None, overwrite: bool = False):
        if database_exists(self._url):
            if overwrite:
                drop_database(self._url)
                create_database(self._url)
        else:
            create_database(self._url)

    def exists(self, name: str = None):
        return database_exists(self._url)

    def drop(self, name: str = None):
        drop_database(self._url)

    def create_all_tables(self):
        Base.metadata.create_all(self._engine)

    def create_all(self, overwrite: bool = False):
        self.create(overwrite)
        self.create_all_tables()

    def close(self):
        self._engine.dispose()

    def user_repo(self) -> UserRepo:
        return UserOrmRepo()
