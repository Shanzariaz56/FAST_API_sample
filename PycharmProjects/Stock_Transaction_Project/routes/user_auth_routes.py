from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models.user_auth import UserAuth
from schema.user_auth_schema import UserRegister,LoginResponse,UserLogin
from commons.authentication import user_authentication, verify_password
from passlib.context import CryptContext
import bcrypt

router=APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Registration Routes
@router.post("/registration")#response_model=UserRegister)
def user_registration(user:UserRegister, db:Session=Depends(get_db)):
    try:
        existing_user=db.query(UserAuth).filter(UserAuth.username== user.username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already registered")
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        new_user = UserAuth(
            username=user.username,
            password=hashed_password.decode('utf-8')
        )  # Store the hashed password
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "User registered successfully", "user": new_user.username}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Login Routes
@router.post("/login/", response_model=LoginResponse)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    print("jhgjiuhgbnjhghjhcbjhbn")
    try:
        token = user_authentication(user.username, user.password, db)
        if not token:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {
            "access_token": token,
            "token_type": "bearer",
            "username": user.username
        }
    except Exception as e:
        pass

