from services.user_service import UserService

class UserController:
    def __init__(self) -> None:
        self.user_service = UserService()

    def user_response(self, method, args, request_body_data):
        if method == "GET":
            if args is None:
                return self.user_service.get_all_user() # For admin
            return self.user_service.get_user_by_params(args)
        elif method == "POST":
            return self.user_service.insert_user(request_body_data)
        elif method == "PUT":
            return self.user_service.update_user(args, request_body_data) # For admin
        elif method == "DELETE":
            return self.user_service.delete_user(args) # For admin