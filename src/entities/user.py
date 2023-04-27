class User:
    def __init__(self, name: str, email: str, password: str):
        self._name = name
        self._email = email
        self._password = password

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def password(self) -> str:
        return self._password

    @name.setter
    def name(self, name: str):
        self._name = name

    @email.setter
    def email(self, email: str):
        self._email = email

    @password.setter
    def password(self, password: str):
        self._password = password
