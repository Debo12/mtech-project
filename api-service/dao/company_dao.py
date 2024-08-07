from .base_dao import BaseDAO

class CompanyDao:
    def __init__(self) -> None:
        baseDao = BaseDAO()
        self.collection = baseDao.get_db_connection().Insurance_Companies

    def get_all_companies(self):
        cursor = self.collection.find({})
        return cursor
    
    def get_companies_by_params(self, query_params):
        companies = self.collection.find(query_params)
        companies_list = list(companies)
        return companies_list
    
    def insert_companies(self, request_data):
        inserted_result = self.collection.insert_many(request_data)
        return inserted_result
    
    def update_companies(self, filter_query, update_operation):
        updated_result = self.collection.update_one(filter_query, update_operation)
        return updated_result.modified_count
    
    def delete_company_by_id(self, id):
        result  = self.collection.delete_one({"_id": id})
        return result
