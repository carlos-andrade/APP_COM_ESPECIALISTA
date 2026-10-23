# APP_COM_ESPECIALISTA

| Campo | Valor |
|---|---|
| **ID** | CPE-README-001 |
| **Projeto** | APP_COM_ESPECIALISTA |
| **Repositório** | [carlos-andrade/APP_COM_ESPECIALISTA](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA) |
| **Tipo documental** | README |
| **Fase** | FASE_0_FUNDAMENTOS |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 95d9c7a693a7dd08c3a1aa048e727233c5537e047e1adade24df7a6a4532d89e |
| **Commit de referência (versão anterior)** | [557f2bacc41ef20999726543be4c48e955619165](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA/commit/557f2bacc41ef20999726543be4c48e955619165) |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Proprietário do repositório APP_COM_ESPECIALISTA |
| **Aprovador** | Pendente — não há aprovação formal do conteúdo documental registada |
| **Origem** | Visão do produto e documentação inicial do projeto |
| **Autoridade superior** | [Norma de Cabeçalho Documental Padrão — GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Histórico Git; documentos ligados neste README |
| **Escopo** | Visão, requisitos, arquitetura, roadmap e governança inicial do projeto |
| **Objetivo** | Descrever o produto, o estado documental e as regras de execução |
| **Dependências** | Documentos de requisitos, arquitetura, roadmap e governança referenciados abaixo |

> Um especialista para cada desafio da vida.

## 1. Visão do produto

Criar uma aplicação que permita a qualquer pessoa explicar um problema em linguagem natural e receber apoio do especialista mais adequado, em qualquer área relevante da vida. O utilizador também pode escolher diretamente uma especialidade ou um especialista.

A aplicação não deve ser apenas um chatbot com personagens diferentes: deve combinar triagem de necessidades, seleção transparente de especialistas, conversa contextual, planos de ação e encaminhamento responsável quando a situação ultrapassar as capacidades do sistema.

## Regra transversal dos especialistas virtuais

Todos os especialistas, atuais e futuros, são agentes virtuais alimentados por inteligência artificial e devem ser concebidos e avaliados segundo o padrão interno **«PhD máximo»** da sua especialidade. Esta expressão significa um objetivo de excelência técnica, profundidade e rigor; não é uma credencial académica literal nem autoriza alegações de doutoramento, licença profissional ou infalibilidade. A publicação de cada agente depende de critérios de qualidade, testes e salvaguardas próprios do domínio.

Carta normativa: [CPE-001 — Especialistas Virtuais de IA](GOVERNANCA/CARTA_CPE-001_ESPECIALISTAS_VIRTUAIS_IA.md).

## 2. Princípios fundamentais

- **Acesso simples:** começar pelo problema descrito pela pessoa, não obrigá-la a conhecer o nome da profissão certa.
- **Escolha do utilizador:** permitir pesquisa e seleção manual de áreas e especialistas.
- **Seleção fundamentada:** explicar brevemente por que motivo um especialista foi recomendado.
- **Continuidade:** preservar o contexto autorizado pelo utilizador para evitar que tenha de repetir tudo.
- **Transparência:** distinguir informação geral, apoio por IA e aconselhamento prestado por profissionais humanos.
- **Segurança:** reconhecer situações de risco e aplicar encaminhamento apropriado.
- **Privacidade:** recolher apenas dados necessários, com controlos claros sobre histórico e memória.
- **Qualidade verificável:** definir critérios de avaliação, testes e mecanismos para comunicar respostas inadequadas.

## 3. Experiência principal

1. O utilizador descreve o problema em linguagem natural.
2. O sistema identifica a área, o objetivo, o contexto relevante e eventuais sinais de urgência.
3. O sistema seleciona ou recomenda um especialista e explica a escolha.
4. O utilizador inicia uma conversa ou escolhe outro especialista.
5. O especialista clarifica o contexto e responde de forma estruturada.
6. Quando útil, a conversa resulta num plano de ação com etapas, prioridades e ressalvas.
7. O utilizador pode retomar a conversa, consultar o histórico e mudar de especialista.

## 4. Exemplos de domínios

- Saúde e bem-estar — com limites clínicos claros e encaminhamento para profissionais de saúde quando necessário.
- Psicologia e relações pessoais — apoio informativo e emocional responsável, sem substituir cuidados profissionais.
- Finanças pessoais, orçamento, dívidas e educação financeira.
- Direito, direitos do consumidor e orientação para encontrar apoio jurídico qualificado.
- Educação, explicações, estudo e aprendizagem.
- Carreira, procura de emprego e desenvolvimento profissional.
- Tecnologia, programação, cibersegurança e suporte técnico.
- Empreendedorismo, gestão, vendas e marketing.
- Casa, manutenção, organização e vida quotidiana.
- Escrita, criatividade, comunicação e produção de conteúdo.
- Família, parentalidade e orientação prática.
- Administração pública e compreensão de procedimentos.

Esta lista é inicial e extensível; não limita as áreas futuras.

## 5. Modelo de especialista

Cada especialista deverá ter, no mínimo:

- identificador estável e nome;
- domínio e subdomínios;
- descrição e necessidades que pode atender;
- instruções e limites de atuação;
- perguntas de clarificação recomendadas;
- critérios de seleção e sinais de encaminhamento;
- fontes ou ferramentas permitidas, quando aplicável;
- versão, estado de publicação e testes de qualidade.

Especialistas de IA não devem alegar qualificações humanas que não possuem. Quando forem apresentados profissionais humanos, as qualificações e a disponibilidade devem ser verificadas.

## 6. Seleção de especialistas

A seleção deve considerar adequação ao problema, objetivo declarado, contexto relevante, urgência, competências disponíveis e limites de atuação. A recomendação deve ser compreensível e o utilizador deve poder recusá-la ou selecionar outro especialista.

Quando o problema envolver vários domínios, a aplicação poderá propor uma sequência coordenada ou uma abordagem multidisciplinar, sem gerar encaminhamentos desnecessários.

## 7. Âmbito inicial (MVP)

1. Página inicial com campo para descrever o problema.
2. Catálogo pesquisável de especialistas e categorias.
3. Motor de triagem e recomendação.
4. Conversa contextual com o especialista escolhido.
5. Resumo da conversa e plano de ação.
6. Histórico controlado pelo utilizador.
7. Feedback de qualidade e opção de mudar de especialista.
8. Avisos e encaminhamento específicos para domínios de risco.

O MVP deverá validar primeiro a utilidade da triagem, a qualidade das conversas e a experiência de mudança entre especialistas, antes de expandir para um catálogo massivo.

## 8. Arquitetura de referência — proposta inicial

- **Frontend:** aplicação web responsiva, acessível em computador e telemóvel.
- **Backend/API:** API versionada com autenticação, autorização, validação e documentação.
- **Orquestrador:** componente responsável por triagem, seleção, contexto e passagem de controlo ao especialista.
- **Catálogo:** registo versionado de áreas e perfis de especialistas.
- **Camada de IA:** adaptadores desacoplados dos fornecedores de modelos.
- **Persistência:** utilizadores, preferências, conversas e auditoria, com políticas de retenção explícitas.
- **Observabilidade:** métricas, logs estruturados, rastreabilidade e avaliação de qualidade, sem expor dados sensíveis desnecessários.
- **Segurança:** gestão de segredos, limites de utilização, prevenção de abuso e minimização de dados.

Esta arquitetura é uma proposta de partida, não uma declaração de implementação existente. As tecnologias concretas devem ser decididas durante o desenho técnico.

## 9. API reutilizável

A API deverá ser concebida para que aplicações de outros repositórios possam invocar as capacidades de triagem, consulta do catálogo e gestão das conversas. As interfaces devem ser documentadas, versionadas, autenticadas e estáveis, com contratos de entrada e saída, códigos de erro, limites de utilização e testes de compatibilidade.

Operações conceptuais iniciais:

- `POST /api/v1/triage` — analisar a necessidade e recomendar especialistas;
- `GET /api/v1/specialists` — pesquisar o catálogo;
- `GET /api/v1/specialists/{id}` — consultar um perfil;
- `POST /api/v1/conversations` — iniciar uma conversa;
- `POST /api/v1/conversations/{id}/messages` — enviar uma mensagem;
- `GET /api/v1/conversations/{id}` — consultar uma conversa autorizada;
- `POST /api/v1/feedback` — registar avaliação da resposta.

Estes endpoints são uma proposta sem implementação e poderão ser revistos após aprovação dos contratos da API.

## 10. Segurança, limites e domínios de alto risco

- Não apresentar conteúdo gerado como diagnóstico médico, decisão jurídica ou garantia financeira.
- Identificar urgências e disponibilizar orientações de segurança proporcionais ao risco.
- Não inventar qualificações, fontes, disponibilidade ou ações executadas.
- Informar o utilizador quando uma recomendação é automatizada.
- Proteger dados pessoais e restringir o acesso a conversas.
- Avaliar os especialistas com testes específicos para o respetivo domínio.
- Permitir sinalização de erros e revisão de conteúdo inadequado.

## 11. Roadmap proposto

### Fase 0 — Fundamentos
Aprovar visão, requisitos, limites, critérios de sucesso, política de dados e arquitetura.

### Fase 1 — Desenho da experiência
Definir fluxos, protótipo, categorias iniciais, modelo de especialista e regras de recomendação.

### Fase 2 — Núcleo funcional
Implementar catálogo, triagem, conversa, histórico controlado e API versionada.

### Fase 3 — Validação
Testar qualidade das recomendações, segurança, privacidade, acessibilidade, desempenho e robustez.

### Fase 4 — Expansão
Adicionar especialistas e domínios, integrações externas e eventuais diretórios de profissionais humanos verificados.

Cada fase só deve ser considerada concluída após evidências e critérios de aceitação documentados.

## 12. Critérios de sucesso iniciais

- O utilizador consegue começar pelo problema sem conhecer a categoria técnica.
- A recomendação é relevante e inclui uma explicação compreensível.
- É possível escolher outro especialista sem perder o contexto autorizado.
- As respostas são úteis, claras e proporcionais ao nível de confiança.
- Situações de risco são tratadas pelos fluxos definidos.
- A API é utilizável por clientes independentes e dispõe de documentação e testes.
- A privacidade, a segurança e a qualidade são validadas antes da expansão.

## Regra de governança — sincronização do README

Todas as atualizações do projeto que tenham sido validadas devem ser refletidas neste README. Após validar uma alteração, atualizar este documento para corresponder ao estado confirmado, verificar a coerência com os artefactos alterados e reler os ficheiros no GitHub. Não apresentar propostas como funcionalidades implementadas nem declarar validações sem evidências. A regra completa está em [GOV-README-001 — Atualizações Validadas e README](GOVERNANCA/REGRA_ATUALIZACOES_VALIDACAO_README.md).

## Estado do projeto

**Estado:** visão e escopo inicial documentados; implementação ainda por iniciar.

As decisões técnicas descritas neste documento são propostas de arquitetura. Não representam funcionalidades já implementadas ou testadas.

## Validação documental do cabeçalho

Os documentos Markdown iniciais do projeto foram normalizados segundo a [Norma de Cabeçalho Documental Padrão do repositório GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md). A revisão inclui os requisitos, a arquitetura proposta, o roadmap, a carta CPE-001 e a regra de sincronização do README. Os campos SHA-256 canónico seguem a normalização UTF-8/LF e excluem do cálculo as linhas do próprio SHA-256 e do commit de referência.

A aplicação do cabeçalho é uma validação estrutural/documental; não equivale à aprovação formal de todos os requisitos nem prova implementação ou testes funcionais.

## Histórico de alterações

| Versão | Data | Alteração | Responsável | Evidência |
|---|---|---|---|---|
| 1.0.1 | 2026-10-23 | Aplicação do cabeçalho canónico e sincronização da regra de governança | Responsável do projeto | Commit GitHub desta atualização |
