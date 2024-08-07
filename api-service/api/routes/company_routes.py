from flask import Blueprint, request, jsonify, current_app

company_routes = Blueprint('company_routes', __name__)

@company_routes.route("/companies", methods=['GET', 'POST', 'PUT', 'DELETE'])
def companies():
    method = request.method
    args = request.args
    request_body_data = request.get_json(silent=True) or {}
    company_controller = current_app.company_controller
    response = company_controller.companies_response(method, args, request_body_data)
    return response
