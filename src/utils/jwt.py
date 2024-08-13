import jwt
import os
import pytz

from datetime import datetime, timedelta

from src.config.constants import ALGORITHM
from src.config.env import SECRET_KEY

def create_jwt_token(data: dict, expires_delta: timedelta = timedelta(hours=1)) -> str:
    to_encode = data.copy()
    expire = datetime.now(pytz.UTC) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_jwt_token(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token if decoded_token["exp"] >= datetime.now(pytz.UTC).timestamp() else None
    except jwt.PyJWTError:
        return None