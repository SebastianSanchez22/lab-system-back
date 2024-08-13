from src.decorators.decorators import try_except_decorator

class AuthService(object):

    def __init__(self):
        self.resource = AuthResource()

    @try_except_decorator
    def authenticate_user(self, user: dict) -> dict:
        return self.resource.authenticate_user(user)
    
    @try_except_decorator
    def create_user(self, user: dict) -> dict:
        return self.resource.create_user(user)