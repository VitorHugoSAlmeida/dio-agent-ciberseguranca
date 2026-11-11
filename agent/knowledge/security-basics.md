# Conhecimento básico de cibersegurança — AppSec

## Termos essenciais

- **Vulnerabilidade:** fraqueza em um sistema, processo ou configuração que pode permitir uma consequência indesejada.
- **Ameaça:** evento, ator ou capacidade que pode explorar uma fraqueza e provocar dano.
- **Risco:** possibilidade e consequência de um incidente, analisadas segundo o contexto do sistema.
- **Ataque:** ação que busca violar um objetivo de segurança; a existência de uma vulnerabilidade não comprova que houve ataque.

## Tríade CIA

1. **Confidencialidade:** impedir divulgação indevida de dados.
2. **Integridade:** impedir modificações não autorizadas.
3. **Disponibilidade:** manter serviços e dados acessíveis quando necessários.

## Risco qualitativo

Para fins educativos: classifique impacto e probabilidade em baixo, médio ou alto, sempre justificando. A severidade resulta do cenário observado, dos controles existentes, da exposição e do valor do ativo. Uma classificação qualitativa não substitui CVSS nem uma avaliação formal.

## SQL Injection e prevenção

A aplicação é vulnerável quando trata dados não confiáveis como parte da sintaxe de uma consulta SQL. A defesa principal consiste em instruções parametrizadas: `SELECT ... WHERE usuario = ?` e passagem separada dos valores. Também aplique privilégio mínimo, autenticação correta, testes de regressão, logs sem dados sensíveis e tratamento de erros.

Para armazenamento de senhas em sistemas reais, use algoritmos dedicados com salt como Argon2id, scrypt ou bcrypt. Evite SHA-256 puro.

## Boas práticas de defesa

Atualização de dependências, MFA quando aplicável, backup verificado, segmentação, menor privilégio, revisão de alterações, CI com testes, monitoramento responsável, sandboxing e conscientização contra phishing.

## MITRE ATT&CK

[T1190 — Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) descreve exploração de aplicação exposta publicamente. Uma falha de SQL Injection num aplicativo SQLite local não demonstra, sozinha, o emprego dessa técnica.

## Fontes

- https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
- https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
- https://docs.python.org/3/library/sqlite3.html
- https://attack.mitre.org/techniques/T1190/
