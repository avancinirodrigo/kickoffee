from app.dataaccess.database import Database
from app.entities.user import User
from .use_case_response import NotFound, NotMatched, Created, Success, UseCaseResponse


class UserManager:
    def __init__(self, db: Database):
        self._db = db

    def create(self, name: str, email: str, password) -> UseCaseResponse:
        user = User(name, email, password)
        session = self._db.session()
        user_repo = self._db.user_repo()
        user_repo.add(user, session)
        session.close()
        return UseCaseResponse(Created())

    def get(self, email: str, password: str) -> UseCaseResponse:
        session = self._db.session()
        user_repo = self._db.user_repo()
        user = user_repo.get(email, session)
        session.close()
        if user is None:
            return UseCaseResponse(NotFound('User not found'))
        if user.password == password:
            return UseCaseResponse(Success(), user)
        else:
            return UseCaseResponse(NotMatched('Wrong password'))

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
