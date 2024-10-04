from fastapi import Request, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database.db import get_db
from models.user_auth import UserAuth
from commons.helper import generate_jwt_token, decode_jwt_token
from passlib.context import CryptContext
import bcrypt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def user_authentication(username: str, password: str, db: Session = Depends(get_db)) -> str:
    """Authenticate the user and return a JWT token."""
    user = db.query(UserAuth).filter(UserAuth.username == username).first()
    if user and verify_password(password, user.password):
        return generate_jwt_token(user.id, user.username)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

def jwt_required_decorator(func):
    """Decorator to ensure JWT token is valid."""
    def wrapper(request: Request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token is missing')

        token = auth_header.split(" ")[1]
        user_id = decode_jwt_token(token)
        request.state.user_id = user_id
        return func(request)

    return wrapper

'''from fastapi import Request, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database.db import get_db
from models.user_auth import UserAuth
from commons.helper import generate_jwt_token, decode_jwt_token
from passlib.context import CryptContext

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create a password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


# User Registration
def user_registration(username: str, password: str, db: Session) -> UserAuth:
    if db.query(UserAuth).filter(UserAuth.username == username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    hashed_password = get_password_hash(password)
    new_user = UserAuth(username=username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Authenticate the user and return a JWT token
def user_authentication(username: str, password: str, db: Session = Depends(get_db)) -> str:
    user = db.query(UserAuth).filter(UserAuth.username == username).first()
    if user and verify_password(password, user.password):
        return generate_jwt_token(user.id, user.username)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")


# JWT Required Decorator
def jwt_required_decorator(func):
    async def wrapper(request: Request, db: Session = Depends(get_db)):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token is missing')

        token = auth_header.split(" ")[1]  # Extract token from 'Bearer <token>'
        try:
            user_id = decode_jwt_token(token)
            request.state.user_id = user_id  # Attach user_id to the request state
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token has expired')
        except jwt.JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
        return await func(request, db)

    return wrapper'''
