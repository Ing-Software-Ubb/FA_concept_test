from fastapi import APIRouter

router = APIRouter()  

@router.get("/a")
def a():
    return {"message": "recurso A usando método get"} 
