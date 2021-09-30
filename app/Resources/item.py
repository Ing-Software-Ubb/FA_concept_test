from typing import List
from fastapi import APIRouter,Depends
from models.item import Item
from schemes.item import ItemScheme
from sqlalchemy.orm import Session
from bd import get_db
from crud.item import get_item, insert_item, update_item_name, delete_item
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

@router.get("/item/{id}")
def get_ite(id, db: Session = Depends(get_db)):
    item = get_item(db, id)
    return{
        "id": item.id,
        "name": item.nombre,
        "exist": item.existe
    }

@router.post("/items/insert/{id}/{nombre}/{existe}")
def ins_item(id, nombre, existe:bool, db: Session = Depends(get_db)):
    insert_item(db, id, nombre, existe)
    return {"message:" "Complete"
    }

@router.delete("/items/delete/{id}")
def del_item(id, db: Session = Depends(get_db)):
    delete_item(db, id)
    return {"message:" "Delete complete"
    }

@router.put("/items/update/{id}/{newname}")
def upt_item_name(id, newname, db: Session = Depends(get_db)):
    update_item_name(db, id, newname)
    return {"message:" "update complete"
    }