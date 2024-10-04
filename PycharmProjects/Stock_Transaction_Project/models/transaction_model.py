from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from models.user_model import User
from models.stock_model import Stock
from enum import Enum as pyEnum
from datetime import datetime
from database.db import Base
from sqlalchemy.types import DECIMAL

class TransactionType(pyEnum):
    BUY = "buy"
    SELL = "sell"

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    transaction_type = Column(Enum(TransactionType), default=TransactionType.SELL)
    transaction_volume = Column(Integer, nullable=False)
    transaction_price = Column(DECIMAL(20, 2), nullable=False)
    transaction_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="transactions")
    stock = relationship("Stock", back_populates="transactions")

