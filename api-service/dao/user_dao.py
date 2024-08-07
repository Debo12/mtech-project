from .base_dao import BaseDAO

class UserDao:
    def __init__(self) -> None:
        baseDao = BaseDAO()
        self.collection = baseDao.get_db_connection().Users

    def get_all_user(self):
        cursor = self.collection.find({})
        return cursor
    
    def get_user_by_params(self, query_params):
        user = self.collection.find(query_params)
        user_list = list(user)
        return user_list
    
    def insert_user(self, request_data):
        inserted_result = self.collection.insert_one(request_data)
        return inserted_result
    
    def update_user(self, filter_query, update_operation):
        updated_result = self.collection.update_one(filter_query, update_operation)
        return updated_result.modified_count
    
    def delete_user_by_id(self, id):
        result  = self.collection.delete_one({"_id": id})
        return result
    
    def login_check(self, username, phone):
        result = self.collection.find_one({'$or': [{'username': username}, {'phone': phone}]})
        return result