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
- [6. Localização dos Dados de Avaliação](#localização-dos-dados-de-avaliação)
- [7. Cronograma](#cronograma)
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


#### Q2. Os resultados apresentados pelo sistema estão corretos?

- Nesta análise, o foco é a precisão dos resultados. Realizaremos testes manuais na aplicação offline, pois o ambiente offline possue os usuários de maior nível na aplicação ao invés só do convidado, inserindo dados de faturas e comparando os resultados gerados pela plataforma com cálculos de referência.


#### Q3. As funcionalidades implementadas operam em conformidade com o esperado?

- Na análise de pertinência buscamos entender se as funcionalidades existentes são de fato úteis e relevantes para os objetivos dos usuários. Portanto, realizamos um passo a passo simulado das tarefas do gestor como: cadastrar uma fatura e gerar um relatório de economia para avaliarmos o fluxo de trabalho é lógico.

---

## 2. Descrição da Medição Para a Confiabilidade

A **Confiabilidade**, fundamentada na norma ISO/IEC 25010, refere-se à capacidade do produto de software de manter um nível de desempenho especificado quando usado sob condições especificadas.

Para esta avaliação do sistema **MEPA Energia**, a abordagem metodológica adotada é a de **Testes de Caixa Preta (Black Box Testing)**. Nesta abordagem, as medições são realizadas através da interface do usuário e ferramentas de inspeção de navegador (*Browser DevTools*), sem acesso intrusivo ao código-fonte ou banco de dados, auditando a resiliência do sistema sob a ótica da experiência real do usuário.

Focaremos nas seguintes sub-características essenciais:

| Sub-característica | Descrição Técnica (Abordagem Caixa Preta) |
| :--- | :--- |
| **Tolerância a Falhas (Fault Tolerance)** | Capacidade do *front-end* de validar entradas e gerenciar exceções de uso (erros humanos ou dados inválidos) sem colapso da interface ou exposição de erros críticos de execução (*Stack Trace*) no Console do navegador. |
| **Recuperabilidade (Recoverability)** | Capacidade do sistema de preservar o estado da aplicação (*State Management*) e os dados inseridos pelo usuário em caso de interrupção abrupta da sessão (ex: atualização de página ou queda de rede momentânea) antes da submissão. |
| **Disponibilidade (Availability)** | Verificação da latência de resposta inicial, status HTTP e tempo de carregamento da árvore crítica (*DOM*) em ambiente de produção, garantindo que o serviço esteja acessível quando solicitado. |

Mais detalhes sobre o propósito e as perguntas de avaliação podem ser encontrados no planejamento da Fase 2.

### Procedimentos das Análises:

A seguir, detalhamos o passo a passo de como as medições serão realizadas via ferramentas de auditoria *Client-Side*.

#### Tolerância a Falhas: Validação de Entrada e Estabilidade
- **Procedimento:** Execução de testes de submissão de formulários críticos com *payloads* vazios (entradas nulas). Utiliza-se o inspetor de elementos para monitorar a aba **Console** em busca de erros de execução (JavaScript Exceptions) e verifica-se o *feedback* visual imediato ao usuário.
- **Métricas associadas:**
    - **CF1 - Eficácia da Validação (EV):** Capacidade binária do sistema de impedir o envio de requisições inválidas e manter o console livre de erros críticos.

#### Recuperabilidade: Persistência de Rascunho
- **Procedimento:** Simulação de falha de continuidade. O usuário preenche formulários transacionais e força o recarregamento da página (*Hard Refresh* - F5) antes da submissão. Monitora-se a aba **Application > Local Storage** do navegador para verificar se há salvamento temporário dos dados digitados.
- **Métricas associadas:**
    - **CF2 - Taxa de Recuperação de Sessão (TRS):** Proporção de campos recuperados após a atualização da página.

#### Disponibilidade: Performance e Latência
- **Procedimento:** Análise de performance via aba **Network** do DevTools. Mede-se o tempo total de *Load* (carregamento completo) e o código de status HTTP retornado pelo servidor principal após uma limpeza de cache.
- **Métricas associadas:**
    - **CF3 - Tempo de Carregamento (Load Time):** Tempo cronometrado em segundos até a interatividade total da interface.

### Resumo dos Instrumentos de Medição:

| Instrumento | Descrição |
|---|---|
| **Chrome DevTools (Network)** | Utilizado para aferir o Status Code (200 OK) e o tempo exato de carregamento dos recursos (*Waterfall*). |
| **Chrome DevTools (Console)** | Utilizado para monitorar logs de erro, avisos e exceções de JavaScript durante a operação. |
| **Chrome DevTools (Application)** | Utilizado para inspecionar o armazenamento local (*Local Storage*) e verificar a persistência de dados. |
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

## 6. Localização dos Dados de Avaliação

Os dados coletados serão organizados e armazenados na seguinte estrutura neste repositório:

- **`/docs/pages/Modulo4/dados/`**: Diretório principal para todos os dados da avaliação
  - **`adequacao_funcional/`**: Resultados das métricas de adequação funcional
    - `Checklist Funcionalidades`: Dados dos requisitos elicitados
    - `Corretude`: 
    - `Pertinencia`: 
  - **`portabilidade/`**: Resultados das métricas de portabilidade
    - `Complexidade Ciclomática`: Dados do SonarQube

---

## 7. Cronograma 

| Atividade                                                             | Responsável(is)                  | Data       | Status        |
|-----------------------------------------------------------------------|----------------------------------|------------|----------------|
| Gravação com os desenvolvedores no MEPA para a Adq Funcional                             | Felipe das Neves e Mylena Mendonça | 18/11     | Concluído     |
| Elicitação dos requisitos com base no vídeo para a Adq Funcional                           | Felipe das Neves e Mylena Mendonça                          | 19/11     | Concluído     |
| Gravação dos vídeos de testes da adequação funcional                 | Felipe das Neves e Mylena Mendonça                          | 25/11     | Concluído     |
| Análise das métricas para a Adq Funcional                                                 | Felipe das Neves e Mylena Mendonça                          | 25/11     | Concluído     |
| Finalização da Adq Funcional                                                          | Felipe das Neves e Mylena Mendonça                          | 26/11     | Concluído     |


---

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