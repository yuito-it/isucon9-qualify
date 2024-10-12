from fastapi import FastAPI
from routers import apps

app = FastAPI()

# apps配下
app.include_router(apps.router)
