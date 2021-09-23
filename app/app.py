from fastapi import FastAPI

from Resources import a,b,c


# incializamos la app 
app = FastAPI() 
# Añadimos los recursos o rutas que se requieren
app.include_router(a.router)
app.include_router(b.router)
app.include_router(c.router)
 
 # Acá deberia implementar la conexión a la base de datos


# run with command: 
#    uvicorn app:app --reload and test with postman or similar 