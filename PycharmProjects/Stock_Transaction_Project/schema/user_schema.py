from pydantic import BaseModel
from decimal import Decimal

class UserSchema(BaseModel):
    id:int
    name:str
    initial_price:Decimal
    class Config:
        from_attributes = True