from dataaccess.database import Database
from entities.user import User


class UserManager:
    def __init__(self, db: Database):
        self._db = db

    def create(self, name: str, email: str, password):
        user = User(name, email, password)
        session = self._db.session()
        user_repo = self._db.user_repo()
        user_repo.add(user, session)
        session.close()

    def get(self, email: str) -> User:
        session = self._db.session()
        user_repo = self._db.user_repo()
        user = user_repo.get(email, session)
        session.close()
        return user

    def delete(self, email: str):
        session = self._db.session()
        user_repo = self._db.user_repo()
        user_repo.delete(email, session)
        session.close()

    def update(self, email: str, userUp: User):
        session = self._db.session()
        user_repo = self._db.user_repo()
        user_repo.update(email, userUp, session)
        session.close
