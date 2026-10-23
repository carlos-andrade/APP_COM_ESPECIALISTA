# Arquitetura proposta — APP_COM_ESPECIALISTA

| Campo | Valor |
|---|---|
| **ID** | CPE-ARQ-001 |
| **Projeto** | APP_COM_ESPECIALISTA |
| **Repositório** | [carlos-andrade/APP_COM_ESPECIALISTA](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA) |
| **Tipo documental** | ESPECIFICACAO |
| **Fase** | FASE_0_FUNDAMENTOS |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | c020ba7ff1063f83d48a4eef45cb5c214d3050fb00620ef3d12cf15abf5d29b7 |
| **Commit de referência (versão anterior)** | [61347612289e95801bb792469131e34390f96362](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA/commit/61347612289e95801bb792469131e34390f96362) |
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
