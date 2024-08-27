from pydantic import BaseModel, Field
from typing import List, Optional


class PetModel(BaseModel):
    nome: str
    alergia: Optional[str] = None
    consultas_realizadas: List[str] = []
    especie: str
    idade: int = Field(..., gt=0)
    procedimentos_realizados: List[str] = []
    raca: str
    receitas_anteriores: List[str] = []
    sexo: str