from flask import request
from webapp.controllers.user_controller import UserController
from . import bp
from .dataaccess import db


@bp.route('/users', methods=['POST'])
def create_user():
    userdata = request.get_json() or {}
    ctrl = UserController(db, userdata)
    resp = ctrl.signup()
    return resp.data, resp.status_code
