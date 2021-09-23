from fastapi import APIRouter, Request
from BD.models.complex_item import ComplexItem

router = APIRouter()  

@router.post("/c") 
def b(item:ComplexItem):
    alfa = item.id
    beta = item.name
    gamma = item.existe
    new_item = ComplexItem(id= alfa , name = beta, existe = gamma)
    return new_item