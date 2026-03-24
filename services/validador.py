import re
from datetime import datetime, timedelta
from typing import Tuple, Dict

class BoletoValidator:
    @staticmethod
    def validar_codigo(codigo: str) -> Tuple[bool, str]:
        if not codigo.isdigit():
            return False, "O código deve conter apenas números."
        if len(codigo) not in [47, 48, 44]:
            return False, "O código deve ter 44, 47 ou 48 dígitos."
        return True, "Formato válido."

    @staticmethod
    def simular_dados_boleto(codigo: str) -> Dict:
        # Simulação de extração de dados
        valor = round(100 + (int(codigo[-4:]) % 9000) / 100, 2)
        dias = int(codigo[-6:-4]) if len(codigo) >= 6 else 5
        vencimento = (datetime.now() + timedelta(days=dias)).strftime('%Y-%m-%d')
        banco = {
            '001': 'Banco do Brasil',
            '237': 'Bradesco',
            '341': 'Itaú',
            '104': 'Caixa Econômica',
            '033': 'Santander',
        }.get(codigo[:3], 'Banco Desconhecido')
        return {
            'valor': valor,
            'vencimento': vencimento,
            'banco': banco
        }

    @staticmethod
    def validar_boleto(codigo: str) -> Tuple[bool, str, Dict]:
        valido, msg = BoletoValidator.validar_codigo(codigo)
        if not valido:
            return False, msg, {}
        dados = BoletoValidator.simular_dados_boleto(codigo)
        # Simulação de regras adicionais
        if dados['valor'] <= 0:
            return False, "Valor do boleto inválido.", dados
        try:
            datetime.strptime(dados['vencimento'], '%Y-%m-%d')
        except Exception:
            return False, "Data de vencimento inválida.", dados
        if dados['banco'] == 'Banco Desconhecido':
            return False, "Banco emissor não reconhecido.", dados
        return True, "Boleto válido.", dados
