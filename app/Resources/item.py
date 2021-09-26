from typing import List
from fastapi import APIRouter,Depends
from models.item import Item
from schemes.item import ItemScheme
from sqlalchemy.orm import Session
from bd import get_db
router = APIRouter()  

@router.get("/a")
def a():
    return {"message": "recurso A usando método get"} 


@router.get("/items/", response_model=List[ItemScheme])
def show_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Item).all() # Hasta aquí debería ser suficiente

    # Esta segunda forma utilizando una forma mas controlada de la BD
    # sugiere utilizar metodos de clase que en principio debiesen ir en los modelos
    # podemos discutir mas adelante esto !! 
    items = get_users(db, skip=skip, limit=limit)
    return items

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()