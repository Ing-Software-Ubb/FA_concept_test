from pydantic import BaseModel
 

class ItemScheme(BaseModel):
    id:int
    nombre:str
    existe:bool

    class Config:
	    orm_mode = True