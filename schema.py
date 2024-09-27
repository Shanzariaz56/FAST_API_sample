from pydantic import BaseModel
from uuid import UUID,uuid4

class Books(BaseModel):
    id:UUID=uuid4()
    title:str
    author:str
    description:str