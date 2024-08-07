from flask import Blueprint, request, jsonify, current_app

user_routes = Blueprint('user_routes', __name__)

@user_routes.route("/user", methods=['GET', 'POST', 'PUT', 'DELETE'])
def user():
    method = request.method
    args = request.args
    request_body_data = request.get_json(silent=True) or {}
    user_controller = current_app.user_controller
    response = user_controller.user_response(method, args, request_body_data)
    return response