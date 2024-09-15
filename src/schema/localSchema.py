from datetime import datetime

def unicoLocal(local) -> dict:
    return {
        "id": str(local["_id"]),
        "nome": local["nome"],
        "endereco": local["endereco"],
        "createdAt": local["createdAt"].isoformat() if isinstance(local["createdAt"], datetime) else local["createdAt"],
        "modifiedAt": local["modifiedAt"].isoformat() if isinstance(local["modifiedAt"], datetime) else local["modifiedAt"]
    }


def listaLocais(locais) -> list:
    return [unicoLocal(local) for local in locais]