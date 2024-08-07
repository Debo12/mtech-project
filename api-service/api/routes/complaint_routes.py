from flask import Blueprint, request, jsonify, current_app

complaint_routes = Blueprint('complaint_routes', __name__)

@complaint_routes.route("/complaints", methods=['GET', 'POST', 'PUT', 'DELETE'])
def complaints():
    method = request.method
    args = request.args
    request_body_data = request.get_json(silent=True) or {}
    complaint_controller = current_app.complaint_controller
    response = complaint_controller.complaint_response(method, args, request_body_data)
    return response
