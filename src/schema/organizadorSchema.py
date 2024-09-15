from datetime import datetime

def unicoOrganizador(organizador) -> dict:
    return {
        "id": str(organizador["_id"]),
        "nome": organizador["nome"],
        "email": organizador["email"],
        "createdAt": organizador["createdAt"].isoformat() if isinstance(organizador["createdAt"], datetime) else organizador["createdAt"],
        "modifiedAt": organizador["modifiedAt"].isoformat() if isinstance(organizador["modifiedAt"], datetime) else organizador["modifiedAt"]
    }


def listaOrganizadores(organizadores) -> list:
    return [unicoOrganizador(organizador) for organizador in organizadores]
    