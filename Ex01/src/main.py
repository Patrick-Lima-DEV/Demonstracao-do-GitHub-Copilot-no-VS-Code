"""
main.py
Exemplo de uso do GitHub Copilot para automação simples em Python.
"""

# Função gerada com auxílio do Copilot: soma de dois números
def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

# Função gerada com auxílio do Copilot: validação de e-mail
import re
def validar_email(email):
    """Valida se o e-mail possui formato válido."""
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(padrao, email) is not None

# Exemplo de uso das funções
def exemplos():
    print("Exemplo de soma:", somar(2, 3))
    print("Validação de e-mail válido:", validar_email("teste@exemplo.com"))
    print("Validação de e-mail inválido:", validar_email("teste@exemplo"))

if __name__ == "__main__":
    exemplos()
