from app.dataaccess.database import Database
from app.entities.jason_web_token import JsonWebToken
from .user_manager import UserManager
from .use_case_response import MissedInfo, Success, UseCaseResponse


class LogIn:
    def __init__(self, db: Database, userdata: dict, jwt: JsonWebToken):
        self._db = db
        self._userdata = userdata
        self._jwt = jwt

    def execute(self) -> UseCaseResponse:
        if ('email' not in self._userdata
                or 'password' not in self._userdata):
            return UseCaseResponse(MissedInfo("SigUp missed some key-value"))

        email = self._userdata['email']
        password = self._userdata['password']

        user_manager = UserManager(self._db)
        resp = user_manager.get(email, password)

        if isinstance(resp.type, Success):
            return UseCaseResponse(resp.type, self._jwt.create_token(email, self._userdata))

        return resp
