"""
test_main.py
Testes automatizados para as funções do main.py
"""
import unittest
from main import somar, validar_email

class TestMain(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(0, 0), 0)

    def test_validar_email(self):
        self.assertTrue(validar_email("teste@exemplo.com"))
        self.assertFalse(validar_email("teste@exemplo"))
        self.assertFalse(validar_email("@exemplo.com"))
        self.assertFalse(validar_email("teste@.com"))

if __name__ == "__main__":
    unittest.main()
