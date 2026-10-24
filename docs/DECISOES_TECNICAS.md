# Decisões técnicas — APP_COM_ESPECIALISTA

| Campo | Valor |
|---|---|
| ID | CPE-ADR-001 |
| Projeto | APP_COM_ESPECIALISTA |
| Repositório | https://github.com/carlos-andrade/APP_COM_ESPECIALISTA |
| Tipo documental | DECISAO_TECNICA |
| Fase | FASE_1_IMPLEMENTACAO_MVP |
| Estado | EM_REVISAO |
| Versão | 1.0.0 |
| SHA-256 (conteúdo canónico) | PENDENTE_DE_VALIDACAO |
| Commit de referência (versão anterior) | N/A — documento novo |
| Data de criação | 2026-10-24 |
| Data de atualização | 2026-10-24 |
| Responsável | Proprietário do repositório |
| Aprovador | Pendente |
| Origem | Pedido de execução integral do MVP |
| Autoridade superior | https://github.com/carlos-andrade/GOVERNANCA |
| Cadeia de autoridade | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| Rastreabilidade | PR de implementação e testes |
| Escopo | Stack, segurança, dados, fornecedor e piloto |
| Objetivo | Registar decisões provisórias e gates de adoção |

## Decisões propostas

1. Runtime/API: Python 3.12+, FastAPI, Pydantic e OpenAPI gerado pelo framework.
2. Persistência: SQLite apenas para desenvolvimento/testes. PostgreSQL obrigatório antes de piloto multiutilizador.
3. Autenticação: JWT Bearer HS256, segredo de pelo menos 32 bytes e expiração curta. Antes do piloto, rever rotação, revogação e identidade.
4. IA: adaptador inicial OpenAI por OPENAI_API_KEY e CPE_OPENAI_MODEL. Sem chave, a conversa devolve 503; não simula resposta.
5. Dados: utilizadores, conversas, mensagens, memória curada e auditoria; autorização por proprietário.
6. Retenção provisória a aprovar: conversas 90 dias por defeito; eliminação antecipada por pedido; auditoria mínima sem conteúdo sensível por 12 meses, sujeita a base legal e revisão RGPD. Não ativar retenção real antes da aprovação.
7. Piloto: software e orientação geral de baixo risco. Excluir diagnóstico/tratamento médico, aconselhamento jurídico personalizado, decisões de crédito/investimento e situações de crise.
8. Limites iniciais: mensagem 8.000 caracteres; 60 pedidos/minuto/IP; timeout do fornecedor 30 segundos; contexto máximo 20 mensagens.
9. Versionamento: prefixo /api/v1; alterações incompatíveis exigem versão principal nova e testes contratuais.
10. Observabilidade: metadados mínimos; nunca registar passwords, tokens ou conteúdo sensível por defeito.

## Gates antes do piloto

Política final de retenção, região de alojamento, base legal, contrato com fornecedor, procedimento de direitos RGPD, PostgreSQL, gestão robusta de chaves e revisão de segurança devem ser aprovados. Este documento e a implementação do ramo não equivalem a aprovação de produção.
