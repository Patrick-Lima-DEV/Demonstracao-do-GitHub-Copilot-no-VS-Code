from pydantic import BaseModel, Field
from typing import Optional

class BoletoRequest(BaseModel):
    codigo: str = Field(..., description="Linha digitável ou código de barras do boleto")

class BoletoStatusResponse(BaseModel):
    status: str
    mensagem: str
    dados: Optional[dict] = None
