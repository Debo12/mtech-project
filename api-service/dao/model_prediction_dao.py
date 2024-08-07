from .base_dao import BaseDAO

class ModelPredictionDao:
    def __init__(self) -> None:
        baseDao = BaseDAO()
        self.collection = baseDao.get_db_connection().Model_Prediction

    def get_all_model_prediction(self):
        cursor = self.collection.find({})
        return cursor
    
    def get_model_prediction_by_params(self, query_params):
        modelPrediction = self.collection.find(query_params)
        modelPrediction_list = list(modelPrediction)
        return modelPrediction_list
    
    def insert_model_prediction(self, request_data):
        inserted_result = self.collection.insert_many(request_data)
        return inserted_result
    
    def update_model_prediction(self, filter_query, update_operation):
        updated_result = self.collection.update_one(filter_query, update_operation)
        return updated_result.modified_count
    
    def delete_model_prediction_by_id(self, id):
        result  = self.collection.delete_one({"_id": id})
        return result
