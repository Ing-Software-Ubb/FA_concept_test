from fastapi import APIRouter
from BD.models.item import Item

router = APIRouter()  

@router.post("/b/{item_name}") 
def b(item_name):
    new_item = Item(name = item_name)
    return new_item