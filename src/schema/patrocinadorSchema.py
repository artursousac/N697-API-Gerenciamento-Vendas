from datetime import datetime

def unicoPatrocinador(patrocinador) -> dict:
    return {
        "id": str(patrocinador["_id"]),
        "nome": patrocinador["nome"],
        "email": patrocinador["email"],
        "createdAt": patrocinador["createdAt"].isoformat() if isinstance(patrocinador["createdAt"], datetime) else patrocinador["createdAt"],
        "modifiedAt": patrocinador["modifiedAt"].isoformat() if isinstance(patrocinador["modifiedAt"], datetime) else patrocinador["modifiedAt"]
    }


def listaPatrocinadores(patrocinadores) -> list:
    return [unicoPatrocinador(patrocinador) for patrocinador in patrocinadores]