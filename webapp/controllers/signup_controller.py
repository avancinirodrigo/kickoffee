from app.ucs.use_case_response import Created, UseCaseResponse
from app.dataaccess.database import Database
from app.ucs.signup import SignUp
from .rest_response import RestResponse


class SignUpController:
    def __init__(self, db: Database, userdata: dict):
        self._db = db
        self._userdata = userdata

    def execute(self) -> RestResponse:
        uc = SignUp(self._db, self._userdata)
        resp = uc.execute()
        if isinstance(resp.type, Created):
            return RestResponse.Created()
