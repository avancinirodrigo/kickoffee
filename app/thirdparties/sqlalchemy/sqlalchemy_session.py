from sqlalchemy import exc, orm
from app.dataaccess.session import Session
from app.dataaccess.exceptions import NotNullViolationException, UniqueViolationException


class SqlAlchemySession(Session):
    def __init__(self, session: orm.Session):
        self._session = session

    def commit(self):
        try:
            self._session.commit()
        except exc.IntegrityError as e:
            self._session.rollback()
            self._session.close()
            if 'NotNullViolation' in str(e):
                raise NotNullViolationException('Object violates not-null constraint')
            elif 'UniqueViolation' in str(e):
                raise UniqueViolationException('Object violates unique constraint')
            else:
                raise e

    def add(self, object):
        self._session.add(object)

    def delete(self, object):
        self._session.delete(object)

    def close(self):
        self._session.close()

    def query(self, object):
        return self._session.query(object)
