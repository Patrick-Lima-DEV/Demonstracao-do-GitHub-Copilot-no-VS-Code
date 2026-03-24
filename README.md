# API de Validação de Boletos Bancários

Este projeto é uma API em Python (FastAPI) para validação de boletos bancários, pronta para deploy em Azure Functions ou como container.

## Funcionalidades
- Validação de linha digitável/código de barras
- Simulação de valor, vencimento e banco emissor
- Mensagens de erro claras
- Autenticação por API Key
- Estrutura pronta para produção e portfólio

## Endpoints

### POST /validar-boleto
Valida um boleto bancário.

**Headers:**
- `x-api-key`: sua API Key

**Body:**
```json
{
  "codigo": "23793381286008200009301000060104775890000002000"
}
```

**Resposta (válido):**
```json
{
  "status": "válido",
  "mensagem": "Boleto válido.",
  "dados": {
    "valor": 20.0,
    "vencimento": "2026-03-29",
    "banco": "Bradesco"
  }
}
```

**Resposta (inválido):**
```json
{
  "status": "inválido",
  "mensagem": "Banco emissor não reconhecido.",
  "dados": {
    "valor": 20.0,
    "vencimento": "2026-03-29",
    "banco": "Banco Desconhecido"
  }
}
```

### GET /status-boleto/{codigo}
Consulta o status de um boleto já validado.

**Headers:**
- `x-api-key`: sua API Key

**Resposta:**
```json
{
  "status": "válido",
  "mensagem": "Boleto válido.",
  "dados": {
    "valor": 20.0,
    "vencimento": "2026-03-29",
    "banco": "Bradesco"
  }
}
```

## Exemplos de uso

### Curl

**Boleto válido:**
```
curl -X POST "http://localhost:8000/validar-boleto" -H "Content-Type: application/json" -H "x-api-key: minha-api-key-supersegura" -d "{\"codigo\":\"23793381286008200009301000060104775890000002000\"}"
```

**Boleto inválido (formato):**
```
curl -X POST "http://localhost:8000/validar-boleto" -H "Content-Type: application/json" -H "x-api-key: minha-api-key-supersegura" -d "{\"codigo\":\"123abc\"}"
```

**Consulta status:**
```
curl -X GET "http://localhost:8000/status-boleto/23793381286008200009301000060104775890000002000" -H "x-api-key: minha-api-key-supersegura"
```

## Como rodar o projeto

1. Instale as dependências:
   ```bash
   pip install fastapi uvicorn
   ```
2. Execute a API:
   ```bash
   uvicorn main:app --reload
   ```
3. Acesse a documentação automática em: http://localhost:8000/docs

## Estrutura
- main.py
- services/validador.py
- models/boleto.py
- README.md

---

Pronto para deploy em Azure Functions ou Docker.
