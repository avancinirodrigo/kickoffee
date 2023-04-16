from typing import Any, List

from dataaccess.session import Session


class SessionFs(Session):
    def add(self, obj: Any):
        '''add object'''

    def close(self):
        '''close a session'''

    def fetchone(self) -> Any:
        '''fetch one row of a table'''

    def fetchall(self) -> List[Any]:
        '''fetch all rows of a table'''
