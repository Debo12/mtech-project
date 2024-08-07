from .base_dao import BaseDAO

class ModelTrainMetadataDao:
    def __init__(self) -> None:
        baseDao = BaseDAO()
        self.collection = baseDao.get_db_connection().Model_Train_Metadata

    def get_all_model_train_metadata(self):
        cursor = self.collection.find({})
        return cursor
    
    def get_model_train_metadata_by_params(self, query_params):
        modeltrain_metadata = self.collection.find(query_params)
        modeltrain_metadata_list = list(modeltrain_metadata)
        return modeltrain_metadata_list
    
    def insert_model_train_metadata(self, request_data):
        inserted_result = self.collection.insert_many(request_data)
        return inserted_result
    
    def update_model_train_metadata(self, filter_query, update_operation):
        updated_result = self.collection.update_one(filter_query, update_operation)
        return updated_result.modified_count
    
    def delete_model_train_metadata_by_id(self, id):
        result  = self.collection.delete_one({"_id": id})
        return result
