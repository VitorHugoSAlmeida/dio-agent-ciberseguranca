"""Testes de regressão locais, sem servidor e sem tráfego externo."""
import unittest
from exemplos.app import autenticar, criar_banco_teste, criar_hash_senha, verificar_senha
from exemplos.app_vulneravel import construir_sql_inseguro


class TestLoginSeguranca(unittest.TestCase):
    def setUp(self):
        self.banco = criar_banco_teste()

    def tearDown(self):
        self.banco.close()

    def test_usuario_valido(self):
        self.assertTrue(autenticar(self.banco, "aluno", "senha-ficticia"))

    def test_senha_incorreta(self):
        self.assertFalse(autenticar(self.banco, "aluno", "outra"))

    def test_entrada_especial_nao_autentica(self):
        self.assertFalse(autenticar(self.banco, "' OR '1'='1", "x"))

    def test_invalido_permanece_invalido(self):
        self.assertFalse(autenticar(self.banco, "inexistente", "senha-ficticia"))

    def test_hash_com_salt(self):
        primeiro = criar_hash_senha("teste")
        segundo = criar_hash_senha("teste")
        self.assertNotEqual(primeiro, segundo)
        self.assertTrue(verificar_senha("teste", primeiro))
        self.assertFalse(verificar_senha("errado", primeiro))

    def test_codigo_inseguro_e_apenas_exemplo_estatico(self):
        texto = construir_sql_inseguro("aluno", "exemplo")
        self.assertIn("SELECT id FROM usuarios", texto)
        self.assertIn("aluno", texto)


if __name__ == "__main__":
    unittest.main()
