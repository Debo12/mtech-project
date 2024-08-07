from services.model_train_metadata_service import ModelTrainMetadataService

class ModelTrainMetadataController:
    def __init__(self) -> None:
        self.model_train_metadata_service = ModelTrainMetadataService()

    def model_train_metadata_response(self, method, args, request_body_data):
        args = None
        if method == "GET":
            if args is None:
                return self.model_train_metadata_service.get_all_model_train_metadata()
            return self.model_train_metadata_service.get_model_train_metadata_by_params(args)
        elif method == "POST":
            return self.model_train_metadata_service.insert_model_train_metadata(request_body_data)
        elif method == "PUT":
            return self.model_train_metadata_service.update_model_train_metadata(args, request_body_data)
        elif method == "DELETE":
            return self.model_train_metadata_service.delete_model_train_metadata(args)
