from flask import request, jsonify
from app.thirdparties.flask.jwt_flask import JwtFlask
from webapp.controllers.user_controller import UserController
from . import bp
from .dataaccess import db


@bp.route('/tokens', methods=['POST'])
def create_token():
    userdata = request.get_json() or {}
    ctrl = UserController(db, userdata)
    out = ctrl.login(JwtFlask())
    return jsonify({'token': out.data}), out.status_code
