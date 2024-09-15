from datetime import datetime

def unicoParticipante(participante) -> dict:
    return {
        "id": str(participante["_id"]),
        "nome": participante["nome"],
        "email": participante["email"],
        "createdAt": participante["createdAt"].isoformat() if isinstance(participante["createdAt"], datetime) else participante["createdAt"],
        "modifiedAt": participante["modifiedAt"].isoformat() if isinstance(participante["modifiedAt"], datetime) else participante["modifiedAt"]
    }


def listaParticipantes(participantes) -> list:
    return [unicoParticipante(participante) for participante in participantes]