from sqlalchemy import Column, String, Integer
from entities.user import User
from .sqlalchemy_base import Base


class UserMetaclass(type(Base), type(User)):
    pass


class UserOrm(Base, User, metaclass=UserMetaclass):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def __init__(self, name: str, email: str, password: str):
        User.__init__(self, name, email, password)  # TODO: maybe there is a better way
        self.name = name
        self.email = email
        self.password = password
        print('---------------------------------------')
