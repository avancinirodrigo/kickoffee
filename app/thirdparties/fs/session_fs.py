from typing import Any
from app.dataaccess.session import Session


class SessionFs(Session):
    def add(self, obj: Any):
        '''add object'''

    def close(self):
        '''close a session'''

    def commit(self):
        '''commit session'''
