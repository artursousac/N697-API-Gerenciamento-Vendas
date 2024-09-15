from fastapi import APIRouter
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def RotaInicial():
    return {"message": "bem-vindo à primeira rota do projeto"}

@router.get("/organizadores")
async def get_organizadores(inicio: int = Query(0), fim: int = None):
    """organizadores = listaOrganizadores(collection_Organizadores.find())"""
    totalOrganizadores = collection_Organizadores.count_documents({})
    if fim is None:
        fim = totalOrganizadores
    limit = fim+1 - inicio
    organizadoresCursor = listaOrganizadores(collection_Organizadores.find().skip(inicio).limit(limit))
    organizadores = list(organizadoresCursor)
    return organizadores

@router.get("/organizador/{id}")
async def get_organizador(id):
    organizador = unicoOrganizador(collection_Organizadores.find_one({"_id": ObjectId(id)}))
    return organizador

@router.post("/organizador")
async def post_organizador(organizador: Organizador):
    idOrganizador = collection_Organizadores.insert_one(dict(organizador)).inserted_id
    return {"message": "organizador criado com sucesso: " + str(idOrganizador)}

@router.put("/organizador/{id}")
async def put_organizador(id: str, organizador: Organizador):
    organizadorUpdate = collection_Organizadores.find_one_and_replace({"_id": ObjectId(id)}, dict(organizador))
    return {"message": "organizador atualizado com sucesso" + str(organizadorUpdate)}

@router.delete("/organizador/{id}")
async def delete_organizador(id: str):
    collection_Organizadores.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "deletado"}