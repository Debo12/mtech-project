from flask import Blueprint, request, jsonify, current_app

user_activity_routes = Blueprint('user_activity_routes', __name__)

@user_activity_routes.route("/user_activity", methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_activity():
    method = request.method
    args = request.args
    request_body_data = request.get_json(silent=True) or {}
    user_activity_controller = current_app.user_activity_controller
    response = user_activity_controller.user_activity_response(method, args, request_body_data)
    return response
