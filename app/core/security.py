from datetime import timedelta
from typing import Any, Union

from fastapi_jwt_auth import AuthJWT
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


@AuthJWT.load_config
def get_config():
    return settings


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None, authorize: AuthJWT = None
) -> tuple[str, str]:
    access_token = authorize.create_access_token(subject=str(subject), algorithm=ALGORITHM, expires_time=expires_delta)
    refresh_token = authorize.create_refresh_token(
        subject=str(subject), algorithm=ALGORITHM, expires_time=expires_delta
    )
    return access_token, refresh_token


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
