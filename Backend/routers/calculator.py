from fastapi import APIRouter
from services.operacoes import calculate

router = APIRouter()
    
@router.get("/calcular")
def calcular(tipo: str, num: float, num2: float):
    resultado = calculate(tipo, num, num2)
    return {"tipo": tipo, "resultado": resultado}