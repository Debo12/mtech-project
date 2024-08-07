from flask import Response, jsonify
from dao.user_dao import UserDao
import logging
import http
import json
from bson import ObjectId
from werkzeug.security import check_password_hash, generate_password_hash

class UserService:
    def __init__(self):
        self.user_dao = UserDao()

    def get_all_user(self):
        userList = self.user_dao.get_all_user()
        return self.format_response(userList)
    
    def get_user_by_params(self, query_params):
        query = {}
        for key, value in query_params.items():
            query[key] = value if key != "_id" else ObjectId(value)
        user_list = self.user_dao.get_user_by_params(query)
        return self.format_response(user_list)
    
    def insert_user(self, request_data):
        if request_data and isinstance(request_data, dict):
            username = request_data.get('username')
            phone = request_data.get('phone')
            existing_user = self.user_dao.login_check(username, phone)
            if existing_user:
                return jsonify({"message": "Username or phone number already exists"}), 409
            request_data['password'] = generate_password_hash(request_data['password'])
            response = self.user_dao.insert_user(request_data)
            inserted_ids = str(response.inserted_id)
            return jsonify({"message": "user created successfully", "inserted_ids": inserted_ids}), 201
        else:
            return jsonify({"message": "Invalid request body or data format"}), 400
        
    def update_user(self, args, request_data):
        user_id = ObjectId(args.get("_id"))
        filter_query = {"_id": user_id}
        update_operation = {"$set": request_data}
        result = self.user_dao.update_user(filter_query, update_operation)
        if result:
            return jsonify({"message": "user updated successfully"}), 200
        else:
            return jsonify({"message": "Failed to update user"}), 400

    def delete_user(self, args):
        user_id = args.get("_id")
        result = self.user_dao.delete_user_by_id(ObjectId(user_id))
        if result.deleted_count == 1:
            return jsonify({"message": "user deleted successfully", "deleted_ids": user_id}), 200
        else:
            return jsonify({"message": "No user found with the provided IDs"}), 404
    
    def format_response(self, datas):
        user = []
        for document in datas:
            document['_id'] = str(document['_id'])
            user.append(document)
        response = {"user": user}
        json_response = json.dumps(response)
        return json.loads(json_response)
    
    def login_check(self, data):
        username = data.get('username')
        password = data.get('password')

        user = self.user_dao.login_check(username, username)

        if user:
            # Verify the password
            stored_password = user['password']
            if check_password_hash(stored_password, password):
                # Password is correct, user is authenticated
                return jsonify({'message': 'Login successful', 'user_id': str(user['_id'])}), 200
            else:
                return jsonify({'message': 'Incorrect password'}), 401
        else:
            return jsonify({'message': 'User not found'}), 404

        # user  = self.user_dao.login_check(username)

        # if user and check_password_hash(user['password'], password):
        # # Login successful
        #     return jsonify({'message': 'Login successful!'}), 200
        # else:
        #     # Login failed
        #     return jsonify({'message': 'Invalid username or password.'}), 401