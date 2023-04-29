from flask import jsonify
from flask.wrappers import Response
from app.ucs.use_case_response import (
    NotMatched,
    UseCaseResponse,
    Success,
    Created,
    MissedInfo,
    Duplicated,
    NotFound
)


class RestResponse:
    @staticmethod
    def Json(response: UseCaseResponse) -> Response:
        if isinstance(response.type, Created):
            return RestResponse.Created()
        elif isinstance(response.type, Success):
            return RestResponse.Ok()
        elif isinstance(response.type, MissedInfo):
            return RestResponse.BadRequest(response.type.message)
        elif isinstance(response.type, Duplicated):
            return RestResponse.Conflict(response.type.message)
        elif isinstance(response.type, NotFound):
            return RestResponse.NotFound(response.type.message)
        elif isinstance(response.type, NotMatched):
            return RestResponse.Unauthorized(response.type.message)
        return RestResponse.NotImplemented(f'Response not implemented yet {response.__dict__}')

    @staticmethod
    def Ok() -> Response:
        resp = Response()
        resp.status_code = 200
        return resp

    @staticmethod
    def Created() -> Response:
        resp = Response()
        resp.status_code = 201
        return resp

    @staticmethod
    def Failure(message: str, status: int) -> Response:
        resp = jsonify({'message': message})
        resp.status_code = status
        return resp

    @staticmethod
    def BadRequest(message: str) -> Response:
        return RestResponse.Failure(message, 400)

    @staticmethod
    def Conflict(message: str) -> Response:
        return RestResponse.Failure(message, 409)

    @staticmethod
    def NotImplemented(message: str) -> Response:
        return RestResponse.Failure(message, 501)

    @staticmethod
    def NotFound(message: str) -> Response:
        return RestResponse.Failure(message, 501)

    @staticmethod
    def Unauthorized(message: str) -> Response:
        return RestResponse.Failure(message, 401)
