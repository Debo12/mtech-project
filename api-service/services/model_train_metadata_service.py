import json
from flask import jsonify
from bson.objectid import ObjectId
from dao.model_train_metadata_dao import ModelTrainMetadataDao

class ModelTrainMetadataService:
    def __init__(self):
        self.model_train_metadata_dao = ModelTrainMetadataDao()

    def get_all_model_train_metadata(self):
        model_train_metadataList = self.model_train_metadata_dao.get_all_model_train_metadata()
        return self.format_response(model_train_metadataList)
    
    def get_model_train_metadata_by_params(self, query_params):
        query = {}
        for key, value in query_params.items():
            query[key] = value if key != "_id" else ObjectId(value)
        model_train_metadata_list = self.model_train_metadata_dao.get_model_train_metadata_by_params(query)
        return self.format_response(model_train_metadata_list)
    
    def insert_model_train_metadata(self, request_data):
        if request_data and isinstance(request_data, list):
            response = self.model_train_metadata_dao.insert_model_train_metadata(request_data)
            inserted_ids = [str(inserted_id) for inserted_id in response.inserted_ids]
            return jsonify({"message": "model_train_metadata inserted successfully", "inserted_ids": inserted_ids}), 201
        else:
            return jsonify({"message": "Invalid request body or data format"}), 400
        
    def update_model_train_metadata(self, args, request_data):
        model_train_metadata_id = ObjectId(args.get("_id"))
        filter_query = {"_id": model_train_metadata_id}
        update_operation = {"$set": request_data}
        result = self.model_train_metadata_dao.update_model_train_metadata(filter_query, update_operation)
        if result:
            return jsonify({"message": "model_train_metadata updated successfully"}), 200
        else:
            return jsonify({"message": "Failed to update model_train_metadata"}), 400

    def delete_model_train_metadata(self, args):
        model_train_metadata_id = args.get("_id")
        result = self.model_train_metadata_dao.delete_model_train_metadata_by_id(ObjectId(model_train_metadata_id))
        if result.deleted_count == 1:
            return jsonify({"message": "model_train_metadata deleted successfully", "deleted_ids": model_train_metadata_id}), 200
        else:
            return jsonify({"message": "No model_train_metadata found with the provided IDs"}), 404
    
    def format_response(self, datas):
        model_train_metadata = []
        for document in datas:
            document['_id'] = str(document['_id'])
            model_train_metadata.append(document)
        response = {"model_train_metadata": model_train_metadata}
        json_response = json.dumps(response)
        return json.loads(json_response)  