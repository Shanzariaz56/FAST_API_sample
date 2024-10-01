from sqlalchemy import Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base

'''this line create a base class for your sqlalchemy models
all models should be inherited from this class'''

Base=declarative_base()
class Book(Base):
    __tablename__ = "books"

    id=Column(Integer,primary_key=True, autoincrement=True)
    title=Column(String,nullable=False)
    author=Column(String,nullable=False)
    description=Column(String,nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"