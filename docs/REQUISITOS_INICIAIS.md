# Requisitos iniciais — APP_COM_ESPECIALISTA

| Campo | Valor |
|---|---|
| **ID** | CPE-REQ-001 |
| **Projeto** | APP_COM_ESPECIALISTA |
| **Repositório** | [carlos-andrade/APP_COM_ESPECIALISTA](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA) |
| **Tipo documental** | ESPECIFICACAO |
| **Fase** | FASE_0_FUNDAMENTOS |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.2 |
| **SHA-256 (conteúdo canónico)** | e99b09e63c56bdb5f41aae2ab46d3a281a6ace4e959a3e62d5ac661741111458 |
| **Commit de referência (versão anterior)** | [f5d8936599998b68059c6c01172807c0e414f4e8](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA/commit/f5d8936599998b68059c6c01172807c0e414f4e8) |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Proprietário do repositório APP_COM_ESPECIALISTA |
| **Aprovador** | Pendente — não há aprovação formal do conteúdo documental registada |
| **Origem** | Revisão documental do projeto; requisitos iniciais existentes no repositório |
| **Autoridade superior** | [Norma de Cabeçalho Documental Padrão — GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Histórico Git; referências e evidências indicadas no corpo documental |
| **Escopo** | Conforme definido no corpo documental |
| **Objetivo** | Conforme definido no corpo documental |
| **Dependências** | N/A — não declaradas além das referências explícitas no documento |

## Objetivo
Permitir que uma pessoa explique um problema ou selecione diretamente uma especialidade e receba apoio contextual do especialista mais adequado.

## Regra obrigatória para todos os especialistas

- **REG-IA-001 — Especialistas virtuais:** todos os especialistas existentes e futuros são agentes alimentados por IA; nenhum perfil humano é apresentado como se fosse um agente do catálogo.
- **REG-IA-002 — Padrão «PhD máximo»:** cada agente deve visar o máximo rigor e profundidade possíveis na especialidade, com instruções, limites, avaliação e testes próprios. A expressão é um padrão interno de qualidade, não uma credencial académica literal.
- **REG-IA-003 — Gate de publicação:** nenhum agente deve ser publicado sem perfil documentado, limites explícitos, avaliação específica do domínio e validações de segurança aplicáveis.
- **REG-IA-004 — Transparência e segurança:** agentes não podem alegar credenciais reais inexistentes nem apresentar-se como infalíveis; devem reconhecer incertezas e encaminhar situações de alto risco quando necessário.

Carta normativa: [CPE-001 — Especialistas Virtuais de IA](../GOVERNANCA/CARTA_CPE-001_ESPECIALISTAS_VIRTUAIS_IA.md).

## Requisitos funcionais

- **RF-001 — Entrada por problema:** aceitar texto livre e, futuramente, voz.
- **RF-002 — Catálogo:** permitir navegar e pesquisar especialidades e perfis.
- **RF-003 — Triagem:** identificar objetivo, domínio, contexto necessário e sinais de risco.
- **RF-004 — Recomendação:** recomendar especialista(s) com uma explicação curta e compreensível.
- **RF-005 — Controlo do utilizador:** permitir aceitar a recomendação, escolher outro especialista ou pedir alternativa.
- **RF-006 — Conversa:** manter o contexto dentro de uma conversa autorizada.
- **RF-007 — Plano de ação:** quando adequado, sintetizar próximos passos, prioridades e limitações.
- **RF-008 — Continuidade:** permitir consultar e retomar conversas segundo as opções de privacidade do utilizador.
- **RF-009 — Feedback:** permitir avaliar respostas, reportar erros e indicar que a recomendação não foi adequada.
- **RF-010 — API externa:** oferecer contratos versionados para outros sistemas autorizados consumirem catálogo, triagem e conversas.
- **RF-011 — Escalonamento:** sinalizar situações em que o apoio automatizado não é suficiente.
- **RF-012 — Administração do catálogo:** permitir gerir, testar, versionar, ativar e desativar perfis de especialistas.
- **RF-013 — Deteção de lacunas de cobertura:** quando nenhum especialista disponível for adequado, identificar e registar a lacuna em vez de atribuir a questão a um agente inadequado.
- **RF-014 — Criação de novos especialistas:** iniciar um fluxo controlado para especificar, configurar e desenvolver um novo especialista virtual de IA para a lacuna identificada, definindo domínio, âmbito, instruções, ferramentas autorizadas, limites e critérios de encaminhamento.
- **RF-015 — Preparação e melhoria do agente:** preparar o novo especialista para atingir o padrão interno «PhD máximo» por meio de engenharia de instruções, conhecimento autorizado, ferramentas e/ou treino ou ajuste quando justificados. A abordagem deve ser documentada; fine-tuning não é obrigatório por defeito nem garantia de qualidade.
- **RF-016 — Validação antes da publicação:** submeter o agente a avaliações específicas do domínio e testes de precisão, robustez, segurança, casos-limite e encaminhamento. O agente só pode entrar no catálogo ativo após passar todos os gates aplicáveis.
- **RF-017 — Integração no catálogo:** após aprovação, atribuir identificador e versão estáveis, definir categoria e metadados, registar evidências de avaliação e disponibilizar o especialista na mesma categoria operacional dos restantes agentes aprovados.
- **RF-018 — Encaminhamento enquanto a lacuna é resolvida:** até o novo especialista ser aprovado, informar que não existe cobertura adequada, pedir esclarecimentos, propor alternativa segura ou encaminhar para apoio humano qualificado quando apropriado. Nunca apresentar um agente não validado como pronto.
- **RF-019 — Ciclo de vida e monitorização:** monitorizar qualidade após publicação, recolher feedback, reavaliar versões e suspender ou retirar agentes que falhem critérios relevantes.

## Requisito transversal — criação segura de especialistas em falta

Quando uma necessidade não puder ser atribuída com segurança e adequação a nenhum especialista publicado e disponível, o sistema deve abrir um processo de lacuna de cobertura. O processo deve incluir:

1. Registar a necessidade e a razão pela qual o catálogo atual é insuficiente, minimizando dados pessoais.
2. Definir o perfil do novo especialista, domínio, âmbito, exclusões, riscos e critérios de aceitação.
3. Desenvolver e configurar o agente com instruções, fontes e ferramentas autorizadas, sem conceder permissões por defeito.
4. Selecionar e documentar a abordagem de preparação: configuração, recuperação de conhecimento, ferramentas, treino ou ajuste de modelo, conforme necessário e permitido.
5. Executar avaliações e testes reproduzíveis e documentar resultados, limitações e versão.
6. Exigir aprovação do gate de publicação antes de ativar o agente no catálogo.
7. Integrar o agente aprovado na categoria correspondente e disponibilizá-lo aos utilizadores e clientes API conforme as permissões.
8. Monitorizar resultados e manter mecanismos de correção, desativação e reversão.

**Regra fail-closed:** a ausência de um especialista adequado nunca autoriza a publicação automática de um agente não testado. Até à aprovação, o sistema deve usar uma alternativa segura, pedir clarificação ou encaminhar a pessoa para apoio humano apropriado.

## Requisitos não funcionais

- **RNF-001 — Segurança:** autenticação, autorização por recurso, validação de entradas, limitação de pedidos e gestão segura de segredos.
- **RNF-002 — Privacidade:** minimização de dados, política de retenção, eliminação controlada e acesso transparente ao histórico.
- **RNF-003 — Observabilidade:** logs estruturados, métricas e correlação de pedidos sem registar segredos nem dados sensíveis desnecessários.
- **RNF-004 — Fiabilidade:** timeouts, tratamento de erros, retentativas limitadas e degradação controlada quando um fornecedor não está disponível.
- **RNF-005 — Portabilidade:** camada de IA desacoplada de um único fornecedor.
- **RNF-006 — Acessibilidade:** interface responsiva, navegação por teclado e texto compreensível.
- **RNF-007 — Testabilidade:** testes automatizados para seleção, contratos de API, autorização e cenários de segurança.
- **RNF-008 — Transparência:** mostrar a natureza automatizada das respostas e não inventar credenciais ou ações.

## Fora do âmbito inicial

- Garantir que o conselho resolverá o problema do utilizador.
- Representar especialistas de IA como profissionais humanos licenciados.
- Executar atos médicos, jurídicos ou financeiros regulados.
- Publicar um catálogo enorme antes de validar a qualidade da triagem.
- Guardar indefinidamente todas as conversas por defeito.

## Questões para decisão de arquitetura

1. Autenticação e modelo de contas.
2. Tecnologias de frontend, backend e persistência.
3. Fornecedor(es) de modelos e estratégia de custos.
4. Política de memória e retenção por tipo de dado.
5. Domínios incluídos no primeiro piloto e protocolos de risco.
6. Métricas de qualidade e critérios de aceitação do MVP.

## Critérios de aceitação adicionais para novos especialistas

- A lacuna de cobertura é identificada quando nenhum agente publicado satisfaz os critérios de adequação e segurança.
- O perfil e os limites do novo agente são documentados e versionados.
- A abordagem de preparação ou treino é justificada e rastreável.
- O agente passa avaliações específicas e gates de segurança antes de ser publicado.
- A publicação coloca o agente na categoria adequada e torna-o consultável pelas interfaces autorizadas.
- Se a avaliação falhar, o agente permanece fora do catálogo ativo e o utilizador recebe uma alternativa segura.
- A publicação e as alterações de versão ficam auditáveis e podem ser revertidas.

## Estado

Documento atualizado para incluir a criação controlada de especialistas em falta. Os requisitos continuam propostos e não são considerados formalmente aprovados até existir uma decisão explícita.
