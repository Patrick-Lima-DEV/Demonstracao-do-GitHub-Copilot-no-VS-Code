# 🤖 Demonstração do GitHub Copilot no VS Code

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)](https://fastapi.tiangolo.com/)
[![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-Enabled-orange.svg)](https://github.com/features/copilot)

## 📌 Sobre o Projeto

Projeto didático e pronto para portfólio, demonstrando o uso prático do **GitHub Copilot** para acelerar o desenvolvimento em Python no Visual Studio Code. Inclui exemplos reais, testes automatizados, uma API simples e guia completo de configuração.

## 🎯 Objetivos

✅ Demonstrar a produtividade com GitHub Copilot  
✅ Apresentar boas práticas de código assistido por IA  
✅ Estrutura profissional pronta para portfólio  
✅ Exemplos didáticos e funcionais  

## 🚀 Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal
- **Visual Studio Code** - Editor
- **GitHub Copilot** - Assistente de IA para programação
- **FastAPI** - Framework para API Web
- **unittest** - Testes automatizados

## 📂 Estrutura do Projeto

```
Demonstracao-do-GitHub-Copilot-no-VS-Code/
├── Ex01/
│   ├── src/
│   │   ├── main.py           # Exemplos básicos com Copilot
│   │   ├── test_main.py      # Testes automatizados
│   │   └── api.py            # API FastAPI
│   ├── README.md             # Documentação detalhada
│   └── .gitignore
├── README.md                 # Este arquivo
└── .git/
```

## ⚙️ Configuração Rápida

### 1. Pré-requisitos
- Python 3.8+
- Visual Studio Code
- Conta GitHub (para usar GitHub Copilot)

### 2. Instalação do GitHub Copilot

1. Abra o VS Code
2. Vá em **Extensões** (Ctrl+Shift+X)
3. Busque por **"GitHub Copilot"**
4. Clique em **Instalar**
5. Faça **login com sua conta GitHub**

### 3. Clone e Acesse o Projeto

```bash
git clone https://github.com/Patrick-Lima-DEV/Demonstracao-do-GitHub-Copilot-no-VS-Code.git
cd Demonstracao-do-GitHub-Copilot-no-VS-Code/Ex01
```

## 🤖 Como Usar o GitHub Copilot

### Sugestões Automáticas
- Comece digitando um **comentário descritivo**
- O Copilot sugere automaticamente o código
- Aceite com **Tab** ou **Enter**

### Exemplo Prático

```python
# Função para validar e-mail
def validar_email(email):
    # O Copilot sugere a implementação automaticamente!
```

### Atalhos Úteis
- `Ctrl+Enter` - Ver sugestões alternativas
- `Escape` - Rejeitar sugestão
- `Tab` - Aceitar sugestão

## 📚 Exemplos de Código

### main.py - Funções Básicas
```python
def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def validar_email(email):
    """Valida se o e-mail possui formato válido."""
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(padrao, email) is not None
```

### test_main.py - Testes Automatizados
```bash
python -m pytest src/test_main.py
# ou
python -m unittest src.test_main
```

### api.py - API FastAPI
```bash
pip install fastapi uvicorn
uvicorn src.api:app --reload
# Acesse: http://localhost:8000/docs
```

## 💡 Insights e Aprendizados

### ✨ Vantagens do Copilot
- ⚡ Acelera o desenvolvimento em até 40%
- 📚 Sugere soluções baseadas em padrões consolidados
- 💻 Reduz tempo em tarefas repetitivas
- 🎓 Ferramenta excelente para aprendizado

### ⚠️ Cuidados Importantes
- ❌ **Não confie cegamente** nas sugestões
- 🔍 **Sempre revise** o código gerado
- ✅ **Teste** antes de usar em produção
- 📖 **Entenda** o que o código faz
- 🔐 **Proteja** dados sensíveis no chat

### 🎯 Boas Práticas
- Escreva **comentários claros e descritivos**
- Use **nomes de variáveis significativos**
- Mantenha **contexto organizado**
- Faça **refatoração regularmente**
- Documente **decisões importantes**

## 🔮 Possíveis Melhorias

- [ ] Adicionar autenticação JWT
- [ ] Expandir cobertura de testes
- [ ] Criar documentação automaticamente
- [ ] Integrar com CI/CD (GitHub Actions)
- [ ] Deploy em Azure Functions
- [ ] Exemplos com mais linguagens

## 📷 Prints de Demonstração

> **Dica:** Adicione prints mostrando:
> - Sugestões do Copilot em tempo real
> - Autocompletar de funções
> - Testes sendo executados
> - API rodando localmente

## 🚀 Deploy

### Local
```bash
pip install requirements.txt
uvicorn src.api:app --reload
```

### Docker (Exemplo)
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0"]
```

## 📖 Recursos Úteis

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Python Documentation](https://docs.python.org/3/)
- [VS Code Tips & Tricks](https://code.visualstudio.com/docs/introvideos/tips-and-tricks)

## 👨‍💻 Autor

**Patrick Lima**  
🔗 GitHub: [@Patrick-Lima-DEV](https://github.com/Patrick-Lima-DEV)

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## ⭐ Contribuições

Se encontrou algo útil, considere dar uma ⭐ no repositório!

---

**Desenvolvido com ❤️ e assistido por 🤖 GitHub Copilot**
