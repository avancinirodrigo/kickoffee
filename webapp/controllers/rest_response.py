from __future__ import annotations


class RestResponse:
    def __init__(self, status_code: int, data: dict = ""):
        self._data = data
        self._status_code = status_code

    @property
    def data(self) -> dict:
        return self._data

    @property
    def status_code(self) -> int:
        return self._status_code

    @staticmethod
    def Ok(data: dict) -> RestResponse:
        return RestResponse(200, data)

    @staticmethod
    def Created() -> RestResponse:
        return RestResponse(201)

    # @staticmethod
    # def Failure(message: str, status: int) -> Response:
    #     resp = jsonify({'message': message})
    #     resp.status_code = status
    #     return resp

    # @staticmethod
    # def BadRequest(message: str) -> Response:
    #     return RestResponse.Failure(message, 400)

    # @staticmethod
    # def Conflict(message: str) -> Response:
    #     return RestResponse.Failure(message, 409)

    # @staticmethod
    # def NotImplemented(message: str) -> Response:
    #     return RestResponse.Failure(message, 501)

    # @staticmethod
    # def NotFound(message: str) -> Response:
    #     return RestResponse.Failure(message, 501)

    # @staticmethod
    # def Unauthorized(message: str) -> Response:
    #     return RestResponse.Failure(message, 401)
