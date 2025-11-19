# Fase 3 - Descrição da Medição

## Sumário

- [Descrição da Medição Para a Adequação Funcional](#descrição-da-medição-para-a-adequação-funcional)
- [Descrição da Medição Para a Confiabilidade](#descrição-da-medição-para-a-confiabilidade)
- [Descrição da Medição Para a Manutenibilidade](#descrição-da-medição-para-a-manutenibilidade)
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

Aqui vamos descrever todo o passo a passo de como iremos realizar as medições para as perguntas feitas na etapa de planejamento de avaliação: [Fase 2 - Planejamento de Avaliação](https://fcte-qualidade-de-software-1.github.io/2025-2_T02_CAROL-SHAW/pages/Modulo2/planejamentoDaAvaliacao/#2-metodologia-e-diretrizes-de-medicao).

#### Completude Funcional: todas as funções estão presentes?

- Utilizaremos como insumos a lista de requisitos funcionais (obtida na entrevista) e a análise dos documentos públicos (Tabela 1) para verificar se as funcionalidades especificadas estão implementadas.

#### Métricas associadas:

AF1, 

#### Correção funcional: os resultados das funções estão corretos?

- Nesta análise, o foco é a precisão dos resultados. Realizaremos testes manuais na aplicação online, inserindo dados de faturas e comparando os resultados gerados pela plataforma com cálculos de referência.

#### Métricas associadas:

AF3, 

#### Pertinencia Funcional: essas funções de fato ajudam os usuários?

- Na análise de pertinência buscamos entender se as funcionalidades existentes são de fato úteis e relevantes para os objetivos dos usuários. Portanto, realizamos um passo a passo simulado das tarefas do gestor como: cadastrar uma fatura e gerar um relatório de economia para avaliarmos o fluxo de trabalho é lógico.

#### Métricas associadas:

AF4, 


### Ambiente de Teste:
 
Os testes foram executados nos ambientes descritos na tabela abaixo, garantindo a verificação em diferentes configurações:
 
| Componente | Especificação |
|---|---|
| **Sistema Operacional** | Windows 11 e Ubuntu 22.04 LTS |
| **Hardware** | Processador Ryzen 7 Pro 4750U ou superior |
| **Navegador** | Mozilla Firefox (versão mais recente) |

### Resumo dos Instrumentos de Medição:

Para a coleta de dados, foram utilizados os seguintes instrumentos:

| Instrumento | Descrição |
|---|---|
| **Checklist de Funcionalidades** | Documento para verificação da implementação dos requisitos, baseado no escopo da Fase 1 e elicitado na Fase 4. |
| **Ferramenta de Captura de Tela** | Utilizada para registrar evidências estáticas (imagens) de resultados e comportamentos específicos. |
| **Software de Gravação (OBS Studio e Microsoft Teams)** | Utilizado para gravar as sessões de teste em vídeo, documentando o fluxo de interação e entrevistas. |

---

## 2. Descrição da Medição Para a Confiabilidade

A **Confiabilidade**, de acordo com a norma ISO/IEC 25010, é definida como a capacidade de um sistema, produto ou componente de manter seu nível de desempenho sob condições especificadas por um determinado período de tempo. Para a avaliação da qualidade do software, focaremos nas seguintes sub-características essenciais:

| Sub-característica | Descrição Detalhada |
| :--- | :--- |
| **Tolerância a Falhas (Fault Tolerance)** | Capacidade do sistema de operar corretamente e manter um nível de serviço especificado, mesmo na presença de falhas de hardware ou software. Isso inclui a habilidade de evitar a falha completa do sistema. |
| **Recuperabilidade (Recoverability)** | Capacidade do sistema de restabelecer um nível de desempenho especificado e recuperar os dados afetados diretamente após uma falha. O foco é no tempo e na integridade da recuperação. |
| **Disponibilidade (Availability)** | Grau em que um sistema, produto ou componente está operacional e acessível para uso quando solicitado. É frequentemente medida pela proporção de tempo em que o sistema está em um estado operacional. |

Mais detalhes sobre o propósito e as perguntas de avaliação que guiam esta medição podem ser encontrados em: [Fase 1 - Proposito de Avaliação](https://fcte-qualidade-de-software-1.github.io/2025-2_T02_CAROL-SHAW/pages/Modulo1/propositoDeAvaliacao/) e [Fase 2 - Planejamento de Avaliação](https://fcte-qualidade-de-software-1.github.io/2025-2_T02_CAROL-SHAW/pages/Modulo2/planejamentoDaAvaliacao/#2-metodologia-e-diretrizes-de-medicao).

### Procedimentos das Análises:

A seguir, detalhamos o passo a passo de como as medições serão realizadas para responder às perguntas de avaliação definidas na etapa de planejamento.

#### Tolerância a Falhas (Fault Tolerance): o sistema consegue manter a operação em caso de falhas?

- **Procedimento:** Serão simuladas falhas controladas no ambiente de teste, como a interrupção da conexão com o banco de dados e a sobrecarga de requisições (teste de estresse). O objetivo é observar a resposta do sistema: se ele consegue tratar a exceção de forma elegante (e.g., *fallback*, mensagem de erro clara) sem causar a interrupção total do serviço.
- **Métricas associadas:**
    - **CF1 - Taxa de Sobrevivência a Falhas (TSF):** $\frac{\text{Número de falhas simuladas que não resultaram em interrupção total do serviço}}{\text{Total de falhas simuladas}}$

#### Recuperabilidade (Recoverability): o sistema consegue se recuperar de uma falha e restaurar os dados?

- **Procedimento:** Após a simulação de uma falha que cause a interrupção do serviço (e.g., reinicialização abrupta do servidor), serão medidos dois aspectos cruciais: o tempo necessário para o sistema retornar ao estado operacional completo e a integridade dos dados transacionais mais recentes.
- **Métricas associadas:**
    - **CF2 - Tempo Médio de Recuperação (TMR):** $\frac{\text{Tempo total gasto para recuperar o sistema após falhas}}{\text{Número de falhas}}$
    - **CF3 - Índice de Perda de Dados (IPD):** $\frac{\text{Número de transações perdidas durante a falha}}{\text{Total de transações no momento da falha}}$

#### Disponibilidade (Availability): o sistema está acessível e operacional quando necessário?

- **Procedimento:** Será utilizado um script de monitoramento para registrar o tempo de atividade (*uptime*) e inatividade (*downtime*) do sistema em um período de 24 horas. A coleta de dados será realizada em intervalos regulares (e.g., a cada 5 minutos) para garantir a precisão da medição.
- **Métricas associadas:**
    - **CF4 - Disponibilidade Percentual (DP):** $\frac{\text{Tempo total de operação} - \text{Tempo total de inatividade}}{\text{Tempo total de operação}} \times 100$
    - **CF5 - Tempo Médio Entre Falhas (TMEF):** $\frac{\text{Tempo total de operação}}{\text{Número de falhas}}$

### Resumo dos Instrumentos de Medição:

Para a coleta de dados e execução dos procedimentos, serão utilizados os seguintes instrumentos:

| Instrumento | Descrição |
|---|---|
| **Ferramenta de Simulação de Carga (Ex: JMeter)** | Utilizada para gerar requisições em massa e simular sobrecarga no sistema, essencial para testar a Tolerância a Falhas. |
| **Script de Monitoramento de Uptime** | Ferramenta automatizada para registrar o tempo de atividade e inatividade do servidor, fundamental para o cálculo da Disponibilidade. |
| **Cronômetro e Logs do Sistema** | Utilizados para medir o Tempo Médio de Recuperação (TMR) e para a análise detalhada da causa raiz das falhas. |
| **Checklist de Preservação de Dados** | Documento para verificar a integridade e a ausência de perda dos dados transacionais após a recuperação do sistema. |

---

## 3. Descrição da Medição Para a Manutenibilidade




---

## Localização dos Dados de Avaliação

Os dados coletados serão organizados e armazenados na seguinte estrutura neste repositório:

- **`/docs/pages/Modulo4/assets/`**: Diretório principal para todos os dados da avaliação
  - **`adequacao_funcional/`**: Resultados das métricas de adequação funcional
    - `Checklist Funcionalidades`: Dados do TCF e ICF
    - `Testes Correção`: Dados do TCR  
    - `Workflow Tarefas`: Dados do IAT
  - **`portabilidade/`**: Resultados das métricas de portabilidade
    - `Adaptabilidade em Multiplataforma`: Dados do TAM
    - `Instalação de Sistemas`: Dados do TMI e TSI
    - `Migração de projetos`: Dados do IPD
  - **`evidencias/`**: Capturas de tela, vídeos e logs dos testes realizados
  - **`analise/`**: Análises estatísticas e relatórios consolidados

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
| `1.1` | Inserção das técnicas de medição para a confiabilidade. | [Gustavo Gontijo Lima](https://github.com/Guga301104) | 18/11/2025 | [Ana Luiza Komatsu](https://github.com/luluaroeira) | 18/11/2025 | Revisão da ideação do artefato. |
| `1.2` | Realocação da Entrevista com o desenvolvedor para a fase 4 | [Felipe das Neves](https://github.com/FelipeFreire-gf) | | | |  |