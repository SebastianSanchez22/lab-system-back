from fastapi import APIRouter, Body, status, Path
from typing import List

from src.services.user import UserService
from src.config.constants import USER_ROUTE
from src.entities.schemas.user import UserSchema

user_router = APIRouter(prefix=USER_ROUTE)

@user_router.get(
    path='', 
    response_model=List[UserSchema],
    status_code=status.HTTP_200_OK
)
def get_users():
    return UserService().get_all()

@user_router.post(
    path="",
    response_model=dict,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserSchema = Body(...)):
    return UserService().add_one(user.model_dump())

@user_router.put(
    path="/{id}", 
    response_model=dict,
    status_code=status.HTTP_200_OK
)
def update_user(id: int = Path(...), user: UserSchema = Body(...)):
    return UserService().update_one(id, user.model_dump())

@user_router.delete(
    path="/{id}",
    response_model=dict, 
    status_code=status.HTTP_200_OK
)
def delete_user(id: int = Path(...)):
    return UserService().delete_one(id)