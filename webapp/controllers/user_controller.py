from app.ucs.use_case_response import Created, Success
from app.dataaccess.database import Database
from app.ucs.signup import SignUp
from app.ucs.login import LogIn
from app.entities.jason_web_token import JsonWebToken
from .rest_response import RestResponse


class UserController:
    def __init__(self, db: Database, userdata: dict):
        self._db = db
        self._userdata = userdata

    def signup(self) -> RestResponse:
        uc = SignUp(self._db, self._userdata)
        resp = uc.execute()
        if isinstance(resp.type, Created):
            return RestResponse.Created()

    def login(self, jwt: JsonWebToken) -> RestResponse:
        uc = LogIn(self._db, self._userdata, jwt)
        resp = uc.execute()
        if isinstance(resp.type, Success):
            return RestResponse.Ok(resp.data)
