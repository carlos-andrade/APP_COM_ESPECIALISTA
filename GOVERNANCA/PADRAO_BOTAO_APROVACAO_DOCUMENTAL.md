# Padrão local — Botão de aprovação documental

| Campo | Valor |
|---|---|
| **ID** | CPE-GOV-APPROVAL-BUTTON-001 |
| **Projeto** | APP_COM_ESPECIALISTA |
| **Repositório** | [carlos-andrade/APP_COM_ESPECIALISTA](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA) |
| **Tipo documental** | NORMA |
| **Fase** | GOVERNANCA |
| **Estado** | APROVADO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 7e11cf77af279a3928309bb7e40509e70a6abffb0b2e5f721f406cfdf6868b9b |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Proprietário do repositório APP_COM_ESPECIALISTA |
| **Aprovador** | Carlos Andrade — instrução explícita registada na conversa de 2026-10-23 |
| **Origem** | Adoção explícita do padrão de aprovação documental |
| **Autoridade superior** | [Norma central — Botão de aprovação documental](https://github.com/carlos-andrade/GOVERNANCA/blob/main/standards/botao-aprovacao-documental.md) e [Norma de cabeçalho](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Histórico Git e issues de aprovação específicos por documento |

## Regra obrigatória

Todo documento deste repositório que aguarde aprovação formal deve exibir um botão verde clicável com o texto exato **APROVAR AGORA?**, ligado a um registo GitHub próprio que identifique o ID, caminho e versão exata do documento.

Formato padrão:

[![APROVAR AGORA?](https://img.shields.io/badge/APROVAR%20AGORA%3F-%E2%9C%93-2ea44f?style=for-the-badge)](URL_DO_REGISTO_DE_APROVACAO)

O registo deve explicar como aprovar ou rejeitar e exigir uma decisão explícita, rastreável e atribuível ao responsável autorizado. Abrir o link, por si só, não constitui aprovação. Não inferir consentimento pelo silêncio.

Enquanto a decisão não for registada e validada, manter o documento em EM_REVISAO (ou no estado não aprovado aplicável). Qualquer alteração material invalida a correspondência com a versão anteriormente submetida e exige que o registo de aprovação seja atualizado para a versão atual.

Após cada alteração, reler o ficheiro no GitHub, verificar o link, confirmar que a versão do registo corresponde ao documento e recalcular o SHA-256 canónico. A existência desta regra não certifica automaticamente a implementação em todos os ficheiros; cada documento pendente deve ser inspecionado individualmente.

## Registos de aprovação existentes

- [README — CPE-README-001](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA/issues/1)
- [Requisitos — CPE-REQ-001](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA/issues/2)
- [Arquitetura — CPE-ARQ-001](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA/issues/3)
- [Roadmap — CPE-ROADMAP-001](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA/issues/4)
- [Carta de princípios — CPE-CARTA-001](https://github.com/carlos-andrade/APP_COM_ESPECIALISTA/issues/5)
