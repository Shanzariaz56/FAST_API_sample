from sqlalchemy import Column, String,Integer
from sqlalchemy.types import DECIMAL
from database.db import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String, index=True, nullable=False)
    initial_balance=Column(DECIMAL(20,2), nullable=False)

    transactions = relationship("Transaction", back_populates="user")