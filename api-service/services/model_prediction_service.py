import json
from flask import jsonify
from bson.objectid import ObjectId
from dao.model_prediction_dao import ModelPredictionDao

class ModelPredictionService:
    def __init__(self):
        self.model_prediction_dao = ModelPredictionDao()

    def get_all_model_prediction(self):
        modelPredictionList = self.model_prediction_dao.get_all_model_prediction()
        return self.format_response(modelPredictionList)
    
    def get_model_prediction_by_params(self, query_params):
        query = {}
        for key, value in query_params.items():
            query[key] = value if key != "_id" else ObjectId(value)
        modelPrediction_list = self.model_prediction_dao.get_model_prediction_by_params(query)
        return self.format_response(modelPrediction_list)
    
    def insert_model_prediction(self, request_data):
        if request_data and isinstance(request_data, list):
            response = self.model_prediction_dao.insert_model_prediction(request_data)
            inserted_ids = [str(inserted_id) for inserted_id in response.inserted_ids]
            return jsonify({"message": "modelPrediction inserted successfully", "inserted_ids": inserted_ids}), 201
        else:
            return jsonify({"message": "Invalid request body or data format"}), 400
        
    def update_model_prediction(self, args, request_data):
        modelPrediction_id = ObjectId(args.get("_id"))
        filter_query = {"_id": modelPrediction_id}
        update_operation = {"$set": request_data}
        result = self.model_prediction_dao.update_model_prediction(filter_query, update_operation)
        if result:
            return jsonify({"message": "modelPrediction updated successfully"}), 200
        else:
            return jsonify({"message": "Failed to update modelPrediction"}), 400

    def delete_model_prediction(self, args):
        modelPrediction_id = args.get("_id")
        result = self.model_prediction_dao.delete_model_prediction_by_id(ObjectId(modelPrediction_id))
        if result.deleted_count == 1:
            return jsonify({"message": "modelPrediction deleted successfully", "deleted_ids": modelPrediction_id}), 200
        else:
            return jsonify({"message": "No modelPrediction found with the provided IDs"}), 404
    
    def format_response(self, datas):
        modelPrediction = []
        for document in datas:
            document['_id'] = str(document['_id'])
            modelPrediction.append(document)
        response = {"modelPrediction": modelPrediction}
        json_response = json.dumps(response)
        return json.loads(json_response)  