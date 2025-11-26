# Fase 3 - Descrição da Medição

## Sumário

- [1. Descrição da Medição Para a Adequação Funcional](#1-descrição-da-medição-para-a-adequação-funcional)
  - [1.1. Procedimentos das Análises](#11-procedimentos-das-análises)
    - [Q1. Em que medida as funcionalidades priorizadas do MEPA foram implementadas?](#q1-em-que-medida-as-funcionalidades-priorizadas-do-mepa-foram-implementadas)
    - [Q2. Os resultados apresentados pelo MEPA nas funcionalidades estão corretos?](#q2-os-resultados-apresentados-pelo-mepa-nas-funcionalidades-estão-corretos)
    - [Q3. As funcionalidades implementadas operam em conformidade com o esperado?](#q3-as-funcionalidades-implementadas-operam-em-conformidade-com-o-esperado)
- [2. Descrição da Medição Para a Confiabilidade](#2-descrição-da-medição-para-a-confiabilidade)
  - [2.1. Procedimentos das Análises](#procedimentos-das-análises)
    - [Tolerância a Falhas (Fault Tolerance)](#tolerância-a-falhas-fault-tolerance-o-sistema-consegue-manter-a-operação-em-caso-de-falhas)
    - [Recuperabilidade (Recoverability)](#recuperabilidade-recoverability-o-sistema-consegue-se-recuperar-de-uma-falha-e-restaurar-os-dados)
    - [Disponibilidade (Availability)](#disponibilidade-availability-o-sistema-está-acessível-e-operacional-quando-necessário)
- [3. Descrição da Medição Para a Manutenibilidade](#3-descrição-da-medição-para-a-manutenibilidade)
  - [3.1. Procedimentos das Análises](#procedimentos-das-análises-1)
    - [Q8. A estrutura do código favorece a manutenção?](#q8-a-estrutura-do-código-favorece-a-manutenção-complexidade-ciclomática-média---ccm)
    - [Q9. Qual é a agilidade no fluxo de correção de defeitos?](#q9-qual-é-a-agilidade-no-fluxo-de-correção-de-defeitos-lead-time-de-correção---ltc)
    - [Q10. O sistema possui proteção adequada contra regressão?](#q10-o-sistema-possui-proteção-adequada-contra-regressão-cobertura-de-testes-de-regressão---ctr)
- [4. Ambiente de Testes](#4-ambiente-de-testes)
- [5. Instrumentos de Medição](#5-instrumentos-de-medição)
- [Localização dos Dados de Avaliação](#localização-dos-dados-de-avaliação)
- [Uso de IA](#uso-de-ia)
- [Referências Bibliográfica](#referências-bibliográfica)
- [Histórico de Versões](#historico-de-versoes)

---

## 1. Descrição da Medição Para a Adequação Funcional

Afim de permear nossa proposta inicial de abringir os escopos planejados para a adequação funcional:

   - Completude Funcional: todas as funções estão presentes?

   - Correção funcional: os resultados das funções estão corretos?

   - Pertinencia Funcional: essas funções de fato ajudam os usuários?

Mais detalhes em: [Fase 1 - Proposito de Avaliação](https://fcte-qualidade-de-software-1.github.io/2025-2_T02_CAROL-SHAW/pages/Modulo1/propositoDeAvaliacao/)

Os artefatos encontrados na documentação pública e como estudado na referência <sup>[1]</sup> e <sup>[4]</sup>, não são suficientes para a completa modelagem desse artefato o ideal é a utilização de requisitos funcionais para a completude da análise. Portanto, solicitamos uma entrevista com dois dos desenvolvedores do lappis que atuam diretamente no desenvolvimento produto: [Gabriel Ferreira](https://gitlab.com/oo7gabriel) e [Hugo Rocha](https://gitlab.com/hugorochaffs) para nos ajudar a melhor entender a aplicação e modelar de maneira mais completa esse artefato.

### 1.1. Procedimentos das Análises:

Aqui vamos descrever todo o passo a passo de como iremos realizar as medições para as perguntas feitas na etapa de planejamento de avaliação mais detalhes em: [Fase 2 - Planejamento de Avaliação](https://fcte-qualidade-de-software-1.github.io/2025-2_T02_CAROL-SHAW/pages/Modulo2/planejamentoDaAvaliacao/#2-metodologia-e-diretrizes-de-medicao). Para a melhor análise posterior das questões todos os processos será gravados e disponibilizados na [Fase 4](https://fcte-qualidade-de-software-1.github.io/2025-2_T02_CAROL-SHAW/pages/Modulo4/execucaoDaMedicao/#1-execucao-da-medicao-para-a-adequacao-funcional).

#### Q1. Em que medida as funcionalidades priorizadas do MEPA foram implementadas?

- Utilizaremos como insumos a lista de requisitos funcionais (obtida na entrevista) que será realizada na [Fase 4 - Execução da Medição](https://fcte-qualidade-de-software-1.github.io/2025-2_T02_CAROL-SHAW/pages/Modulo4/execucaoDaMedicao/#1-execucao-da-medicao-para-a-adequacao-funcional) e a análise dos documentos públicos: [Fase 1 - Proposito de Avaliação](https://fcte-qualidade-de-software-1.github.io/2025-2_T02_CAROL-SHAW/pages/Modulo1/propositoDeAvaliacao/) para verificar se as funcionalidades especificadas estão implementadas.


#### Q2. Os resultados apresentados pelo MEPA nas funcionalidades estão corretos?

- Nesta análise, o foco é a precisão dos resultados. Realizaremos testes manuais na aplicação online e offline, pois o ambiente offline possue os usuários de maior nível na aplicação ao invés só do convidado, inserindo dados de faturas e comparando os resultados gerados pela plataforma com cálculos de referência.


#### Q3. As funcionalidades implementadas operam em conformidade com o esperado?

- Na análise de pertinência buscamos entender se as funcionalidades existentes são de fato úteis e relevantes para os objetivos dos usuários. Portanto, realizamos um passo a passo simulado das tarefas do gestor como: cadastrar uma fatura e gerar um relatório de economia para avaliarmos o fluxo de trabalho é lógico.

---

## 2. Descrição da Medição Para a Confiabilidade

A **Confiabilidade**, de acordo com a norma ISO/IEC 25010, é definida como a capacidade de um sistema, produto ou componente de manter seu nível de desempenho sob condições especificadas por um determinado período de tempo. Para a avaliação da qualidade do software, focaremos nas seguintes sub-características essenciais:

<font size="3">
    <p style="text-align: center">
        <b>Tabela 1:</b> Documentos e Artefatos Analisados para Manutenibilidade
    </p>
</font>

| Sub-característica | Descrição Detalhada |
| :--- | :--- |
| **Tolerância a Falhas (Fault Tolerance)** | Capacidade do sistema de operar corretamente e manter um nível de serviço especificado, mesmo na presença de falhas de hardware ou software. Isso inclui a habilidade de evitar a falha completa do sistema. |
| **Recuperabilidade (Recoverability)** | Capacidade do sistema de restabelecer um nível de desempenho especificado e recuperar os dados afetados diretamente após uma falha. O foco é no tempo e na integridade da recuperação. |
| **Disponibilidade (Availability)** | Grau em que um sistema, produto ou componente está operacional e acessível para uso quando solicitado. É frequentemente medida pela proporção de tempo em que o sistema está em um estado operacional. |

Mais detalhes sobre o propósito e as perguntas de avaliação que guiam esta medição podem ser encontrados em: [Fase 1 - Proposito de Avaliação](https://fcte-qualidade-de-software-1.github.io/2025-2_T02_CAROL-SHAW/pages/Modulo1/propositoDeAvaliacao/) e [Fase 2 - Planejamento de Avaliação](https://fcte-qualidade-de-software-1.github.io/2025-2_T02_CAROL-SHAW/pages/Modulo2/planejamentoDaAvaliacao/#2-metodologia-e-diretrizes-de-medicao).

### Procedimentos das Análises:

A seguir, detalhamos o passo a passo de como as medições serão realizadas para responder às perguntas de avaliação definidas na etapa de planejamento.

#### Tolerância a Falhas (Fault Tolerance): o sistema consegue manter a operação em caso de falhas?

- **Procedimento:** Serão simuladas falhas controladas no ambiente de teste, como a interrupção da conexão com o banco de dados e a sobrecarga de requisições (teste de estresse). O objetivo é observar a resposta do sistema: se ele consegue tratar a exceção sem causar a interrupção total do serviço.
- **Métricas associadas:**
    - **CF1 - Taxa de Sobrevivência a Falhas (TSF):** Número de falhas simuladas que não resultaram em interrupção total do serviço/Total de falhas simuladas

#### Recuperabilidade (Recoverability): o sistema consegue se recuperar de uma falha e restaurar os dados?

- **Procedimento:** Após a simulação de uma falha que cause a interrupção do serviço (e.g., reinicialização abrupta do servidor), serão medidos dois aspectos cruciais: o tempo necessário para o sistema retornar ao estado operacional completo e a integridade dos dados transacionais mais recentes.
- **Métricas associadas:**
    - **CF2 - Tempo Médio de Recuperação (TMR):** Tempo total gasto para recuperar o sistema após falhas/Número de falhas
    - **CF3 - Índice de Perda de Dados (IPD):** Número de transações perdidas durante a falha/Total de transações no momento da falha

#### Disponibilidade (Availability): o sistema está acessível e operacional quando necessário?

- **Procedimento:** Será utilizado um script de monitoramento para registrar o tempo de atividade (*uptime*) e inatividade (*downtime*) do sistema em um período de 24 horas. A coleta de dados será realizada em intervalos regulares (e.g., a cada 5 minutos) para garantir a precisão da medição.
- **Métricas associadas:**
    - **CF4 - Disponibilidade Percentual (DP):** Tempo total de operação - Tempo total de inatividade-Tempo total de operação/100
    - **CF5 - Tempo Médio Entre Falhas (TMEF):** Tempo total de operação/Número de falhas

---

## 3. Descrição da Medição Para a Manutenibilidade

A medição da Manutenibilidade é crucial para garantir a longevidade e a adaptabilidade do software MEPA, que é um projeto de código aberto e em constante evolução. Conforme definido no Planejamento de Avaliação (Fase 2), o foco está em avaliar a facilidade com que o sistema pode ser analisado, modificado e testado.

Nossa análise será baseada no acesso ao código-fonte e aos dados de gestão de projetos, conforme detalhado nos artefatos abaixo:

<font size="3">
    <p style="text-align: center">
        <b>Tabela 2:</b> Documentos e Artefatos Analisados para Manutenibilidade
    </p>
</font>

| Artefato | Descrição | Link/Localização |
|---|---|---|
| **Repositório de Código-Fonte** | O código-fonte completo do projeto MEPA, essencial para a análise estática. | [Repositório no GitLab](https://gitlab.com/lappis-unb/projetos-energia/mec-energia) |
| **Sistema de Gestão de Issues** | Plataforma utilizada para rastrear defeitos e tarefas de manutenção (Lead Time de Correção). | [Presente no próprio repositório](https://gitlab.com/lappis-unb/projetos-energia/mec-energia/mec-energia-api/-/issues) |
| **Relatórios de Cobertura de Testes** | Documentos gerados pelo CI/CD que indicam a cobertura de código por testes automatizados. | [Presentes no próprio repositório na visualização das pipelines de CI/CD](https://gitlab.com/lappis-unb/projetos-energia/mec-energia/mec-energia-api/-/jobs/11894408124) |

### Procedimentos das Análises:

Aqui descrevemos o passo a passo de como serão realizadas as medições para as questões de Manutenibilidade definidas na Fase 2.

#### Q8. A estrutura do código favorece a manutenção? (Complexidade Ciclomática Média - CCM)

- **Procedimento:** Utilizaremos a ferramenta de análise estática SonarQube para calcular a Complexidade Ciclomática (CC) em todos nos módulos da api. A **CCM** será calculada como a média dos valores de CC para estas funções/módulos.
- **Métricas associadas:** MN4 (Complexidade Ciclomática), MN5 (Acoplamento).

#### Q9. Qual é a agilidade no fluxo de correção de defeitos? (Lead Time de Correção - LTC)

- **Procedimento:** Serão extraídos dados das Issues presentes no GitLab abrangindo um período de 6 meses. O **LTC** será calculado para uma amostra dos defeitos críticos, medindo o tempo entre a abertura da *issue* e o *merge* da correção em produção.
- **Métricas associadas:** MN1 (Tempo de Resolução de Defeitos), MN2 (Tempo de Entrega de Correção).

#### Q10. O sistema possui proteção adequada contra regressão? (Cobertura de Testes de Regressão - CTR)

- **Procedimento:** Como houve dificuldade em analisar o relatório de cobertura de código (CTR) gerado durante a build, o cálculo de CTR será feito manualmente nos últimos 5 Merge Requestes aceitos (!430; !431; !432; !433 e !435), que foram todos feitos no período do último mês.
- **Métricas associadas:** MN3 (Cobertura de Testes).

---

## 4. Ambiente de Testes:
 
Os testes foram executados nos ambientes descritos na tabela abaixo, garantindo a verificação em diferentes configurações:
 
| Componente | Especificação | Observações |
|---|---|---|
| **Sistema Operacional** | Windows 11 e Ubuntu 22.04 LTS | Utilizado para execução dos testes manuais e automáticos. |
| **Hardware** | Processador Ryzen 7 Pro 4750U, 16 GB RAM | Configuração mínima para garantir a execução fluida das ferramentas. |
| **Navegador** | Mozilla Firefox (versão mais recente) | Browser utilizado para os testes de interface e funcionalidade. |
| **Ambiente Backend** | Python 3.10+ / Django 4.2+ | Ambiente de execução da API do MEPA. |
| **Banco de Dados** | PostgreSQL 15 | Utilizado para armazenamento e consulta dos dados da aplicação. |
| **Containerização** | Docker 24.0+ | Utilizado para criar um ambiente padronizado e isolado para a aplicação e seus serviços. |

---

## 5. Instrumentos de Medição:

Para a coleta de dados, foram utilizados os seguintes instrumentos:

| Instrumento | Descrição |
|---|---|
| **Ferramenta de Captura de Tela** | Utilizada para registrar evidências estáticas (imagens) de resultados e comportamentos específicos. |
| **Software de Gravação (OBS Studio e Microsoft Teams)** | Utilizado para gravar as sessões de teste em vídeo, documentando o fluxo de interação e entrevistas. |
| **Relatório de Análise Estática** | Documento gerado pela ferramenta SonarQube contendo as métricas de código (CCM, Coesão, Acoplamento). |
| **Query de Issues** | Consulta no GitLab para extrair os dados de tempo de vida dos defeitos (LTC). |
| **Relatório de Cobertura de Código** | Documento que detalha o percentual de código coberto por testes automatizados (CTR). |
| **Ferramenta de Simulação de Carga (JMeter)** | Utilizada para gerar requisições em massa e simular sobrecarga no sistema, essencial para testar a Tolerância a Falhas. |
| **Script de Monitoramento de Uptime** | Ferramenta automatizada para registrar o tempo de atividade e inatividade do servidor, fundamental para o cálculo da Disponibilidade. |
| **Cronômetro** | Utilizados para medir o Tempo Médio de Recuperação (TMR). |
| **Ferramenta de Análise Estática** | SonarQube |

---

## Localização dos Dados de Avaliação

Os dados coletados serão organizados e armazenados na seguinte estrutura neste repositório:

- **`/docs/pages/Modulo4/dados/`**: Diretório principal para todos os dados da avaliação
  - **`adequacao_funcional/`**: Resultados das métricas de adequação funcional
    - `Checklist Funcionalidades`: Dados dos requisitos elicitados
    - `Corretude`: 
    - `Pertinencia`: 
  - **`portabilidade/`**: Resultados das métricas de portabilidade
    - `Complexidade Ciclomática`: Dados do SonarQube

  
## Uso de IA
 
Para a elaboração deste documento e de outros artefatos do projeto, foram utilizadas ferramentas de Inteligência Artificial, como o **ChatGPT (OpenAI)** e o **Gemini (Google)**. O uso dessas tecnologias teve como principais objetivos:
 
- **Aprimoramento da Escrita:** Melhorar a clareza, coesão e correção gramatical dos textos, garantindo uma comunicação mais eficaz.
- **Geração de Estruturas:** Auxiliar na criação de estruturas iniciais para seções e tabelas, otimizando o tempo de desenvolvimento.
- **Refinamento de Ideias:** Servir como ferramenta de brainstorming para refinar conceitos e justificativas apresentadas no documento.
- **Consistência Terminológica:** Ajudar a manter a consistência dos termos técnicos utilizados ao longo da documentação.
 
Ressaltamos que todo o conteúdo gerado por IA foi cuidadosamente revisado, editado e validado pelos membros da equipe para assegurar sua precisão, relevância e alinhamento com os objetivos da avaliação de qualidade. As ferramentas foram empregadas como um suporte ao processo de criação, e a responsabilidade final pelo conteúdo permanece com os autores do projeto.

---

## Referências Bibliográfica

> [1] REQUISITOS NÃO FUNCIONAIS. Canal Fatto Consultoria e Sistemas. Publicado em 06 de ago. de 2015. Disponível em: <https://www.youtube.com/watch?v=Gv5H9XgWOJ0>. Acesso em: 17 de nov. de 2025.
> 
> [2] RODRIGUES, Renato. ISO/IEC 25010: Functional Suitability. LinkedIn, 2 de fev. de 2024. Disponível em: <https://pt.linkedin.com/pulse/isoiec-25010-functional-suitability-renato-rodrigues>. Acesso em: 17 de nov. de 2025.
>
> [3] Notas de aula da disciplina de Qualidade de Software: **Conceitos GQM (introdução, planejamento, definição, coleta e interpretação)**.
>
> [4] Qualidade de Software - Visão geral em 20 minutos. Canal Vitor Maia. Publicado em 25 de ago. de 2025. Disponível em: <https://www.youtube.com/watch?v=Gv5H9XgWOJ0>. Acesso em: 17 de nov. de 2025.

---

## Histórico de Versões

| Versão | Descrição | Autor(es) | Data de Produção | Revisor(es) | Data de Revisão | Observações / Incrementos |
|:------:|------------------|------------|:----------------:|--------------|:----------------:|---------------------------|
| `1.0` | Desenvolvimento dos objetivos do GQM. | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 17/11/2025 | — | — | Versão inicial do documento. |
| `1.1` | Inserção das técnicas de medição para a adequação funcional. | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 17/11/2025 | [Mylena Mendonça](https://github.com/MylenaTrindade) | 17/11/2025 | Revisão da ideação do artefato. |
| `1.2` | Inserção das técnicas de medição para a confiabilidade. | [Gustavo Gontijo Lima](https://github.com/Guga301104) | 18/11/2025 | [Ana Luiza Komatsu](https://github.com/luluaroeira) | 18/11/2025 | Revisão da ideação do artefato. |
| `1.3` | Inserção das técnicas de medição para a Manuntenabilidade. | [Pedro Barbosa](https://github.com/pedrobarbosaocb) | 18/11/2025 |  |  |  |
| `1.4` | Realocação da Entrevista com o desenvolvedor para a fase 4 | [Felipe das Neves](https://github.com/FelipeFreire-gf) | | | |  |
| `1.5` | Unificação dos ambientes de testes e instrumentos de medição | [Felipe das Neves](https://github.com/FelipeFreire-gf) | | | |  |
| `1.6` | Correção das contas em confiabilidade | [Felipe das Neves](https://github.com/FelipeFreire-gf) | | | |  |
| `1.7` | Alteração em Manutenibilidade | [Marcos Bittar](https://github.com/Bittarx) | | | |  |
| `1.8` | Remoção do checklist como uma das ferramentas de análise  | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 26/11/2025 | | |  |