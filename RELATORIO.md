# Relatório de análise de vulnerabilidade — laboratório SQLite

> **Natureza:** exercício educacional com código fictício; achado de revisão estática, não resultado de ataque real.

## Contexto e autorização

Projeto Python de laboratório, banco SQLite em memória e usuários fictícios. Nenhum alvo externo.

## Evidência localizada

Em `exemplos/app_vulneravel.py`, a função `construir_sql_inseguro()` monta uma string SQL por concatenação dos valores `usuario` e `senha`. Isso mistura dados de entrada com texto da instrução SQL, o que configura o padrão de código associado ao SQL Injection.

## Impacto potencial na tríade CIA

- **Confidencialidade:** possíveis consultas não autorizadas se uma aplicação de produção executar SQL equivalente.
- **Integridade:** possíveis alterações indevidas em sistemas com permissões excessivas.
- **Disponibilidade:** possibilidade de perturbação do serviço, conforme o contexto.

## Classificação qualitativa

- **Probabilidade (hipotética): média**, pois depende da exposição, permissões e controles de uma aplicação real.
- **Impacto potencial: alto** caso seja um login de produção exposto com dados sensíveis.
- **Severidade estimada: alta para o cenário hipotético de produção**, não aplicável automaticamente ao laboratório. Não corresponde a uma nota CVSS.

## Correção

Em `exemplos/app.py`, a consulta usa o marcador `?` e uma tupla separada com o nome do usuário. A verificação de senha acontece fora do SQL, usando `scrypt` com salt aleatório e comparação resistente a timing.

## Validação

Execute `python -m unittest discover -s testes -v`. Os testes abrangem autenticação válida, credenciais inválidas, entrada especial, usuário inexistente, geração/validação de hash e identificação estática do código inseguro. A configuração de GitHub Actions repete a suíte em cada atualização.

## Referências

- OWASP: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
- MITRE ATT&CK T1190: https://attack.mitre.org/techniques/T1190/

**Limitações:** o Hermes não foi executado nesta interação; a comprovação visual do comportamento do agente exige sessão real em um harness. A associação com T1190 exige contexto de aplicação publicamente exposta.
