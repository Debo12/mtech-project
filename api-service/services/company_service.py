import json
from flask import jsonify
from bson.objectid import ObjectId
from dao.company_dao import CompanyDao

class CompanyService:
    def __init__(self):
        self.company_dao = CompanyDao()

    def get_all_companies(self):
        companyList = self.company_dao.get_all_companies()
        return self.format_response(companyList)
    
    def get_companies_by_params(self, query_params):
        query = {}
        for key, value in query_params.items():
            query[key] = value if key != "_id" else ObjectId(value)
        companies_list = self.company_dao.get_companies_by_params(query)
        return self.format_response(companies_list)
    
    def insert_company(self, request_data):
        if request_data and isinstance(request_data, list):
            response = self.company_dao.insert_companies(request_data)
            inserted_ids = [str(inserted_id) for inserted_id in response.inserted_ids]
            return jsonify({"message": "Companies inserted successfully", "inserted_ids": inserted_ids}), 201
        else:
            return jsonify({"message": "Invalid request body or data format"}), 400
        
    def update_company(self, args, request_data):
        company_id = ObjectId(args.get("_id"))
        filter_query = {"_id": company_id}
        update_operation = {"$set": request_data}
        result = self.company_dao.update_companies(filter_query, update_operation)
        if result:
            return jsonify({"message": "Company updated successfully"}), 200
        else:
            return jsonify({"message": "Failed to update company"}), 400

    def delete_company(self, args):
        company_id = args.get("_id")
        result = self.company_dao.delete_company_by_id(ObjectId(company_id))
        if result.deleted_count == 1:
            return jsonify({"message": "Companies deleted successfully", "deleted_ids": company_id}), 200
        else:
            return jsonify({"message": "No companies found with the provided IDs"}), 404
    
    def format_response(self, datas):
        companies = []
        for document in datas:
            document['_id'] = str(document['_id'])
            companies.append(document)
        response = {"companies": companies}
        json_response = json.dumps(response)
        return json.loads(json_response)  