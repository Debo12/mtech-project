from services.user_service import UserService

class LoginController:
    def __init__(self) -> None:
        self.user_service = UserService()

    def login_response(self, data):
        return self.user_service.login_check(data)