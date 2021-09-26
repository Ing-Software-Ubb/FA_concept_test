from fastapi import FastAPI
from bd import SessionLocal, engine,Base
from Resources import item

#ojo piojo ACÁ
##Base.metadata.create_all(bind=engine)

# incializamos la app 
app = FastAPI() 
# Añadimos los recursos o rutas que se requieren
app.include_router(item.router)
 
 # Acá deberia implementar la conexión a la base de datos

# Dependency


# run with command: 
#    uvicorn app:app --reload and test with postman or similar 
#   windows: python -m uvicorn app:app --reload