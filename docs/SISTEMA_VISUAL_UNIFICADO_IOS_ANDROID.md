# Sistema visual unificado — APP_COM_ESPECIALISTA

| Campo | Valor |
|---|---|
| **ID** | CPE-UX-001 |
| **Projeto** | APP_COM_ESPECIALISTA |
| **Repositório** | [carlos-andrade/APP_COM_ESPECIALISTA](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA) |
| **Tipo documental** | ESPECIFICACAO |
| **Fase** | FASE_1_UX |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 93cc829ffb5df6f73615fd459751eb3ca9758c3e7a2c3e30490bb683ed37f675 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-24 |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Proprietário do repositório APP_COM_ESPECIALISTA |
| **Aprovador** | Pendente — aprovação formal deste documento não registada |
| **Origem** | Decisão de produto registada na [Issue #7](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA/issues/7) |
| **Autoridade superior** | [Norma de Cabeçalho Documental Padrão — GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Issue #7; arquitetura proposta; roadmap |
| **Escopo** | Sistema visual e experiência móvel iOS/Android |
| **Objetivo** | Especificar identidade visual partilhada com temas claro e escuro nas duas plataformas |
| **Dependências** | Arquitetura, fluxos UX, acessibilidade, implementação cliente e testes |

[![APROVAR AGORA?](https://img.shields.io/badge/APROVAR%20AGORA%3F-%E2%9C%93-2ea44f?style=for-the-badge)](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA/issues/7)

> Abrir o link não aprova o documento. A aprovação exige comentário explícito para a versão exata.

## 1. Decisão

Adotar um único sistema visual e funcional para iOS e Android, com temas claro e escuro disponíveis em ambas as plataformas. Maximizar a reutilização de componentes, tokens de design, regras de interação e lógica de produto, preservando adaptações necessárias às convenções de cada sistema operativo. Esta decisão não seleciona uma framework nem declara interfaces implementadas.

## 2. Princípios

1. **Identidade partilhada:** tipografia, espaçamento, cores semânticas, iconografia, cartões, formulários e estados seguem uma linguagem visual comum.
2. **Dois temas em ambas as plataformas:** claro e escuro não ficam vinculados exclusivamente a iOS ou Android.
3. **Adaptação nativa:** navegação, áreas seguras, gestos, teclado e permissões respeitam as convenções de cada plataforma.
4. **Componentes reutilizáveis:** partilhar componentes sempre que a tecnologia escolhida o permita, evitando bifurcações desnecessárias.
5. **Acessibilidade:** contraste verificável, texto escalável, alvos de toque adequados, leitores de ecrã e estados não dependentes apenas da cor.
6. **Estados completos:** carregamento, vazio, sucesso, erro, falta de rede, sessão expirada e acesso negado.
7. **Consistência funcional:** pesquisa, catálogo, triagem, conversas, histórico, feedback e definições mantêm semântica consistente.
8. **Privacidade:** não expor conteúdo de conversas em notificações ou ecrãs partilhados sem controlo adequado.

## 3. Estrutura funcional de referência

- **Início:** pesquisa/pergunta principal, especialistas em destaque e conversas recentes.
- **Especialistas:** catálogo pesquisável, categorias, capacidades, limites e encaminhamento.
- **Conversa:** mensagens, estado da resposta, mudança de especialista e feedback explícito.
- **Histórico:** conversas autorizadas, consulta e eliminação conforme política aprovada.
- **Definições:** tema do sistema/claro/escuro, acessibilidade, privacidade e sessão.

Esta estrutura é uma proposta de UX; depende da revisão dos requisitos e da arquitetura.

## 4. Tokens e componentes

Definir tokens semânticos para superfícies, texto, ações, foco, sucesso, aviso, erro, bordas, separadores, espaçamento, raios, elevação e tipografia. Cada token deve ter equivalentes nos temas claro e escuro. Validar contraste automaticamente e por inspeção manual.

Componentes-base: botão, pesquisa, campo de mensagem, cartão de especialista, linha de conversa, carregamento, aviso, diálogo de confirmação e navegação. Os códigos de cor finais devem ser decididos e verificados no protótipo; não são fixados aqui.

## 5. Requisitos de comportamento

- Respeitar a preferência do sistema e permitir escolha manual de tema, conforme validação dos requisitos.
- Preservar o tema na navegação e entre sessões conforme política aprovada.
- Adaptar a ecrãs e orientações diferentes sem truncar conteúdo essencial.
- Apresentar identidade, domínio e limites do especialista.
- Fornecer erros acionáveis e preservar texto escrito quando possível.
- Não expor dados sensíveis em logs de interface ou telemetria sem controlo apropriado.

## 6. Critérios de aceitação

1. Protótipos iOS e Android nos dois temas.
2. Fluxos de início, catálogo, triagem, conversa e histórico representados.
3. Verificação de contraste e leitor de ecrã documentada.
4. Testes em ecrãs pequenos/grandes, texto ampliado, teclado e erros.
5. Tokens e componentes documentados antes da implementação final.
6. Testes funcionais equivalentes nas plataformas suportadas.
7. Revisão de privacidade e segurança antes do piloto.
8. Evidências no repositório; imagens promocionais não contam como prova de implementação.

## 7. Estado e próximos passos

**Estado:** especificação inicial em revisão. A decisão de produto foi registada na Issue #7; esta versão ainda requer aprovação documental explícita.

Próximas ações: incorporar a direção na arquitetura e roadmap; decidir e documentar a estratégia/framework de cliente; produzir protótipos navegáveis; implementar tokens e componentes; executar testes de acessibilidade, responsividade e paridade; reler os ficheiros do GitHub e validar hashes.

## 8. Limites

Este documento não aprova framework, biblioteca visual, publicação nas lojas, conformidade integral com RGPD, prontidão de produção nem autorização do piloto. Esses pontos exigem decisões e evidências separadas.
