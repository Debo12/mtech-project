from services.model_prediction_service import ModelPredictionService

class ModelPredictionController:
    def __init__(self) -> None:
        self.model_prediction_service = ModelPredictionService()

    def model_prediction_response(self, method, args, request_body_data):
        if method == "GET":
            if args is None:
                return self.model_prediction_service.get_all_model_prediction()
            return self.model_prediction_service.get_model_prediction_by_params(args)
        elif method == "POST":
            return self.model_prediction_service.insert_model_prediction(request_body_data)
        elif method == "PUT":
            return self.model_prediction_service.update_model_prediction(args, request_body_data)
        elif method == "DELETE":
            return self.model_prediction_service.delete_model_prediction(args)
