from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List


class Evento(BaseModel):
    nome: str
    data: datetime
    local: str
    participantes: List[str] = None
    organizador: str
    patrocinador: str
    createdAt: Optional[datetime] = Field(default_factory=datetime.utcnow)
    modifiedAt: Optional[datetime] = Field(default_factory=datetime.utcnow)

class Organizador(BaseModel):
    nome: str
    email: str
    createdAt: Optional[datetime] = Field(default_factory=datetime.utcnow)
    modifiedAt: Optional[datetime] = Field(default_factory=datetime.utcnow)

class Participante(BaseModel):
    nome: str
    email: str
    createdAt: Optional[datetime] = Field(default_factory=datetime.utcnow)
    modifiedAt: Optional[datetime] = Field(default_factory=datetime.utcnow)

class Patrocinador(BaseModel):
    nome: str
    email: str
    createdAt: Optional[datetime] = Field(default_factory=datetime.utcnow)
    modifiedAt: Optional[datetime] = Field(default_factory=datetime.utcnow)

class Local(BaseModel):
    nome: str
    endereco: str
    createdAt: Optional[datetime] = Field(default_factory=datetime.utcnow)
    modifiedAt: Optional[datetime] = Field(default_factory=datetime.utcnow)

