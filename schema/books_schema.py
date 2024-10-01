from pydantic import BaseModel

class BookSchema(BaseModel):
    id:int
    title:str
    author:str
    description:str

    class Config:
        orm_mode = True  # Allows ORM objects to be serialized