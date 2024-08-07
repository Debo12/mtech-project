from services.user_activity_service import UserActivityService

class UserActivityController:
    def __init__(self) -> None:
        self.user_activity_service = UserActivityService()

    def user_activity_response(self, method, args, request_body_data):
        if method == "GET":
            if args is None:
                return self.user_activity_service.get_all_user_activity()
            return self.user_activity_service.get_user_activity_by_params(args)
        elif method == "POST":
            return self.user_activity_service.insert_user_activity(request_body_data)
        elif method == "PUT":
            return self.user_activity_service.update_user_activity(args, request_body_data)
        elif method == "DELETE":
            return self.user_activity_service.delete_user_activity(args)
