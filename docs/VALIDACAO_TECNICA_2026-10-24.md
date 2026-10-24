# Relatório de validação técnica — 2026-10-24

| Campo | Valor |
|---|---|
| ID | CPE-VAL-001 |
| Projeto | APP_COM_ESPECIALISTA |
| Repositório | https://github.com/carlos-andrade/APP_COM_ESPECIALISTA |
| Tipo documental | RELATORIO_VALIDACAO |
| Fase | FASE_1_IMPLEMENTACAO_MVP |
| Estado | EM_REVISAO |
| Versão | 1.0.0 |
| SHA-256 (conteúdo canónico) | 68c7c6639d7691aa90fe5c1ae54839837acc59bbd65502f669a6f9542fedd07e |
| Commit de referência (versão anterior) | N/A — documento novo |
| Data de criação | 2026-10-24 |
| Data de atualização | 2026-10-24 |
| Responsável | Proprietário do repositório |
| Aprovador | Pendente |
| Origem | Validação do ramo remediation/ci-postgres-tests |
| Autoridade superior | https://github.com/carlos-andrade/GOVERNANCA |
| Cadeia de autoridade | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| Rastreabilidade | PR #8; Issue #7; resultados de execução local |
| Escopo | Testes locais, sintaxe, OpenAPI, preparação PostgreSQL e gates pendentes |
| Objetivo | Separar evidências reproduzidas de verificações ainda não executadas |

## Evidências executadas localmente

- **Testes:** `12 passed` com pytest.
- **Compilação:** `python -m compileall -q app tests` passou.
- **OpenAPI:** parse YAML válido para OpenAPI 3.1.0; 16 paths.
- **Ambiente:** Python 3.13.5, FastAPI e Pydantic instalados localmente.
- **Código testado:** conteúdo de `app/main.py` e `tests/test_contracts.py` lido do ramo GitHub e executado numa cópia local. O clone direto do repositório falhou por indisponibilidade de DNS; por isso, não se declara que a suite foi executada por GitHub Actions.

## Cobertura de testes

1. Health endpoint público.
2. Autenticação obrigatória para catálogo.
3. Registo e listagem do catálogo.
4. Conflito de utilizador duplicado.
5. Triagem para software.
6. Isolamento de conversas entre utilizadores.
7. Limite de comprimento da mensagem.
8. Bootstrap administrativo de utilização única.
9. Exportação e eliminação de dados próprios.
10. Rejeição de token inválido.
11. Bloqueio de acesso administrativo para utilizador normal.
12. Aceitação explícita, estado pendente de curadoria e retirada da aceitação.

## Preparação PostgreSQL

Foram adicionados suporte de ligação através de `DATABASE_URL`, dependência psycopg, Dockerfile, Compose e esquema SQL inicial. A conexão PostgreSQL **não foi executada**: o ambiente não tem Docker, servidor PostgreSQL ou psycopg instalado. Não existe evidência de integração PostgreSQL, backup/restauro ou execução do Compose.

## Gates bloqueados

- CI GitHub Actions: a criação de `.github/workflows/ci.yml` foi bloqueada pela configuração de segurança do conector. Não existe run verde comprovada.
- Segurança: falta revisão independente de autenticação, gestão de tokens, bootstrap, rate limiting distribuído, abuso, logs, memória, retenção e eliminação.
- Privacidade: política final de retenção, localização, direitos dos titulares e condições do fornecedor carecem de decisão e validação.
- Contrato: o OpenAPI foi expandido e parseado, mas falta comparação automatizada integral com `/openapi.json` gerado pela aplicação.
- Cliente externo: exemplo de cliente existe, mas não houve chamada a API implantada nem integração num segundo repositório.
- Aprovação documental: versões alteradas permanecem `EM_REVISAO`; os hashes canónicos foram verificados, mas a aprovação formal destas novas versões não foi concedida.
- Piloto: **NÃO AUTORIZADO** até prova e encerramento de todos os gates anteriores.

## Conclusão

A validação local básica passou para os testes descritos, mas não é equivalente a CI verde, validação PostgreSQL, auditoria de segurança ou prontidão para produção. Este relatório não autoriza piloto.
