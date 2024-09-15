from datetime import datetime

def unicoEvento(evento) -> dict:
    return {
        "id": str(evento["_id"]),
        "nome": evento["nome"],
        "data": evento["data"].isoformat() if isinstance(evento["data"], datetime) else evento["data"],
        "local": evento["local"],
        "participantes": evento["participantes"],
        "organizador": evento["organizador"],
        "patrocinador": evento["patrocinador"],
        "createdAt": evento["createdAt"].isoformat() if isinstance(evento["createdAt"], datetime) else evento["createdAt"],
        "modifiedAt": evento["modifiedAt"].isoformat() if isinstance(evento["modifiedAt"], datetime) else evento["modifiedAt"]
    }


def listaEventos(eventos) -> list:
    return [unicoEvento(evento) for evento in eventos]