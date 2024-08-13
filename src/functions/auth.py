from fastapi import APIRouter, Body, status, Path

from src.config.constants import AUTH_ROUTE
from src.entities.schemas.user import UserSchema
from src.services.auth import AuthService

auth_router = APIRouter(prefix=AUTH_ROUTE)

@auth_router.post(
    path="",
    response_model=dict,
    status_code=status.HTTP_201_CREATED
)
def authenticate_user(user: UserSchema = Body(...)):
    return AuthService().authenticate_user(user)

@auth_router.post(
    path="/register",
    response_model=dict,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserSchema = Body(...)):
    return AuthService().create_user(user)