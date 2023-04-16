from kickoffee.src.dataaccess.database import Database
from kickoffee.src.entities.user import User


class UserManager:
    def __init__(self, db: Database):
        self._db = db

    def create(self, name: str, email: str, password):
        user = User(name, email, password)
        session = Database.session()
        user_repo = Database.user_repo()
        user_repo.add(user, session)
        session.close()