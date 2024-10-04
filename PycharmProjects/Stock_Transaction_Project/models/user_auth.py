from sqlalchemy import Column, String, Integer
from database.db import Base

class UserAuth(Base):
    __tablename__ = 'user_auth'
    id = Column(Integer, primary_key=True)
    username = Column(String,unique=True,nullable=False)
    password = Column(String)