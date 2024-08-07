from flask import Blueprint, request, jsonify, current_app

model_prediction_routes = Blueprint('model_prediction_routes', __name__)

@model_prediction_routes.route("/model_predictions", methods=['GET', 'POST', 'PUT', 'DELETE'])
def model_predictions():
    method = request.method
    args = request.args
    request_body_data = request.get_json(silent=True) or {}
    model_prediction_controller = current_app.model_prediction_controller
    response = model_prediction_controller.model_prediction_response(method, args, request_body_data)
    return response
