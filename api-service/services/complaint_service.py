import json
from flask import jsonify
from bson.objectid import ObjectId
from dao.complaint_dao import ComplaintDao

class ComplaintService:
    def __init__(self):
        self.complaint_dao = ComplaintDao()

    def get_all_complaint(self):
        complaintList = self.complaint_dao.get_all_complaint()
        return self.format_response(complaintList)

    def get_complaint_by_params(self, query_params):
        query = {}
        for key, value in query_params.items():
            query[key] = value if key != "_id" else ObjectId(value)
        
        complaint_list = []
        if "NAIC" in query:
            # If NAIC is present in the query parameters, filter complaints based on NAIC
            complaint_list = self.complaint_dao.get_complaint_by_params({'NAIC': int(query_params.get('NAIC'))})
        else:
            # If NAIC is not present, get all complaints
            complaint_list = self.complaint_dao.get_complaint_by_params(query)
        
        return self.format_response(complaint_list)

    
    def insert_complaint(self, request_data):
        if request_data and isinstance(request_data, list):
            response = self.complaint_dao.insert_complaint(request_data)
            inserted_ids = [str(inserted_id) for inserted_id in response.inserted_ids]
            return jsonify({"message": "complaint inserted successfully", "inserted_ids": inserted_ids}), 201
        else:
            return jsonify({"message": "Invalid request body or data format"}), 400
        
    def update_complaint(self, args, request_data):
        complaint_id = ObjectId(args.get("_id"))
        filter_query = {"_id": complaint_id}
        update_operation = {"$set": request_data}
        result = self.complaint_dao.update_complaint(filter_query, update_operation)
        if result:
            return jsonify({"message": "complaint updated successfully"}), 200
        else:
            return jsonify({"message": "Failed to update complaint"}), 400

    def delete_complaint(self, args):
        complaint_id = args.get("_id")
        result = self.complaint_dao.delete_complaint_by_id(ObjectId(complaint_id))
        if result.deleted_count == 1:
            return jsonify({"message": "complaint deleted successfully", "deleted_ids": complaint_id}), 200
        else:
            return jsonify({"message": "No complaint found with the provided IDs"}), 404
    
    def format_response(self, datas):
        complaint = []
        for document in datas:
            document['_id'] = str(document['_id'])
            complaint.append(document)
        response = {"complaint": complaint}
        json_response = json.dumps(response)
        return json.loads(json_response)  