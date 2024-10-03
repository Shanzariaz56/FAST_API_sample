'''
     HERE TWO MAIN FUNCTION IS CONSTRUCTED
     1- GENERATE JWT TOKEN
     2- DECODE HWT TOKEN
'''
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException

from commons.constants import SIMPLE_JWT,JWT_EXPIRATION_DELTA_MINUTES

    payload={
        "id":user_id,
        "username":username,
        "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_DELTA_MINUTES),
        "iat":datetime.utcnow()
    }
    token=jwt.encode(payload,SIMPLE_JWT["SIGNING_KEY"],algorithms=SIMPLE_JWT["ALGORITHM"])
    return token

def decode_jwt_token(token:str) -> int:
    try:
        payload=jwt.decode(token,SIMPLE_JWT["SIGNING_KEY"],algorithms=SIMPLE_JWT["ALGORITHM"])
        return payload.get("id")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
