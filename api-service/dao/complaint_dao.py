from .base_dao import BaseDAO

class ComplaintDao:
    def __init__(self) -> None:
        baseDao = BaseDAO()
        self.collection = baseDao.get_db_connection().Complaints

    def get_all_complaint(self):
        cursor = self.collection.find({})
        return cursor
    
    def get_complaint_by_params(self, query_params):
        complaint = self.collection.find(query_params)
        complaint_list = list(complaint)
        return complaint_list
    
    def insert_complaint(self, request_data):
        inserted_result = self.collection.insert_many(request_data)
        return inserted_result
    
    def update_complaint(self, filter_query, update_operation):
        updated_result = self.collection.update_one(filter_query, update_operation)
        return updated_result.modified_count
    
    def delete_complaint_by_id(self, id):
        result  = self.collection.delete_one({"_id": id})
        return result
