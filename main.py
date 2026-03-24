from fastapi import FastAPI, HTTPException, Header, status
from fastapi.responses import JSONResponse
from models.boleto import BoletoRequest, BoletoStatusResponse
from services.validador import BoletoValidator
import logging

app = FastAPI(title="API de Validação de Boletos")

# Simples API Key para autenticação
API_KEY = "minha-api-key-supersegura"

# Simulação de armazenamento de status
status_boletos = {}

logging.basicConfig(level=logging.INFO)

# Middleware de autenticação
async def verificar_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API Key inválida.")

@app.post("/validar-boleto", response_model=BoletoStatusResponse)
async def validar_boleto(request: BoletoRequest, x_api_key: str = Header(...)):
    await verificar_api_key(x_api_key)
    logging.info(f"Recebida requisição para validar boleto: {request.codigo}")
    valido, mensagem, dados = BoletoValidator.validar_boleto(request.codigo)
    status_boleto = "válido" if valido else "inválido"
    status_boletos[request.codigo] = {"status": status_boleto, "mensagem": mensagem, "dados": dados}
    if not valido:
        return JSONResponse(status_code=400, content={"status": status_boleto, "mensagem": mensagem, "dados": dados})
    return {"status": status_boleto, "mensagem": mensagem, "dados": dados}

@app.get("/status-boleto/{codigo}", response_model=BoletoStatusResponse)
async def status_boleto(codigo: str, x_api_key: str = Header(...)):
    await verificar_api_key(x_api_key)
    logging.info(f"Consulta de status do boleto: {codigo}")
    info = status_boletos.get(codigo)
    if not info:
        raise HTTPException(status_code=404, detail="Boleto não encontrado.")
    return info
