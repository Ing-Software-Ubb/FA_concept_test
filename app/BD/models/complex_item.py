from pydantic import BaseModel
 

class ComplexItem(BaseModel):
    id:int
    name:str
    existe:bool