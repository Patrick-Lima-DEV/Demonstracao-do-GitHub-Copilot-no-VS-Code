"""
api.py
Exemplo de API simples usando FastAPI, com funções geradas com auxílio do Copilot.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SomaRequest(BaseModel):
    a: int
    b: int

class EmailRequest(BaseModel):
    email: str

@app.get("/")
def home():
    return {"mensagem": "API FastAPI rodando!"}

@app.post("/somar")
def somar_endpoint(req: SomaRequest):
    """Endpoint para somar dois números."""
    return {"resultado": req.a + req.b}

@app.post("/validar-email")
def validar_email_endpoint(req: EmailRequest):
    """Endpoint para validar e-mail."""
    import re
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    valido = re.match(padrao, req.email) is not None
    return {"valido": valido}

# Para rodar: uvicorn src.api:app --reload
