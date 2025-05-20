from fastapi import FastAPI
from routers.calculator import router

app = FastAPI()

app.include_router(router, prefix="/calculadora")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API da Calculadora! Acesse /doc"}