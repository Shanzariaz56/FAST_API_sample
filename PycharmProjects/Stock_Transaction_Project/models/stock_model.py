from sqlalchemy import Column, String, Integer
from sqlalchemy.types import DECIMAL
from database.db import Base
from sqlalchemy.orm import relationship

class Stock(Base):
    __tablename__="stocks"
    id=Column(Integer,primary_key=True,autoincrement=True)
    ticker=Column(String,unique=True,nullable=False)
    price=Column(DECIMAL(20,2),nullable=False)

    transactions = relationship("Transaction", back_populates="stock")
