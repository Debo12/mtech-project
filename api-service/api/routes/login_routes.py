from flask import Blueprint, request, jsonify, current_app

login_routes = Blueprint('login_routes', __name__)

@login_routes.route("/login", methods=['POST'])
def login():
    request_body_data = request.get_json(silent=True) or {}
    login_controller = current_app.login_controller
    response = login_controller.login_response(request_body_data)
    return response