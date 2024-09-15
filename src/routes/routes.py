from fastapi import APIRouter, Query
from bson import ObjectId
from src.model.models import *
from src.database.database import *
from src.schema.eventoSchema import *
from src.schema.organizadorSchema import *
from src.schema.participanteSchema import *
from src.schema.patrocinadorSchema import *
from src.schema.localSchema import *

router = APIRouter()

@router.get("/")
async def RotaInicial():
    return {"message": "bem-vindo à primeira rota do projeto"}

@router.get("/eventos")
async def get_eventos(inicio: int = Query(0), fim: int = None):
    totalEventos = collection_Eventos.count_documents({})
    if fim is None:
        fim = totalEventos
    limit = fim+1 - inicio
    eventosCursor = listaEventos(collection_Eventos.find().skip(inicio).limit(limit))
    eventos = list(eventosCursor)
    return eventos

@router.get("/evento/{id}")
async def get_evento(id):
    evento = unicoEvento(collection_Eventos.find_one({"_id": ObjectId(id)}))
    return evento

@router.post("/evento")
async def post_evento(evento: Evento):
    idEvento = collection_Eventos.insert_one(dict(evento)).inserted_id
    return {"message": "evento criado com sucesso: "+str(idEvento)}

@router.put("/evento/{id}")
async def put_evento(id: str, evento: Evento):
    eventoUpdate = collection_Eventos.find_one_and_replace({"_id": ObjectId(id)}, dict(evento))
    return {"message": "evento atualizado com sucesso" + str(eventoUpdate)}

@router.delete("/evento/{id}")
async def delete_evento(id: str):
    collection_Eventos.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "deletado"}

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


@router.get("/participantes")
async def get_participantes(inicio: int = Query(0), fim: int = None):
    """participantes = listaParticipantes(collection_Participantes.find())"""
    totalParticipantes = collection_Participantes.count_documents({})
    if fim is None:
        fim = totalParticipantes
    limit = fim+1 - inicio
    participantesCursor = listaParticipantes(collection_Participantes.find().skip(inicio).limit(limit))
    participantes = list(participantesCursor)
    return participantes

@router.get("/participante/{id}")
async def get_participante(id):
    participante = unicoParticipante(collection_Participantes.find_one({"_id": ObjectId(id)}))
    return participante

@router.post("/participante")
async def post_participante(participante: Participante):
    idParticipante = collection_Participantes.insert_one(dict(participante)).inserted_id
    return {"message": "participante criado com sucesso: " + str(idParticipante)}

@router.put("/participante/{id}")
async def put_participante(id: str, participante: Participante):
    participanteUpdate = collection_Participantes.find_one_and_replace({"_id": ObjectId(id)}, dict(participante))
    return {"message": "participante atualizado com sucesso" + str(participanteUpdate)}

@router.delete("/participante/{id}")
async def delete_participante(id: str):
    collection_Participantes.find_one_and_delete({"_id": ObjectId(id)})
    return {"message":"deletado"}

@router.get("/patrocinadores")
async def get_patrocinadores(inicio: int = Query(0), fim: int = None):
    """patrocinadores = listaPatrocinadores(collection_Patrocinadores.find())"""
    totalPatrocinadores = collection_Patrocinadores.count_documents({})
    if fim is None:
        fim = totalPatrocinadores
    limit = fim+1 - inicio
    patrocinadoresCursor = listaOrganizadores(collection_Patrocinadores.find().skip(inicio).limit(limit))
    patrocinadores = list(patrocinadoresCursor)
    return patrocinadores

@router.get("/patrocinador/{id}")
async def get_patrocinador(id):
    patrocinador = unicoPatrocinador(collection_Patrocinadores.find_one({"_id": ObjectId(id)}))
    return patrocinador

@router.post("/patrocinador")
async def post_patrocinador(patrocinador: Patrocinador):
    idPatrocinador = collection_Patrocinadores.insert_one(dict(patrocinador)).inserted_id
    return {"message": "patrocinador criado com sucesso: " + str(idPatrocinador)}

@router.get("/locais")
async def get_locais(inicio: int = Query(0), fim: int = None):
    """locais = listaLocais(collection_Locais.find())"""
    totalLocais = collection_Locais.count_documents({})
    if fim is None:
        fim = totalLocais
    limit = fim+1 - inicio
    locaisCursor = listaLocais(collection_Locais.find().skip(inicio).limit(limit))
    locais = list(locaisCursor)
    return locais

@router.get("/local/{id}")
async def get_local(id):
    local = unicoLocal(collection_Locais.find_one({"_id": ObjectId(id)}))
    return local

@router.post("/local")
async def post_local(local: Local):
    idLocal = collection_Locais.insert_one(dict(local)).inserted_id
    return {"message": "local criado com sucesso: " + str(idLocal)}

@router.put("/local/{id}")
async def put_local(id: str, local: Local):
    localUpdate = collection_Locais.find_one_and_replace({"_id": ObjectId(id)}, dict(local))
    return {"message": "local atualizado com sucesso" + str(localUpdate)}
    
@router.delete("/local/{id}")
async def delete_local(id: str):
    collection_Locais.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "deletado"}            