# CARTA DE PRINCÍPIOS — ESPECIALISTAS VIRTUAIS DE IA

| Campo | Valor |
|---|---|
| **ID** | CPE-CARTA-001 |
| **Projeto** | APP_COM_ESPECIALISTA |
| **Repositório** | [carlos-andrade/APP_COM_ESPECIALISTA](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA) |
| **Tipo documental** | CARTA |
| **Fase** | TRANSVERSAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | a5086095e2ef8d98d142b1f03ab9d8e331a01f2b14df49cefc88b788bac72d39 |
| **Commit de referência (versão anterior)** | [04a22292e2f273be13d04dd90d62814b290d8c2b](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA/commit/04a22292e2f273be13d04dd90d62814b290d8c2b) |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Proprietário do repositório APP_COM_ESPECIALISTA |
| **Aprovador** | Pendente — não há aprovação formal do conteúdo documental registada |
| **Origem** | Carta de princípios já registada no repositório do projeto |
| **Autoridade superior** | [Norma de Cabeçalho Documental Padrão — GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Histórico Git; referências e evidências indicadas no corpo documental |
| **Escopo** | Conforme definido no corpo documental |
| **Objetivo** | Conforme definido no corpo documental |
| **Dependências** | N/A — não declaradas além das referências explícitas no documento |

- **Projeto:** APP_COM_ESPECIALISTA
- **ID da carta:** CPE-001
- **Versão:** 1.0.0
- **Estado:** Regra de produto registada; implementação e validação técnica pendentes

## 1. Regra fundamental

Todos os especialistas disponibilizados pelo APP_COM_ESPECIALISTA são **agentes virtuais alimentados por inteligência artificial**. Quando uma pessoa real apresenta um problema, a aplicação encaminha-a para um especialista virtual de IA adequado à necessidade. Esta regra aplica-se a todos os especialistas existentes e a todos os que venham a ser criados, independentemente da área.

## 2. Padrão de excelência: «PhD máximo»

A expressão **«PhD máximo»** é o padrão interno de excelência pretendido para cada agente: deve atuar com profundidade técnica, raciocínio rigoroso, domínio amplo da especialidade, capacidade de explicar fundamentos, avaliação crítica de alternativas, reconhecimento de incerteza e produção de respostas estruturadas e úteis.

Este padrão é um objetivo de conceção e avaliação, não uma credencial académica literal. Um agente de IA não possui, por ser um agente, um doutoramento real, licença profissional, experiência humana ou infalibilidade. A aplicação não pode afirmar que um agente tem um título académico ou uma habilitação profissional real que não possui.

## 3. Requisitos obrigatórios para cada especialista

Cada agente deve:

1. Ter uma especialidade e um âmbito de atuação claramente definidos.
2. Ser configurado e avaliado para demonstrar o nível máximo de rigor e profundidade possível naquela especialidade.
3. Usar terminologia técnica apropriada e adaptar a explicação ao conhecimento do utilizador.
4. Separar factos, inferências, hipóteses, recomendações e incertezas.
5. Pedir esclarecimentos quando a informação disponível for insuficiente ou ambígua.
6. Não inventar fontes, dados, credenciais, ações executadas ou resultados de validação.
7. Reconhecer limites, recusar conclusões sem suporte e encaminhar para apoio humano qualificado quando necessário.
8. Ser submetido a testes específicos do domínio, incluindo testes de precisão, robustez, segurança e tratamento de casos-limite.
9. Ter instruções, versão, ferramentas autorizadas, limites e critérios de aceitação documentados.
10. Ser continuamente avaliado; uma designação interna de excelência nunca substitui evidência de qualidade.

## 4. Regra de universalidade

Nenhum especialista do catálogo está isento desta carta. A regra aplica-se aos agentes de todas as áreas atuais e futuras, aos especialistas selecionados automaticamente e aos escolhidos manualmente pelo utilizador. Novos agentes só devem ser publicados depois de cumprirem os critérios de configuração, segurança e avaliação definidos para o respetivo domínio.

## 5. Seleção e encaminhamento

O sistema deve escolher o agente mais adequado à necessidade, e não simplesmente o agente com o nome mais próximo das palavras usadas. Deve considerar contexto, objetivo, informação em falta, risco e limites de atuação. Quando necessário, deve fazer perguntas antes de recomendar um agente ou propor uma abordagem multidisciplinar.

O utilizador deve poder compreender a razão da recomendação, recusá-la e escolher outro especialista.

## 6. Segurança e áreas de alto impacto

Ser um agente de IA de excelência não autoriza a apresentar respostas como certezas infalíveis nem substitui profissionais habilitados. Em saúde, saúde mental, direito, finanças e outras áreas de alto impacto, o agente deve aplicar salvaguardas específicas, comunicar limites e encaminhar para serviços de emergência ou profissionais qualificados quando a situação o exigir.

## 7. Critérios de conformidade

Um agente não pode ser considerado conforme apenas por possuir um prompt que o descreva como especialista. A conformidade exige, no mínimo:

- perfil e âmbito documentados;
- instruções e limites explícitos;
- conjunto de avaliação próprio da especialidade;
- testes de segurança e de casos-limite;
- resultados registados e critérios de aceitação cumpridos;
- mecanismo de feedback, revisão e desativação em caso de falha relevante.

## 8. Aplicação à engenharia do produto

Esta carta deve orientar o catálogo de especialistas, o motor de triagem, a orquestração, os contratos da API, os testes automatizados, a observabilidade e a governação de versões. A implementação deve permitir identificar qual agente e qual versão produziram uma resposta, respeitando a privacidade do utilizador.

## 9. Regra de precedência

Esta carta é um princípio transversal do produto. Todos os requisitos, perfis de agentes, fluxos de seleção e futuras funcionalidades devem respeitá-la. Uma exceção exige decisão formal documentada no repositório; não pode ser introduzida implicitamente por uma implementação.

## 10. Declaração

**Regra do APP_COM_ESPECIALISTA:** todos os especialistas são agentes virtuais alimentados por IA e devem ser concebidos e avaliados segundo o padrão interno «PhD máximo» da sua especialidade, com rigor, profundidade, transparência sobre limitações e segurança.

**Nota de estado:** esta carta regista a regra de produto. Não prova que os agentes já existam, que tenham sido treinados para todas as especialidades ou que tenham passado avaliações; esses resultados dependem de implementação e validação verificáveis.
