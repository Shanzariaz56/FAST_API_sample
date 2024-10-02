from pydantic import BaseModel

class BookSchema(BaseModel):
    id:int
    title:str
    author:str
    description:str

    class Config:
        from_attributes = True