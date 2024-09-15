from fastapi import APIRouter
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def RotaInicial():
    return {"message": "bem-vindo à primeira rota do projeto"}
