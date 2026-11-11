# DIO Agent — Mentor de Cibersegurança (AppSec)

> Especialização educacional do [DIO Agent original](https://github.com/digitalinnovationone/dio-agent), preservando suas **6 skills originais** e acrescentando a skill **vulnerability-analysis**.

## Por que esta especialização?

O projeto transforma o agente em um mentor defensivo de segurança de aplicações. Antes de sugerir ferramentas ou comandos, ele solicita o contexto do sistema, autorização e escopo. A partir das evidências, avalia **impacto, probabilidade e severidade**, orienta mitigação e sugere como comprovar a correção.

**O que foi melhorado:** o agente utiliza sempre um relatório estruturado de risco para permitir comparar análises em diferentes cenários. Nenhum modelo foi treinado: a especialização é feita apenas por arquivos Markdown.

## O que foi alterado

| Arquivo | Função |
|---|---|
| [`skills/vulnerability-analysis/SKILL.md`](skills/vulnerability-analysis/SKILL.md) | Processo defensivo com perguntas, avaliação de risco, correção e validação |
| [`skills/vulnerability-analysis/README.md`](skills/vulnerability-analysis/README.md) | Explicação de uso da skill |
| [`agent/knowledge/security-basics.md`](agent/knowledge/security-basics.md) | Conceitos, tríade CIA, recomendações e fontes |
| [`agent/persona.md`](agent/persona.md) | Persona com comportamento de mentor AppSec |
| [`AGENTS.md`](AGENTS.md) | Nova linha na tabela de skills e referência ao conhecimento |
| [`exemplos/app_vulneravel.py`](exemplos/app_vulneravel.py) | Código de login com SQL concatenado (para revisão estática, não produção) |
| [`exemplos/app.py`](exemplos/app.py) | Versão corrigida com SQLite e parâmetros |
| [`testes/test_app.py`](testes/test_app.py) | Testes de validação locais |
| [`RELATORIO.md`](RELATORIO.md) | Exemplo de relatório de vulnerabilidade |
| [`.github/workflows/testes.yml`](.github/workflows/testes.yml) | Execução automatizada dos testes no GitHub Actions |

## Como usar o agente

1. Abra o repositório em um harness que leia `AGENTS.md`. No **Hermes**, siga a [documentação oficial](https://hermes-agent.nousresearch.com/docs) para instalação.
2. Abra um terminal **dentro da pasta do projeto** e execute `hermes` após instalar e configurar o harness.
3. Envie ao agente: **“Quero analisar a segurança do meu login SQLite de laboratório. Antes de recomendar comandos, pergunte sobre autorização, escopo e criticidade. Compare exemplos/app_vulneravel.py com exemplos/app.py.”**
4. Observe se ele pede o contexto antes de agir e se produz a avaliação padronizada.

**Observação:** a interação com o Hermes depende de execução pelo usuário no próprio ambiente. Este repositório documenta o roteiro; não afirma que o Hermes foi executado neste chat.

## Testar o exemplo em Python

Requer Python 3.10+; usa somente bibliotecas padrão.

```bash
python -m unittest discover -s testes -v
python -m exemplos.app
```

Os testes verificam login válido, senha incorreta, entrada especial tratada como dado e a ausência de concatenação na consulta corrigida. A execução automática está configurada em **Actions → Testes de segurança**.

## Exemplo: risco de SQL Injection

- **Antes:** SQL construído pela concatenação de dados fornecidos na entrada.
- **Depois:** a consulta usa `?` (placeholders) e tupla de parâmetros. A senha fictícia é verificada com hash derivado por `scrypt`, sem inserir a senha na consulta SQL.
- **Risco ilustrativo:** impacto alto para um login exposto com dados sensíveis; classificação depende da análise real do contexto.
- **MITRE ATT&CK:** [T1190](https://attack.mitre.org/techniques/T1190/) somente quando se tratar de exploração de aplicação pública, e não automaticamente para qualquer SQL Injection local.

Leia o [relatório de análise](RELATORIO.md) para ver as justificativas.

## Evidências e prints

Para evitar evidências fabricadas, não foram anexados prints atribuídos a uma execução do Hermes. **O GitHub Actions fornece uma validação reproduzível** dos testes, e a pasta [`images/`](images/README.md) orienta como adicionar capturas reais do VS Code e de perguntas do agente após a execução local.

## Uso ético

Somente arquivos fictícios e testes locais ou sistemas próprios/autorizados. Não realize ataques contra sistemas de terceiros. **Projeto para aprendizagem, não auditoria profissional concluída.**

## Referências

- [DIO Agent oficial](https://github.com/digitalinnovationone/dio-agent)
- [OWASP: SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [Python sqlite3](https://docs.python.org/3/library/sqlite3.html)
