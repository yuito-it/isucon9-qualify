from fastapi import FastAPI
from routers import apps
from .database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

# apps配下
app.include_router(apps.router)
