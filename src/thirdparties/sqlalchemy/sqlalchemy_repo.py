from dataaccess.user_repo import UserRepo
from dataaccess.session import Session
from entities.user import User
from .sqlalchemy_orm import UserOrm


class UserOrmRepo(UserRepo):
    def add(self, user: User, session: Session):
        session.add(UserOrm(user.name, user.email, user.password))
        session.commit()

    def get(self, email: str, session: Session) -> User:
        return session.query(UserOrm).filter(UserOrm.email == email).first()

    def delete(self, email: str, session: Session):
        user = self.get(email, session)
        session.delete(user)
        session.commit()

    def update(self, email: str, userUp: User, session: Session):
        userOrm = self.get(email, session)
        if (userOrm.name != userUp.name
                or userOrm.email != userUp.email
                or userOrm.password != userUp.password):
            userOrm.name = userUp.name
            userOrm.email = userUp.email
            userOrm.password = userUp.password
            session.commit
