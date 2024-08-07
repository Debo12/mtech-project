from .base_dao import BaseDAO

class UserActivityDao:
    def __init__(self) -> None:
        baseDao = BaseDAO()
        self.collection = baseDao.get_db_connection().User_Activity

    def get_all_user_activity(self):
        cursor = self.collection.find({})
        return cursor
    
    def get_user_activity_by_params(self, query_params):
        user_activity = self.collection.find(query_params)
        user_activity_list = list(user_activity)
        return user_activity_list
    
    def insert_user_activity(self, request_data):
        inserted_result = self.collection.insert_many(request_data)
        return inserted_result
    
    def update_user_activity(self, filter_query, update_operation):
        updated_result = self.collection.update_one(filter_query, update_operation)
        return updated_result.modified_count
    
    def delete_user_activity_by_id(self, id):
        result  = self.collection.delete_one({"_id": id})
        return result
