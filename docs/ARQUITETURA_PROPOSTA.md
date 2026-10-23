# Arquitetura proposta — APP_COM_ESPECIALISTA

| Campo | Valor |
|---|---|
| **ID** | CPE-ARQ-001 |
| **Projeto** | APP_COM_ESPECIALISTA |
| **Repositório** | [carlos-andrade/APP_COM_ESPECIALISTA](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA) |
| **Tipo documental** | ESPECIFICACAO |
| **Fase** | FASE_0_FUNDAMENTOS |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.2 |
| **SHA-256 (conteúdo canónico)** | fb6e23ebb268fd40fe9ba305a7925bbe366b895f08bf47e0d98000bc3d07ad38 |
| **Commit de referência (versão anterior)** | [e09a35601b240fd5019e996b426f0f2c4a57f74e](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA/commit/e09a35601b240fd5019e996b426f0f2c4a57f74e) |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Proprietário do repositório APP_COM_ESPECIALISTA |
| **Aprovador** | Pendente — não há aprovação formal do conteúdo documental registada |
| **Origem** | Revisão documental do projeto; proposta arquitetural existente no repositório |
| **Autoridade superior** | [Norma de Cabeçalho Documental Padrão — GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Histórico Git; referências e evidências indicadas no corpo documental |
| **Escopo** | Conforme definido no corpo documental |
| **Objetivo** | Conforme definido no corpo documental |
| **Dependências** | N/A — não declaradas além das referências explícitas no documento |

## 1. Visão lógica

Cliente web/mobile → API Gateway/Backend → Orquestrador de especialistas → Adaptadores de IA e ferramentas autorizadas.

O backend comunica com o catálogo de especialistas, o serviço de conversas, a persistência e a camada de observabilidade. A API pública para clientes externos deve ser separada das interfaces internas de orquestração.

## 2. Componentes

### Interface do utilizador
- Campo para descrever o problema.
- Catálogo e pesquisa manual.
- Ecrã de recomendação e respetiva justificação.
- Interface de conversa, resumo e plano de ação.
- Controlos explícitos para histórico, memória, feedback e mudança de especialista.

### API de aplicação
- Autenticar e autorizar cada pedido.
- Validar esquemas, limites e permissões.
- Versionar contratos.
- Aplicar quotas, idempotência quando adequada e respostas de erro consistentes.

### Orquestrador
- Classificar a necessidade.
- Identificar informação em falta e fazer perguntas de clarificação.
- Aplicar regras de elegibilidade, risco e encaminhamento.
- Selecionar um especialista ou apresentar alternativas.
- Construir o contexto mínimo necessário para a conversa.
- Registar a versão do especialista e as decisões relevantes para auditoria.

### Catálogo de especialistas
- Identificadores estáveis e metadados estruturados.
- Domínios, capacidades, exclusões e requisitos de encaminhamento.
- Prompt/instruções versionadas e configuração do modelo.
- Estado de publicação, conjunto de testes e histórico de avaliação.

### Conversas e memória
- Separar mensagens, metadados operacionais e preferências persistentes.
- Aplicar autorização em cada leitura e escrita.
- Definir prazos de retenção e mecanismos de exportação/eliminação.
- Não usar memória persistente sem comunicação clara e controlo adequado.

### Memória de interações e aprendizagem curada

- **Armazenamento de conversas:** persistir questões e respostas num serviço separado do catálogo, com identificador do utilizador/tenant, conversa, especialista e versão, timestamps, estado de aceitação e metadados mínimos necessários. Aplicar autorização por recurso em cada leitura e escrita.
- **Sinal de aceitação:** recolher um evento explícito do utilizador para identificar uma resposta aceite/útil; não inferir aceitação pelo silêncio nem pela continuação da conversa.
- **Corpus por especialista:** manter um corpus versionado e segregado por especialidade, com itens elegíveis, proveniência, estado de revisão, etiquetas de qualidade e referências aos registos de origem sob controlo de acesso.
- **Pipeline de curadoria:** validar, desduplicar, minimizar dados, remover segredos, avaliar risco e qualidade, anonimizar/pseudonimizar quando possível, rever a autorização de reutilização e aprovar antes de indexar ou disponibilizar qualquer item a outros utilizadores.
- **Recuperação antes de treino:** preferir inicialmente recuperação de conhecimento (RAG) e conjuntos de avaliação versionados. Treino/fine-tuning só após decisão técnica explícita, base legal e avaliação de risco; a aceitação de uma resposta não autoriza, por si só, treino automático.
- **Separação de finalidades:** histórico privado de conversa não é automaticamente conhecimento partilhado. A reutilização para melhorar o especialista exige transparência, base legal e consentimento quando necessário, além de mecanismos de exclusão.
- **Direitos e ciclo de vida:** suportar retenção configurável, acesso, exportação, correção e eliminação; propagar eliminações aos índices e corpora derivados quando aplicável; manter logs de auditoria sem duplicar conteúdo sensível.
- **Segurança e qualidade:** encriptar dados em trânsito e em repouso, restringir acessos por função, registar auditoria, testar isolamento entre utilizadores/tenants e avaliar contaminação, envenenamento, enviesamento e regressões antes de publicar cada versão do corpus.

### Camada de modelos e ferramentas
- Adaptadores substituíveis para fornecedores de modelos.
- Timeouts, limites de custo e tratamento de falhas.
- Ferramentas em lista permitida, com validação de parâmetros e permissões mínimas.
- Tratar conteúdo recuperado de ferramentas como dados, nunca como instruções privilegiadas.

### Observabilidade e avaliação
- Logs estruturados com identificadores de correlação.
- Métricas de latência, falhas, custo, satisfação e adequação da recomendação.
- Conjuntos de avaliação por domínio e testes de regressão.
- Redação de dados sensíveis e controlo do acesso a registos.

## 3. Contratos de API — proposta de trabalho

Base: `/api/v1`.

| Método | Caminho | Finalidade |
| --- | --- | --- |
| POST | `/triage` | Analisar a necessidade e devolver recomendação e justificação |
| GET | `/specialists` | Pesquisar e filtrar especialistas |
| GET | `/specialists/{id}` | Consultar um perfil publicado |
| POST | `/conversations` | Criar conversa para um especialista selecionado |
| POST | `/conversations/{id}/messages` | Enviar mensagem e receber resposta |
| GET | `/conversations/{id}` | Obter conversa a que o cliente tem acesso |
| POST | `/feedback` | Registar feedback associado a resposta/conversa |

Todos os caminhos são conceptuais até à aprovação dos esquemas OpenAPI. Respostas deverão usar códigos HTTP adequados, mensagens de erro consistentes e identificadores de pedido. Endpoints autenticados devem verificar propriedade ou acesso delegado ao recurso.

## 4. Segurança e limites

- Separar autenticação, autorização e regras de negócio.
- Guardar segredos fora do código e dos logs.
- Aplicar proteção contra abuso, injeção de prompt, exfiltração e uso indevido de ferramentas.
- Não permitir que o modelo altere permissões, políticas ou seleção de ferramentas por instruções originadas no conteúdo do utilizador.
- Implementar fluxos específicos para crise, saúde, risco financeiro, questões jurídicas e outras matérias de alto impacto.
- Distinguir recomendação automatizada de consulta por profissional humano.

## 5. Evolução incremental

1. Prototipar experiência e modelo de especialista.
2. Validar triagem com cenários representativos.
3. Implementar API, catálogo e conversa mínima.
4. Acrescentar autenticação, privacidade, observabilidade e testes de segurança.
5. Executar piloto restrito e rever evidências antes de escalar.

## Estado

Proposta arquitetural inicial; não constitui descrição de funcionalidades implementadas.
