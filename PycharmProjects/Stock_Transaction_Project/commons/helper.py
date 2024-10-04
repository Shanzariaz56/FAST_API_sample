import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from commons.constants import SIMPLE_JWT, JWT_EXPIRATION_DELTA_MINUTES

def generate_jwt_token(user_id: int, username: str) -> str:
    """Generate a JWT token for a given user ID and username."""
    payload = {
        "id": user_id,
        "username": username,
        "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_DELTA_MINUTES),
        "iat": datetime.utcnow()
    }
    return jwt.encode(payload, SIMPLE_JWT["SIGNING_KEY"], algorithm=SIMPLE_JWT["ALGORITHM"])

def decode_jwt_token(token: str) -> int:
    """Decode a JWT token and return the user ID."""
    try:
        payload = jwt.decode(token, SIMPLE_JWT["SIGNING_KEY"], algorithms=[SIMPLE_JWT["ALGORITHM"]])
        return payload.get("id")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")




'''
    Here, two main functions are constructed:
    1. Generate JWT token
    2. Decode JWT token

import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException

# Assume these constants are defined in commons/constants.py
from commons.constants import SIMPLE_JWT, JWT_EXPIRATION_DELTA_MINUTES

def generate_jwt_token(user_id: int, username: str) -> str:
    """Generate a JWT token for a given user ID and username."""
    payload = {
        "id": user_id,
        "username": username,
        "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_DELTA_MINUTES),
        "iat": datetime.utcnow()
    }
    token = jwt.encode(payload, SIMPLE_JWT["SIGNING_KEY"], algorithm=SIMPLE_JWT["ALGORITHM"])
    return token

def decode_jwt_token(token: str) -> int:
    """Decode a JWT token and return the user ID."""
    try:
        payload = jwt.decode(token, SIMPLE_JWT["SIGNING_KEY"], algorithms=[SIMPLE_JWT["ALGORITHM"]])
        return payload.get("id")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")'''
