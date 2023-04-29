from app.ucs.use_case_response import MissedInfo, Response
from app.dataaccess.database import Database
from app.ucs.user_manager import UserManager


class LogInController:
    def __init__(self, db: Database, userdata: dict):
        self._db = db
        self._userdata = userdata

    def execute(self) -> Response:
        if ('email' not in self._userdata
                or 'password' not in self._userdata):
            return MissedInfo("SigUp missed some key-value")
        email = self._userdata['email']
        password = self._userdata['password']
        uc = UserManager(self._db)
        return uc.get(email, password)
