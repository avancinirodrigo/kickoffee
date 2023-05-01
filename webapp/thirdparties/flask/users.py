from flask import make_response, request
from webapp.controllers.signup_controller import SignUpController
from . import bp
from .dataaccess import db


@bp.route('/users', methods=['POST'])
def create_user():
    userdata = request.get_json() or {}
    ctrl = SignUpController(db, userdata)
    resp = ctrl.execute()
    return resp.data, resp.status_code
