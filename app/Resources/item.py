from typing import List
from fastapi import APIRouter,Depends
from models.item import Item
from schemes.item import ItemScheme
from sqlalchemy.orm import Session
from app import get_db
router = APIRouter()  

@router.get("/a")
def a():
    return {"message": "recurso A usando método get"} 


@router.get("/items/", response_model=List[ItemScheme])
def show_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items