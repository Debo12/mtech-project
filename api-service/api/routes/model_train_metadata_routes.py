from flask import Blueprint, request, jsonify, current_app

model_train_metadata_routes = Blueprint('model_train_metadata_routes', __name__)

@model_train_metadata_routes.route("/model_train_metadatas", methods=['GET', 'POST', 'PUT', 'DELETE'])
def model_train_metadatas():
    method = request.method
    args = request.args
    request_body_data = request.get_json(silent=True) or {}
    model_train_metadata_controller = current_app.model_train_metadata_controller
    response = model_train_metadata_controller.model_train_metadata_response(method, args, request_body_data)
    return response
