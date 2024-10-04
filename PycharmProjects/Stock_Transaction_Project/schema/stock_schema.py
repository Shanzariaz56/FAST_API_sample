from pydantic import BaseModel
from decimal import Decimal

class StockSchema(BaseModel):
    id:int
    ticker:str
    price:Decimal
    class Config:
        from_attributes = True