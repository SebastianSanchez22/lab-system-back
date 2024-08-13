from typing import Dict, List

from src.config.constants import DELETE_SUCCESS, POST_SUCCESS, PUT_SUCCESS
from src.decorators.decorators import try_except_decorator
from src.resources.user import UserResource

class UserService(object):

    def __init__(self):
       self.resource = UserResource()

    @try_except_decorator
    def get_all(self) -> List[Dict]:
        return self.resource.get_all()
    
    @try_except_decorator
    def add_one(self, user: dict) -> str:
        self.resource.add_one(user)
        return {"message": POST_SUCCESS}
    
    @try_except_decorator
    def update_one(self, id: int, user: dict) -> dict:
        self.resource.update_one(id, user)
        return {"message": PUT_SUCCESS}
    
    @try_except_decorator
    def delete_one(self, id: int):
        self.resource.delete_one(id)
        return {"message": DELETE_SUCCESS}