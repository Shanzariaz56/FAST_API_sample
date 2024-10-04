from pydantic import BaseModel
from decimal import Decimal
from enum import Enum

class TransactionType(str,Enum):
    BUY="buy"
    SELL="sell"

class TransactionSchema(BaseModel):
    id:int
    user_id:int
    stock_id:int
    transaction_type:TransactionType=TransactionType.SELL
    transaction_volume:int
    transaction_price:Decimal
    class Config:
        from_attributes = True
















'''from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal
from datetime import datetime
from enum import Enum

class TransactionType(str, Enum):
    BUY = "buy"
    SELL = "sell"

class TransactionBase(BaseModel):
    user_id: int
    stock_id: int
    transaction_type: TransactionType = TransactionType.SELL
    transaction_volume: int
    transaction_price: Decimal
    class Config:
        orm_mode = True'''



