from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

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

