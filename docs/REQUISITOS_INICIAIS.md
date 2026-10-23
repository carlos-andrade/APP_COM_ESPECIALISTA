# Requisitos iniciais — APP_COM_ESPECIALISTA

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

## Estado

Documento inicial proposto para revisão. Os requisitos não são considerados formalmente aprovados até existir uma decisão explícita.