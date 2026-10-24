# Roadmap inicial

| Campo | Valor |
|---|---|
| **ID** | CPE-ROADMAP-001 |
| **Projeto** | APP_COM_ESPECIALISTA |
| **Repositório** | [carlos-andrade/APP_COM_ESPECIALISTA](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA) |
| **Tipo documental** | PLANO |
| **Fase** | FASE_0_FUNDAMENTOS |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.7 |
| **SHA-256 (conteúdo canónico)** | 4fae7cfefcbe74a4b586e1094bee77f1aded1303446e4007dd947bf6b4782fd6 |
| **Commit de referência (versão anterior)** | [c95edcb2c49bde05bb60dd5d712898c14506508e](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA/commit/c95edcb2c49bde05bb60dd5d712898c14506508e) |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Proprietário do repositório APP_COM_ESPECIALISTA |
| **Aprovador** | Pendente — não há aprovação formal do conteúdo documental registada |
| **Origem** | Revisão documental do projeto; roadmap existente no repositório |
| **Autoridade superior** | [Norma de Cabeçalho Documental Padrão — GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Histórico Git; referências e evidências indicadas no corpo documental |
| **Escopo** | Conforme definido no corpo documental |
| **Objetivo** | Conforme definido no corpo documental |
| **Dependências** | N/A — não declaradas além das referências explícitas no documento |


[![APROVAR AGORA?](https://img.shields.io/badge/APROVAR%20AGORA%3F-%E2%9C%93-2ea44f?style=for-the-badge)](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA/issues/4)

> **Aprovação formal:** selecione o botão verde para abrir o registo de aprovação deste documento. Para aprovar a versão indicada no issue, publique o comentário de aprovação solicitado. Abrir o link, por si só, não aprova o documento. A aprovação só é válida para a versão exata identificada no registo.

O roadmap define a sequência de trabalho proposta. Uma fase não é considerada concluída apenas por ter documentação: requer evidências verificáveis e critérios de aceitação.

| Fase | Entrega | Critério de saída | Estado |
| --- | --- | --- | --- |
| R0 — Visão | Visão do produto e âmbito do MVP | Objetivo e limites registados | Documentado; aguarda aprovação formal |
| R1 — Requisitos | Requisitos funcionais e não funcionais | Requisitos revistos e priorizados | Proposta criada |
| R2 — Arquitetura | Arquitetura lógica, fronteiras e contratos | Decisões técnicas registadas | Proposta criada |
| R3 — UX | Fluxos e protótipo da experiência | Testes de usabilidade com tarefas-chave | Por iniciar |
| R4 — MVP | Catálogo, triagem, conversa e feedback | Testes automatizados e demonstração funcional | Por iniciar |
| R5 — API | API versionada para clientes externos | OpenAPI, autenticação, testes contratuais e exemplo de integração | Por iniciar |
| R6 — Segurança e qualidade | Avaliações por domínio, privacidade e observabilidade | Gates de segurança e qualidade aprovados | Por iniciar |
| R7 — Piloto | Piloto limitado e análise de resultados | Métricas analisadas e decisão documentada | Por iniciar |
| R8 — Expansão | Mais domínios e integrações | Aprovação baseada em evidências do piloto | Por iniciar |

## Trabalho adicional — memória e aprendizagem controlada

Antes do piloto, definir e validar o esquema de armazenamento das interações, o sinal explícito de aceitação, a separação entre histórico privado e corpus partilhado, as regras de curadoria e a política de retenção/eliminação. Implementar testes de isolamento entre utilizadores, autorização, minimização de dados, propagação de eliminações, proveniência e regressão de qualidade. Só disponibilizar conhecimento derivado após revisão e aprovação documentadas.

## Próximo passo recomendado

Rever e aprovar formalmente a visão e os requisitos iniciais; em seguida decidir tecnologias, modelo de dados, autenticação, política de memória e os domínios para o primeiro piloto.

## Regra de estado

Não declarar implementação, testes, segurança ou prontidão de produção sem evidência verificável no repositório e/ou nos resultados de execução.


## Atualização de execução — 2026-10-24

| Frente | Estado | Evidência / bloqueio |
|---|---|---|
| Núcleo API | Implementação inicial integrada | PR #6 integrado em main; não representa aprovação de segurança |
| PostgreSQL | Preparação no ramo de remediação | Dockerfile, compose.yaml, psycopg e esquema inicial adicionados; falta executar e validar |
| Testes | Validação local básica passou | 12 testes passaram localmente; falta CI verde e integração PostgreSQL |
| CI | Bloqueada | Criação do workflow foi bloqueada pelo conector; sem execução verde |
| Documentação | Em revisão | Cabeçalhos e hashes das novas versões precisam de validação; não marcar como APROVADO sem decisão explícita |
| Segurança e privacidade | Pendente | Política de retenção/RGPD, revisão de autenticação, rate limit, eliminação e memória |
| Cliente externo | Smoke test local passou | Cliente Python invocou por HTTP o catálogo e a triagem da API local; falta ambiente implantado e integração a partir de segundo repositório |
| Piloto | NÃO AUTORIZADO | Depende do fecho verificável de todos os gates anteriores |
