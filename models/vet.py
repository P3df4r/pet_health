from pydantic import BaseModel, Field
from typing import List, Optional


class VetModel(BaseModel):
    nome: str
    idade: int = Field(..., gt=0)
    procedimentos_realizados: List[str] = []