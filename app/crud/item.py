from sqlalchemy.orm import Session
from models.item import Item
from schemes.item import ItemScheme

def get_item(db: Session, id: int):
    return db.query(Item).filter(Item.id==id).first()

def insert_item(db: Session, id, nombre, existe):
    new_item = Item(id=id, nombre=nombre, existe=existe)
    db.add(new_item)
    db.commit()

def delete_item(db: Session, id: int):
    db.query(Item).filter(Item.id==id).delete()
    db.commit()

def update_item_name(db: Session, id:int, new_name:str):
    db.query(Item).filter(Item.id==id).update({"nombre":new_name})
    db.commit()