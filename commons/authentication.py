from fastapi import Request, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from commons.helper import generate_jwt_token, decode_jwt_token
from models.user import User
from Database.db import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Authenticate the user and return a JWT token
def user_authentication(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user and user.password == password:
        return generate_jwt_token(user.id, user.username)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

# Decorator that ensures JWT token is valid and attaches the user to the request
def jwt_required_decorator(func):
    def wrapper(request: Request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token is missing')

        token = auth_header.split(" ")[1]  # Extract token from 'Bearer <token>'
        try:
            user_id = decode_jwt_token(token)
            request.state.user_id = user_id
        except Exception:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid or expired token')
        return func(request)

    return wrapper
