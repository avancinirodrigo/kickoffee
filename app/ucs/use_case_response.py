from typing import Any


class Response:
    pass


class Success(Response):
    pass


class Created(Success):
    pass


class Failure(Response):
    def __init__(self, message: str):
        self.message = message


class NotFound(Failure):
    pass


class Duplicated(Failure):
    pass


class MissedInfo(Failure):
    pass


class NotMatched(Failure):
    pass


class UseCaseResponse:
    def __init__(self, type: Response, data: Any = None):
        self._data = data
        self._type = type

    @property
    def type(self) -> Response:
        return self._type

    @property
    def data(self) -> Any:
        return self._data
