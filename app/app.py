from fastapi import FastAPI
from bd import SessionLocal, engine,Base
from Resources import a

#ojo piojo ACÁ
Base.metadata.create_all(bind=engine)

# incializamos la app 
app = FastAPI() 
# Añadimos los recursos o rutas que se requieren
app.include_router(a.router)
 
 # Acá deberia implementar la conexión a la base de datos

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# run with command: 
#    uvicorn app:app --reload and test with postman or similar 
#   windows: python -m uvicorn app:app --reload