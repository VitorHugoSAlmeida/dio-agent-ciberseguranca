"""Exemplo deliberadamente inseguro para REVISÃO ESTÁTICA de AppSec.

Não executar com dados reais. Esta função apenas monta o texto de uma consulta.
"""

def construir_sql_inseguro(usuario: str, senha: str) -> str:
    return (
        "SELECT id FROM usuarios WHERE usuario = '"
        + usuario
        + "' AND senha = '"
        + senha
        + "'"
    )
