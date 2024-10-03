from sqlalchemy import Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)