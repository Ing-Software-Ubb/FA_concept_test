from pydantic import BaseModel
 

class ItemScheme (BaseModel):
    id:int
    nombre:str
    exite:bool
