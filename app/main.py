import uvicorn
from fastapi import FastAPI
from app.handlers import router

def app_aplication()->FastAPI:
    application = FastAPI()
    application.include_router(router)
    return application

app = app_aplication()
