from fastapi import APIRouter,status,Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from models.user_model import User
from schema.user_schema import UserSchema
from commons.authentication import jwt_required_decorator
from routes.user_auth_routes import user_registration,login_user
from fastapi.security import OAuth2PasswordBearer

router=APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# GET ALL RECORD
@router.get("/user",response_model=list[UserSchema])
def get_all_user(db:Session=Depends(get_db),token: str = Depends(oauth2_scheme)):
    user=db.query(User).all()
    return user

# GET BY USER_ID
@router.get("/user/{user_id}",response_model=UserSchema)
def get_user_by_id(user_id:int,db:Session=Depends(get_db),token: str = Depends(oauth2_scheme)):
    user=db.query(User).filter(User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user

# GET BY USER_NAME
@router.get("/user/{username}",response_model=UserSchema)
def get_user_by_username(username:str,db:Session=Depends(get_db),token: str = Depends(oauth2_scheme)):
    user=db.query(User).filter(User.name==username).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user

# CREATE NEW USER
@router.post("/user/add",response_model=UserSchema)
def create_new_user(user:UserSchema,db:Session=Depends(get_db),token: str = Depends(oauth2_scheme)):
    new_user=User(
        name=user.name,
        initial_balance=user.initial_balance,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
