from app.dataaccess.database import Database
from .user_manager import UserManager
from .use_case_response import MissedInfo, UseCaseResponse


class SignUp:
    def __init__(self, db: Database, userdata: dict):
        self._db = db
        self._userdata = userdata

    def execute(self) -> UseCaseResponse:
        if ('name' not in self._userdata
                or 'email' not in self._userdata
                or 'password' not in self._userdata):
            return UseCaseResponse(MissedInfo("SigUp missed some key-value"))

        name = self._userdata['name']
        email = self._userdata['email']
        password = self._userdata['password']

        user_manager = UserManager(self._db)
        return user_manager.create(name, email, password)
