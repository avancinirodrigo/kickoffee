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
