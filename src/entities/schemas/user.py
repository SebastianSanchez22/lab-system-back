from typing import Optional
from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    lastName: str
    email: str
    username: str
    password: str