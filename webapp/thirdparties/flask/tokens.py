from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.ucs.use_case_response import Success
from webapp.controllers.login_controller import LogInController
from . import bp
from .dataaccess import db
from .rest_response import RestResponse


@bp.route('/tokens', methods=['POST'])
def create_token():
    userdata = request.get_json() or {}
    uc = LogInController(db, userdata)
    out = uc.execute()
    if isinstance(out.type, Success):
        user = out.data
        access_token = create_access_token(identity=user.email,
                                           additional_claims=userdata)
        return jsonify({"token": access_token}), 200
    return RestResponse.Json(out)
