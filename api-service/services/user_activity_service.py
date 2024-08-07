import json
from flask import jsonify
from bson.objectid import ObjectId
from dao.user_activity_dao import UserActivityDao

class UserActivityService:
    def __init__(self):
        self.user_activity_dao = UserActivityDao()

    def get_all_user_activity(self):
        user_activityList = self.user_activity_dao.get_all_user_activity()
        return self.format_response(user_activityList)
    
    def get_user_activity_by_params(self, query_params):
        query = {}
        for key, value in query_params.items():
            query[key] = value if key != "_id" else ObjectId(value)
        user_activity_list = self.user_activity_dao.get_user_activity_by_params(query)
        return self.format_response(user_activity_list)
    
    def insert_user_activity(self, request_data):
        if request_data and isinstance(request_data, list):            
            response = self.user_activity_dao.insert_user_activity(request_data)
            inserted_ids = [str(inserted_id) for inserted_id in response.inserted_ids]
            return jsonify({"message": "user_activity inserted successfully", "inserted_ids": inserted_ids}), 201
        else:
            return jsonify({"message": "Invalid request body or data format"}), 400
        
    def update_user_activity(self, args, request_data):
        user_activity_id = ObjectId(args.get("_id"))
        filter_query = {"_id": user_activity_id}
        update_operation = {"$set": request_data}
        result = self.user_activity_dao.update_user_activity(filter_query, update_operation)
        if result:
            return jsonify({"message": "user_activity updated successfully"}), 200
        else:
            return jsonify({"message": "Failed to update user_activity"}), 400

    def delete_user_activity(self, args):
        user_activity_id = args.get("_id")
        result = self.user_activity_dao.delete_user_activity_by_id(ObjectId(user_activity_id))
        if result.deleted_count == 1:
            return jsonify({"message": "user_activity deleted successfully", "deleted_ids": user_activity_id}), 200
        else:
            return jsonify({"message": "No user_activity found with the provided IDs"}), 404
    
    def format_response(self, datas):
        user_activity = []
        for document in datas:
            document['_id'] = str(document['_id'])
            user_activity.append(document)
        response = {"user_activity": user_activity}
        json_response = json.dumps(response)
        return json.loads(json_response)  