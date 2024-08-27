from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date as dt

class TutorModel(BaseModel):
    nome: str
    pets: List[str] = []
    data_nascimento: dt
    email: str
    endereco: str
    sexo: str

