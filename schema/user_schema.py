from pydantic import BaseModel

class UserRegister(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True