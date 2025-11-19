# Fase 2 - Planejamento da Avaliação

## Sumário

- [1. Objetivos de Medição por GQM](#1-objetivos-de-medicao-por-gqm)
  - [1.1. Adequação Funcional](#11-adequacao-funcional)
    - [Questões e Métricas](#questoes-e-metricas)
    - [Diagrama GQM Adaptado da Adequação Funcional](#diagrama-gqm-adaptado-da-adequacao-funcional)
  - [2. Confiabilidade](#2-confiabilidade)
    - [Questões e Métricas](#questoes-e-metricas-1)
    - [Diagrama GQM Adaptado da Confiabilidade](#diagrama-gqm-adaptado-da-confiabilidade)
  - [3. Manutenibilidade](#3-manutenibilidade)
    - [Questões e Métricas](#questoes-e-metricas-2)
    - [Diagrama GQM da Manutenibilidade](#diagrama-gqm-da-manutenibilidade)
- [Apêndice — Tabela Resumo (Q→M)](#apendice-tabela-resumo-qm)
- [Uso de IA](#uso-de-ia)
- [Bibliografia](#bibliografia)
- [Histórico de Versões](#historico-de-versoes)

---

## 1. Objetivos de Medição por GQM

### 1.1. Adequação Funcional

#### Descrição do Objetivo

| Campo | Descrição |
|---|---|
| **Analisar** | A plataforma MEPA Energia |
| **Para o propósito de** | Avaliar |
| **Com respeito a** | Adequação Funcional |
| **Do ponto de vista de** | Gestores e técnicos |
| **No contexto da** | Gestão de contratos de energia e relatórios |

#### Questões e Métricas

##### **Q1. Em que medida as funcionalidades priorizadas do MEPA foram implementadas?**

Para verificar a completude, utilizaremos a **Cobertura de Requisitos Priorizados (CRP)**. Esta métrica avalia se o escopo essencial para a gestão de contratos de energia foi entregue.

> **Fórmula CRP:**
>
> CRP(%) = (Requisitos Funcionais implementados ÷ Requisitos Funcionais priorizados) × 100
>
> **Conceito base:** Functional Completeness (ISO/IEC 25010) [^1]

**Critérios de Medição e Julgamento:**

  * **Método de Coleta:** Comparação entre o backlog priorizado da release e o *changelog* de funcionalidades entregues e aprovadas pelo Product Owner.
  * **Níveis de Pontuação (Julgamento):**
      * **Desejável:** CRP ≥ 90%
      * **Aceitável:** 75% ≤ CRP \< 90%
      * **Inaceitável:** CRP \< 75%

##### **Q2. Os resultados apresentados pelo MEPA nas funcionalidades críticas estão corretos?**

A corretude será avaliada através da **Taxa de Sucesso em Cenários Críticos (TSC)**, focando em cálculos de energia e geração de relatórios onde erros não são toleráveis.

> **Fórmula TSC:**
>
> TSC(%) = (Cenários concluídos sem desvio ÷ Total de cenários críticos executados) × 100
>
> **Conceito base:** Functional Correctness (ISO/IEC 25010) [^1]

**Critérios de Medição e Julgamento:**

  * **Método de Coleta:** Execução de suíte de testes de aceitação automatizados ou manuais focados em "Caminhos Felizes" e "Casos de Borda" críticos.
  * **Níveis de Pontuação (Julgamento):**
      * **Desejável:** TSC ≥ 95%
      * **Aceitável:** 85% ≤ TSC \< 95%
      * **Inaceitável:** TSC \< 85%

##### **Q3. As funcionalidades implementadas operam em conformidade com o esperado na homologação?**

Avalia-se a **Taxa de Conformidade Funcional (TCF)**, que mede a proporção de funcionalidades que passaram pela verificação sem rejeição por parte dos stakeholders.

> **Fórmula TCF:**
>
> TCF(%) = (Requisitos verificados e aprovados ÷ Requisitos implementados) × 100
>
> **Conceito base:** Functional Appropriateness (ISO/IEC 25010) [^1]

**Critérios de Medição e Julgamento:**

  * **Método de Coleta:** Análise dos relatórios de homologação e tickets de rejeição (bugs abertos durante UAT - User Acceptance Testing).
  * **Níveis de Pontuação (Julgamento):**
      * **Desejável:** TCF ≥ 90%
      * **Aceitável:** 75% ≤ TCF \< 89%
      * **Inaceitável:** TCF \< 75%

#### Diagrama GQM Adaptado da Adequação Funcional

<font size="3">
    <p style="text-align: center">
        <b>Figura 1:</b> Diagrama GQM da Adequação Funcional
        <br>
    </p>
</font>

<div align="center">
  <img src="https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2025-2_T02_CAROL-SHAW/refs/heads/main/docs/pages/Modulo2/assets/DiagramaGQM1.png" alt="Diagrama GQM da adequacao" width="600">
</div>

<font size="3">
    <p style="text-align: center">
        <b>Autor:</b> 
        Gustavo Gontijo Lima
    </p>
</font>

---


### 2. Confiabilidade

#### Descrição do Objetivo

| Campo | Descrição |
|---|---|
| **Analisar** | O MEPA |
| **Para o propósito de** | Avaliar |
| **Com respeito a** | Confiabilidade Operacional |
| **Do ponto de vista de** | Desenvolvedores e DevOps |
| **No contexto da** | Operação em ambiente de produção |

#### Questões e Métricas

##### **Q4. Qual é a estabilidade do sistema em operação normal?**

Será utilizado o **Tempo Médio Entre Falhas (MTBF)** para medir a frequência com que o sistema apresenta interrupções não planejadas.

> **Fórmula MTBF:**
>
> MTBF(horas) = Tempo total de operação ÷ Número de falhas detectadas
>
> **Conceito base:** Maturity / Fault Tolerance (ISO/IEC 25010) [^1]

**Critérios de Medição e Julgamento:**

  * **Método de Coleta:** Monitoramento de logs de aplicação e ferramentas de observabilidade (ex: Prometheus, Datadog) contabilizando *downtimes*.
  * **Níveis de Pontuação (Julgamento):**
      * **Desejável:** MTBF \> 100 horas
      * **Aceitável:** 50 \< MTBF ≤ 100 horas
      * **Inaceitável:** MTBF ≤ 50 horas

##### **Q5. O sistema está disponível quando necessário?**

A **Disponibilidade do Serviço (DS)** medirá a porcentagem de tempo que o MEPA está acessível e operacional para os usuários finais.

> **Fórmula DS:**
>
> DS(%) = (Tempo em operação ÷ Tempo total esperado) × 100
>
> **Conceito base:** Availability (ISO/IEC 25010) [^1]

**Critérios de Medição e Julgamento:**

  * **Método de Coleta:** *Ping tests* automatizados e relatórios de SLA do servidor.
  * **Níveis de Pontuação (Julgamento):**
      * **Desejável:** DS ≥ 99,5%
      * **Aceitável:** 99,0% ≤ DS \< 99,5%
      * **Inaceitável:** DS \< 99,0%

##### **Q6. Quão efetiva é a recuperação após uma falha?**

Utilizaremos o **Tempo Médio para Reparo (MTTR)**, que indica a agilidade da equipe e do sistema em restaurar o serviço após um incidente.

> **Fórmula MTTR:**
>
> MTTR(minutos) = Σ(Tempo de indisponibilidade) ÷ Número de falhas
>
> **Conceito base:** Recoverability (ISO/IEC 25010) [^1]

**Critérios de Medição e Julgamento:**

  * **Método de Coleta:** Diferença de tempo entre o ticket de abertura do incidente e o fechamento/restauração do serviço.
  * **Níveis de Pontuação (Julgamento):**
      * **Desejável:** MTTR \< 15 min
      * **Aceitável:** 15 ≤ MTTR ≤ 60 min
      * **Inaceitável:** MTTR \> 60 min


#### Diagrama GQM Adaptado da Confiabilidade

<font size="3">
    <p style="text-align: center">
        <b>Figura 1:</b> Diagrama GQM da Confiabilidade
        <br>
    </p>
</font>

<div align="center">
  <img src="https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2025-2_T02_CAROL-SHAW/refs/heads/main/docs/pages/Modulo2/assets/DiagramaGQM2.png" alt="Diagrama GQM da adequacao" width="600">
</div>

<font size="3">
    <p style="text-align: center">
        <b>Autor:</b> 
        Gustavo Gontijo Lima
    </p>
</font>

---

### 3. Manutenibilidade

#### Descrição do Objetivo

| Campo | Descrição |
|---|---|
| **Analisar** | O código-fonte do MEPA |
| **Para o propósito de** | Avaliar |
| **Com respeito a** | Facilidade de manutenção |
| **Do ponto de vista de** | Desenvolvedores |
| **No contexto da** | Evolução e correção do software |

#### Questões e Métricas

##### **Q8. A estrutura do código favorece a manutenção?**

Avaliaremos a complexidade através da **Complexidade Ciclomática Média (CCM)** e do acoplamento. Códigos muito complexos são difíceis de testar e evoluir.

> **Fórmula CCM:**
>
> CCM = Valor médio da complexidade ciclomática por módulo crítico
>
> **Conceito base:** Modularity / Analyzability (ISO/IEC 25010) [^1]

**Critérios de Medição e Julgamento:**

  * **Método de Coleta:** Ferramentas de análise estática de código (ex: SonarQube, ESLint Complexity) rodando na pipeline de CI/CD.
  * **Níveis de Pontuação (Julgamento):**
      * **Desejável:** CCM ≤ 10
      * **Aceitável:** 10 \< CCM ≤ 15
      * **Inaceitável:** CCM \> 15

##### **Q9. Qual é a agilidade no fluxo de correção de defeitos?**

O **Lead Time de Correção (LTC)** mede o tempo decorrido entre a identificação de um defeito e sua correção em produção.

> **Fórmula LTC:**
>
> LTC(dias) = Data do Merge da correção − Data de abertura da Issue
>
> **Conceito base:** Modifiability (ISO/IEC 25010) [^1]

**Critérios de Medição e Julgamento:**

  * **Método de Coleta:** Dados extraídos do sistema de gestão de projetos (Jira/GitHub Issues).
  * **Níveis de Pontuação (Julgamento):**
      * **Desejável:** LTC ≤ 3 dias
      * **Aceitável:** 4 ≤ LTC ≤ 7 dias
      * **Inaceitável:** LTC \> 7 dias

##### **Q10. O sistema possui proteção adequada contra regressão?**

A **Cobertura de Testes de Regressão (CTR)** verifica se as modificações no código estão cobertas por testes automatizados, garantindo testabilidade.

> **Fórmula CTR:**
>
> CTR(%) = (Linhas ou branches cobertos por testes ÷ Total de linhas ou branches alterados) × 100
>
> **Conceito base:** Testability (ISO/IEC 25010) [^1]

**Critérios de Medição e Julgamento:**

  * **Método de Coleta:** Relatórios de cobertura de código (Coverage Report) gerados durante o build.
  * **Níveis de Pontuação (Julgamento):**
      * **Desejável:** CTR ≥ 80%
      * **Aceitável:** 70% ≤ CTR \< 80%
      * **Inaceitável:** CTR \< 70%

#### Diagrama GQM da Manutenibilidade

<font size="3">
    <p style="text-align: center">
        <b>Figura 1:</b> Diagrama GQM da Manutenibilidade
        <br>
    </p>
</font>

<div align="center">
  <img src="https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2025-2_T02_CAROL-SHAW/refs/heads/main/docs/pages/Modulo2/assets/DiagramaGQM3.png" alt="Diagrama GQM da adequacao" width="600">
</div>

<font size="3">
    <p style="text-align: center">
        <b>Autor:</b> 
        Gustavo Gontijo Lima
    </p>
</font>

---

## Apêndice — Tabela Resumo (Q→M)

| Objetivo | Questão | Métrica(s) | Fonte | Freq. |
|---|---|---|---|---|
| Adequação | Q1 | AF1, AF4 | Backlog/Homologação | por release |
| Adequação | Q2 | AF2, AF3 | Testes | por release |
| Adequação | Q3 | AF4, AF5 | Homologação | por release |
| Confiabilidade | Q4 | CF1, CF3 | Monitoria/Issues | mensal |
| Confiabilidade | Q5 | CF2 | Monitoria | mensal |
| Confiabilidade | Q6 | CF4 | Monitoria/Issues | mensal |
| Confiabilidade | Q7 | CF5 | Issues | mensal |
| Manutenibilidade | Q8 | MN4, MN5 | Análise Estática | por release |
| Manutenibilidade | Q9 | MN1, MN2 | Issues | por demanda |
| Manutenibilidade | Q10 | MN3 | Testes | por release |

---

## Uso de IA
 
Para a elaboração deste documento e de outros artefatos do projeto, foram utilizadas ferramentas de Inteligência Artificial, como o **ChatGPT (OpenAI)** e o **Gemini (Google)**. O uso dessas tecnologias teve como principais objetivos:
 
- **Aprimoramento da Escrita:** Melhorar a clareza, coesão e correção gramatical dos textos, garantindo uma comunicação mais eficaz.
- **Geração de Estruturas:** Auxiliar na criação de estruturas iniciais para seções e tabelas, otimizando o tempo de desenvolvimento.
- **Refinamento de Ideias:** Servir como ferramenta de brainstorming para refinar conceitos e justificativas apresentadas no documento.
- **Consistência Terminológica:** Ajudar a manter a consistência dos termos técnicos utilizados ao longo da documentação.
 
É importante ressaltar que todo o conteúdo gerado por IA foi cuidadosamente revisado, editado e validado pelos membros da equipe para assegurar sua precisão, relevância e alinhamento com os objetivos da avaliação de qualidade. As ferramentas foram empregadas como um suporte ao processo de criação, e a responsabilidade final pelo conteúdo permanece com os autores do projeto.

---

## Bibliografia

> - Notas de aula da disciplina de Qualidade de Software: **Conceitos GQM (introdução, planejamento, definição, coleta e interpretação)**.

> - Basili, V. R., et al. **GQM+Strategies: Aligning Software Measurement with Business Goals**. *IEEE Computer*, 2010.

> - Slides da disciplina de Qualidade de Software: **As cinco métricas fundamentais para normalização/controle**.

> - Fenton, N., & Bieman, S. **Software Metrics: A Rigorous and Practical Approach** (3rd ed.). CRC Press. (Fundamentos de medição e escalas).

---

## Histórico de Versões

| Versão | Descrição | Autor(es) | Data de Produção | Revisor(es) | Data de Revisão | Observações / Incrementos |
|:------:|--------------------|------------|:----------------:|--------------|:----------------:|---------------------------|
| `1.0` | Desenvolvimento dos objetivos do GQM. | Felipe das Neves | 13/10/2025 | — | — | Versão inicial do documento. |
| `1.1` | Desenvolvimento dos GQMs das características de qualidade escolhidas na Fase 1. | Felipe das Neves | 13/10/2025 | — | — | Complemento da versão 1.0. |
| `1.2` | Inserção das imagens do GQM para cada característica de qualidade. | Felipe das Neves | 13/10/2025 | — | — | — |
| `1.3` | Sintetização dos entregáveis. | Felipe das Neves | 13/10/2025 | — | — | — |
| `1.4` | Modificação da estrutura do GQM 2, seguindo os padrões propostos para melhor coerência entre métricas e objetivos. | Mylena Mendonça | 15/10/2025 | — | — | Complemento técnico, sem aumento de escopo. |
| `1.5` | Modificação da estrutura do GQM 1, para adequações ao padrão solicitado. | Ana Luiza Komatsu | 15/10/2025 | — | — | — |
| `1.6` | Revisão e aprimoramento do GQM-3 para adequação à estrutura GQM (Manutenibilidade). | Pedro Barbosa | 15/10/2025 | — | — | — |
| `1.7` | Ajuste de fórmulas, explicações adicionais e tabela de critérios. | Mylena Mendonça e Ana Luiza Komatsu | 16/10/2025 | Felipe das Neves | — | Ajustes na tabela de critérios e unificação com a tabela de métricas. |
| `1.8` | Adição dos diagramas corrigidos e correção das fórmulas do GQM. | Gustavo Gontijo Lima | 20/10/2025 | Marcos Bittar  | — | Revisão final com ajustes. |
| `1.9` | Reunião para verificação final e validação do documento. | Gustavo Gontijo Lima, Pedro Barbosa e Felipe das Neves | 21/10/2025 | — | — | Versão estável. |
| `2.0` | Reunião para verificação de padronização e histórico de versão. | Felipe das Neves e Mylena Mendonça | 22/10/2025 | — | — | — |
| `2.1` | Reunião para verificação de padronização e histórico de versão. | Felipe das Neves e Mylena Mendonça | 22/10/2025 | — | — | — |
