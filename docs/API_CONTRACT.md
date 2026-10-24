# Contrato da API — APP_COM_ESPECIALISTA

| Campo | Valor |
|---|---|
| ID | CPE-API-001 |
| Projeto | APP_COM_ESPECIALISTA |
| Repositório | https://github.com/carlos-andrade/APP_COM_ESPECIALISTA |
| Tipo documental | CONTRATO_API |
| Fase | FASE_1_IMPLEMENTACAO_MVP |
| Estado | EM_REVISAO |
| Versão | 1.0.0 |
| SHA-256 (conteúdo canónico) | PENDENTE_DE_VALIDACAO |
| Commit de referência (versão anterior) | N/A — documento novo |
| Data de criação | 2026-10-24 |
| Data de atualização | 2026-10-24 |
| Responsável | Proprietário do repositório |
| Aprovador | Pendente |
| Origem | Arquitetura proposta CPE-ARQ-001 |
| Autoridade superior | https://github.com/carlos-andrade/GOVERNANCA |
| Cadeia de autoridade | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| Rastreabilidade | openapi.yaml, app/main.py e testes |
| Escopo | Endpoints v1 do MVP |
| Objetivo | Contrato estável para clientes externos |

## Base e autenticação

Base path: /api/v1. Autenticação por Authorization: Bearer JWT, exceto health, registo e obtenção de token. Autorização é verificada no servidor em cada recurso. IDs não substituem verificação de propriedade. O serviço devolve X-Request-ID. Não colocar credenciais em query strings.

## Endpoints

| Método | Caminho | Finalidade |
|---|---|---|
| POST | /auth/register | Criar conta |
| POST | /auth/token | Obter token |
| GET | /specialists | Listar/pesquisar catálogo |
| GET | /specialists/{id} | Consultar especialista |
| POST | /triage | Triagem |
| POST | /conversations | Criar conversa |
| GET | /conversations | Listar conversas próprias |
| GET | /conversations/{id} | Consultar conversa própria |
| POST | /conversations/{id}/messages | Enviar mensagem |
| POST | /feedback | Registar aceitação/rejeição |
| GET | /me/export | Exportar dados próprios |
| DELETE | /me | Eliminar conta |
| GET | /admin/memory | Consultar itens pendentes (admin) |
| POST | /admin/memory/{id}/review | Rever item (admin) |
| GET | /admin/audit | Consultar auditoria (admin) |

## Erros e limites

401: AUTH_REQUIRED, AUTH_INVALID_TOKEN, AUTH_INVALID_CREDENTIALS. 403: AUTH_FORBIDDEN. 404: SPECIALIST_NOT_FOUND, CONVERSATION_NOT_FOUND, MESSAGE_NOT_FOUND. 409: USER_EXISTS. 422: validação. 429: RATE_LIMITED com Retry-After. 502: AI_PROVIDER_ERROR. 503: AI_PROVIDER_NOT_CONFIGURED. Respostas incluem código e mensagem segura.

Mensagem até 8.000 caracteres; contexto até 20 mensagens; rate limit inicial 60/minuto/IP; timeout do fornecedor 30 segundos. O limitador em memória é apenas barreira de desenvolvimento e deve ser substituído por limitador partilhado antes de execução multi-instância.

## Compatibilidade

OpenAPI disponível em /openapi.json e versionado em openapi.yaml. Mudanças aditivas compatíveis podem permanecer em v1. Mudanças incompatíveis exigem nova versão principal. Cada PR executa testes de contrato, autenticação, isolamento e validação. Cliente externo deve consumir apenas o contrato público.

## Limites do MVP

Não aprovado para produção. SQLite, ausência de verificação de email, gestão simplificada de JWT, curadoria administrativa inicial e política provisória de retenção exigem revisão antes do piloto.


## PostgreSQL

A implementação suporta a variável `DATABASE_URL` e o compose de desenvolvimento. A implantação de referência usa PostgreSQL; o SQLite fica reservado a testes locais. A compatibilidade real deve ser comprovada por testes de integração contra PostgreSQL antes de declarar o contrato estável.
