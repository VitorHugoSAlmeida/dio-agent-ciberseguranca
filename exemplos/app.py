"""Login SQLite fictício que mantém a entrada separada da consulta SQL."""

import hashlib
import hmac
import secrets
import sqlite3


def criar_hash_senha(senha: str) -> str:
    """Exemplo com scrypt + salt aleatório (exige Python com suporte a scrypt)."""
    salt = secrets.token_bytes(16)
    derivado = hashlib.scrypt(senha.encode("utf-8"), salt=salt, n=2**14, r=8, p=1)
    return f"{salt.hex()}:{derivado.hex()}"


def verificar_senha(senha: str, senha_armazenada: str) -> bool:
    try:
        salt_hex, hash_hex = senha_armazenada.split(":", 1)
        salt = bytes.fromhex(salt_hex)
        esperado = bytes.fromhex(hash_hex)
        encontrado = hashlib.scrypt(senha.encode("utf-8"), salt=salt, n=2**14, r=8, p=1)
        return hmac.compare_digest(encontrado, esperado)
    except (ValueError, TypeError):
        return False


def criar_banco_teste() -> sqlite3.Connection:
    """Banco exclusivamente em memória: sem dados reais ou arquivos persistentes."""
    banco = sqlite3.connect(":memory:")
    banco.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, usuario TEXT UNIQUE, senha_hash TEXT NOT NULL)")
    banco.execute(
        "INSERT INTO usuarios (usuario, senha_hash) VALUES (?, ?)",
        ("aluno", criar_hash_senha("senha-ficticia")),
    )
    return banco


def autenticar(banco: sqlite3.Connection, usuario: str, senha: str) -> bool:
    linha = banco.execute(
        "SELECT senha_hash FROM usuarios WHERE usuario = ?",
        (usuario,),
    ).fetchone()
    return bool(linha and verificar_senha(senha, linha[0]))


if __name__ == "__main__":
    banco = criar_banco_teste()
    try:
        print("Login fictício aprovado:", autenticar(banco, "aluno", "senha-ficticia"))
    finally:
        banco.close()
