# Execução local e integração de cliente

| Campo | Valor |
|---|---|
| ID | CPE-RUN-001 |
| Projeto | APP_COM_ESPECIALISTA |
| Repositório | https://github.com/carlos-andrade/APP_COM_ESPECIALISTA |
| Tipo documental | RUNBOOK |
| Fase | FASE_1_IMPLEMENTACAO_MVP |
| Estado | EM_REVISAO |
| Versão | 1.0.0 |
| SHA-256 (conteúdo canónico) | PENDENTE_DE_VALIDACAO |
| Commit de referência (versão anterior) | N/A — documento novo |
| Data de criação | 2026-10-24 |
| Data de atualização | 2026-10-24 |
| Responsável | Proprietário do repositório |
| Aprovador | Pendente |
| Origem | Implementação inicial do MVP |
| Autoridade superior | https://github.com/carlos-andrade/GOVERNANCA |
| Cadeia de autoridade | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| Rastreabilidade | app/main.py, requirements.txt, examples/client_python |
| Escopo | Execução de desenvolvimento e cliente externo |
| Objetivo | Permitir instalação local reproduzível |

## Requisitos

Python 3.12 ou superior. Para conversas reais, uma chave válida do fornecedor de IA. Não usar SQLite em produção multi-instância.

## Instalação

1. Criar e ativar um ambiente virtual Python.
2. Instalar dependências com pip install -r requirements.txt.
3. Definir CPE_JWT_SECRET com valor aleatório de pelo menos 32 bytes.
4. Definir CPE_DB_PATH para uma localização gravável.
5. Definir CPE_ADMIN_EMAIL antes de registar a conta administrativa inicial. Só o email configurado recebe o papel admin.
6. Para conversas, definir OPENAI_API_KEY e, se necessário, CPE_OPENAI_MODEL.
7. Executar uvicorn app.main:app --host 127.0.0.1 --port 8000.
8. Consultar /docs, /openapi.json e /api/v1/health.

Nunca guardar segredos no Git. A chave administrativa deve ser provisionada por ambiente; não existe senha administrativa predefinida.

## Testes

Executar pytest -q. Os testes cobrem health, autenticação, registo, catálogo, triagem, isolamento de conversas e validação de tamanho. A execução deve ser registada no PR; a mera existência dos testes não significa que passaram.

## Cliente externo

Instalar requests no ambiente do cliente. Definir CPE_API_BASE_URL, CPE_CLIENT_EMAIL e CPE_CLIENT_PASSWORD como variáveis de ambiente e executar examples/client_python/client.py. O cliente usa apenas endpoints públicos documentados, sem importar código interno da API.

## Limitações antes de piloto

Migrar para PostgreSQL, adicionar migrações e backup/restauro, rever rotação e revogação de tokens, rate limiting distribuído, verificação de email, proteção contra abuso, política RGPD de retenção/eliminação, revisão do fornecedor e testes independentes de segurança. Não colocar o serviço na internet pública antes de fechar estes gates.
