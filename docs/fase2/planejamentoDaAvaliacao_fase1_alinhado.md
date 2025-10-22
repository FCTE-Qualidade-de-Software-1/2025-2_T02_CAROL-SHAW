## Sumário

- [1. Contexto e Escopo](#1-contexto-e-escopo)
- [2. Metodologia e Diretrizes de Medição](#2-metodologia-e-diretrizes-de-medição)
- [3. Objetivos de Medição por GQM](#3-objetivos-de-medição-por-gqm)
  - [GQM-1 — Adequação Funcional](#gqm-1--adequação-funcional)
  - [GQM-2 — Confiabilidade](#gqm-2--confiabilidade)
  - [GQM-3 — Manutenibilidade](#gqm-3--manutenibilidade)
- [4. Plano de Coleta de Dados](#4-plano-de-coleta-de-dados)
- [5. Riscos e Mitigações](#5-riscos-e-mitigações)
- [6. Entregáveis](#6-entregáveis)
- [Apêndice — Tabela Resumo (Q→M)](#apêndice--tabela-resumo-qm)
- [Referências](#referências)
- [Histórico de Versões](#histórico-de-versões)

---

## 2. Metodologia e Diretrizes de Medição

- **Abordagem:** GQM (Goal–Question–Metric). Primeiro define-se **propósito/objetivo**, depois **questões** e **só então** as **métricas** (evitar “respostas na pergunta”).  
- **Conhecer a métrica (passos de leitura/uso):**
  1. Identificar **unidade** e **período** de coleta.  
  2. Comparar com **critérios** (limiares padronizados).  
  3. Analisar **tendências** (histórico por release/sprint).  
  4. Investigar **discrepâncias** (logs, ambiente, dados).  
  5. **Contextualizar** os resultados (versão, SO, hardware, dataset, cenários).

---

## 3. Objetivos de Medição por GQM

### GQM-1 — Adequação Funcional

| Campo | Descrição |
|---|---|
| **Analisar** | A plataforma MEPA Energia |
| **Para o propósito de** | Avaliar |
| **Com respeito a** | Adequação Funcional (cobertura e conformidade funcional) |
| **Do ponto de vista de** | Gestores e técnicos de IFES (usuários finais) |
| **No contexto da** | Gestão de contratos de energia (cadastro, recomendação, relatórios e exportação de dados) |

**Objetivo**: verificar se as **funcionalidades críticas** cobrem e executam corretamente as tarefas priorizadas, com rastreabilidade e verificação formal.

#### Questões 

- **Q1. Cobertura de funcionalidade priorizada** — *O que se deseja saber:* se os requisitos priorizados para a release foram de fato implementados. *O que será medido:* proporção de requisitos priorizados implementados e aprovados em homologação. *Hipótese:* a maioria dos requisitos priorizados está implementada e aprovada.
- **Q2. Evidência e rastreabilidade de teste** — *O que se deseja saber:* se há casos de teste associados aos requisitos e se os cenários críticos executam sem desvio. *O que será medido:* existência de vínculo requisito→teste, taxa de sucesso em cenários críticos. *Hipótese:* cenários críticos executam majoritariamente sem desvio e há vínculo requisito→teste.
- **Q3. Conformidade funcional** — *O que se deseja saber:* se as funcionalidades implementadas operam conforme o esperado pelos stakeholders. *O que será medido:* proporção de requisitos implementados que foram **verificados e aprovados**. *Hipótese:* alta conformidade funcional por release.

#### Métricas, Critérios e Pontuação

| ID | Métrica | Fórmula | Unidade | Fonte | Frequência | Critérios (Verde / Amarelo / Vermelho) |
|---|---|---|---|---|---|---|
| AF1 | Cobertura de requisitos priorizados | (RF implementados ÷ RF priorizados) × 100 | % | Backlog/releases | por release | ≥90 / 75–89 / <75 |
| AF2 | Sucesso de cenários críticos | (Cenários concluídos sem desvio ÷ Total executados) × 100 | % | Execução de testes | por release | ≥95 / 85–94 / <85 |
| AF3 | Cobertura de testes por requisito | (RF com teste associado ÷ RF implementados) × 100 | % | Repositório/CI | por release | ≥85 / 70–84 / <70 |
| AF4 | Conformidade funcional | (RF verificados e aprovados ÷ RF implementados) × 100 | % | Homologação | por release | ≥90 / 75–89 / <75 |
| AF5 | Rejeição em homologação | (RF rejeitados ÷ RF implementados) × 100 | % | Homologação | por release | <5 / 5–15 / >15 |

> **Notas:** “RF verificados e aprovados” = requisitos que passaram na validação e foram aceitos; manter histórico mínimo de 3 releases para tendência.

---

### GQM-2 — Confiabilidade

| Campo | Descrição |
|---|---|
| **Analisar** | O MEPA |
| **Para o propósito de** | Avaliar |
| **Com respeito a** | Confiabilidade operacional |
| **Do ponto de vista de** | Desenvolvedores |
| **No contexto da** | Disciplina de Qualidade de Software |

**Objetivo**: avaliar **estabilidade**, **disponibilidade** e **recuperação** do serviço em produção.

#### Questões

- **Q4. Estabilidade em operação normal** — *O que se deseja saber:* se a frequência de falhas em uso normal é baixa. *O que será medido:* ocorrências de falha por hora de operação e tempo médio entre falhas. *Hipótese:* baixa frequência de falhas e MTBF alto.
- **Q5. Disponibilidade percebida** — *O que se deseja saber:* se o serviço está disponível quando necessário. *O que será medido:* disponibilidade percentual na janela de serviço e/ou disponibilidade teórica (MTBF/(MTBF+MTTR)). *Hipótese:* alta disponibilidade.
- **Q6. Efetividade de recuperação** — *O que se deseja saber:* quão rápido e com que sucesso o serviço é restaurado após uma falha. *O que será medido:* tempo médio de recuperação e taxa de restauração bem-sucedida. *Hipótese:* recuperação rápida com alta taxa de sucesso.
- **Q7. Severidade e impacto** — *O que se deseja saber:* distribuição de incidentes por severidade. *O que será medido:* contagem/percentual por níveis (Crítico/Alto/Médio/Baixo). *Hipótese:* baixa incidência de níveis Crítico/Alto.

#### Métricas, Critérios e Pontuação

| ID | Métrica | Definição/Fórmula | Unidade | Fonte | Frequência | Critérios (Verde / Amarelo / Vermelho) |
|---|---|---|---|---|---|---|
| CF1 | Taxa de falhas | Nº de falhas ÷ tempo total de operação | falhas/h | Monitoria/Issues | mensal | <0,01 / 0,01–0,05 / >0,05 |
| CF2 | Disponibilidade | (Tempo em operação ÷ Tempo esperado) × 100 | % | Monitoria | mensal | ≥99,5 / 99,0–99,49 / <99,0 |
| CF3 | MTBF | Tempo entre falhas | horas | Monitoria | mensal | >100 / 50–100 / <50 |
| CF4 | MTTR | Tempo para restaurar serviço | min | Monitoria/Issues | mensal | <15 / 15–60 / >60 |
| CF5 | Severidade de incidentes | Distribuição por nível | contagem/% | Issues | mensal | manter baixa proporção de níveis Crítico/Alto |

---

### GQM-3 — Manutenibilidade

| Campo | Descrição |
|---|---|
| **Analisar** | O MEPA |
| **Para o propósito de** | Avaliar |
| **Com respeito a** | Manutenibilidade (testabilidade, acoplamento, complexidade) |
| **Do ponto de vista de** | Desenvolvedores e equipe de manutenção |
| **No contexto da** | Disciplina de Qualidade de Software |

**Objetivo**: avaliar **facilidade de mudança** nos módulos críticos (correções/evoluções), mantendo **testabilidade** e **complexidade controlada**.

#### Questões (sem nome de métrica)

- **Q8. Estrutura do código** — *O que se deseja saber:* se níveis de acoplamento e complexidade estão sob controle. *O que será medido:* acoplamento entre módulos e complexidade ciclomática média. *Hipótese:* baixos níveis de acoplamento e CC dentro dos limites.
- **Q9. Fluxo de manutenção** — *O que se deseja saber:* tempo/esforço para corrigir defeitos priorizados. *O que será medido:* tempo entre abertura e merge de correções e esforço registrado por demanda. *Hipótese:* correções com lead time e esforço compatíveis com o SLA do time.
- **Q10. Testabilidade de regressão** — *O que se deseja saber:* cobertura de testes de regressão nos módulos alterados. *O que será medido:* cobertura por linhas/branches em módulos modificados. *Hipótese:* alta cobertura de regressão.

#### Métricas, Critérios e Pontuação

| ID | Métrica | Definição/Fórmula | Unidade | Fonte | Frequência | Critérios (Verde / Amarelo / Vermelho) |
|---|---|---|---|---|---|---|
| MN1 | Tempo de correção | Data de merge − data de abertura do bug | dias | Issues/Repo | por demanda | ≤3 / 4–7 / >7 |
| MN2 | Esforço por demanda | Horas registradas | h | Timesheet/Issues | por demanda | ≤8 / 9–16 / >16 |
| MN3 | Cobertura de regressão | (Linhas/branches cobertos ÷ total) × 100 | % | CI/Testes | por release | ≥80 / 70–79 / <70 |
| MN4 | Acoplamento (CBO) | Média de dependências por módulo | — | Análise estática | por release | ≤9 / 10–12 / >12 |
| MN5 | Complexidade ciclomática média | Valor médio por módulo crítico | — | Análise estática | por release | ≤10 / 11–15 / >15 |

---

## 4. Plano de Coleta de Dados

- **Fontes**: repositórios MEPA (código), issues, documentação de releases, registros de disponibilidade.  
- **Instrumentos**: planilha GQM, relatórios de cobertura, extratores de issues/monitoria.  
- **Amostragem**: cenários críticos (cadastro→recomendação→relatório) e módulos do escopo.  
- **Periodicidade**: por release e por sprint.

## 5. Riscos e Mitigações

- **R1** Rastreabilidade requisito–teste–commit incompleta → política e revisão de links.  
- **R2** Dados/ambiente heterogêneos → matriz de cenários e ambientes padronizados.  
- **R3** Baixa disciplina de apontamento de esforço → definição mínima de apontamento.

## 6. Entregáveis

- Catálogo de métricas, planilha GQM, relatórios por release.

---

## Apêndice — Tabela Resumo (Q→M)
| Objetivo | Questão | Métrica(s) | Fonte | Freq. |
|---|---|---|---|---|
| Adequação | Q1 | AF1, AF4 | Backlog/Homologação | por release |
| Adequação | Q2 | AF2, AF3 | Testes/CI | por release |
| Adequação | Q3 | AF4, AF5 | Homologação | por release |
| Confiabilidade | Q4 | CF1, CF3 | Monitoria/Issues | mensal |
| Confiabilidade | Q5 | CF2 | Monitoria | mensal |
| Confiabilidade | Q6 | CF4 | Monitoria/Issues | mensal |
| Confiabilidade | Q7 | CF5 | Issues | mensal |
| Manutenibilidade | Q8 | MN4, MN5 | Análise Estática | por release |
| Manutenibilidade | Q9 | MN1, MN2 | Issues/Timesheet | por demanda |
| Manutenibilidade | Q10 | MN3 | CI/Testes | por release |

---

## Uso de IA
 
Para a elaboração deste documento e de outros artefatos do projeto, foram utilizadas ferramentas de Inteligência Artificial, como o **ChatGPT (OpenAI)** e o **Gemini (Google)**. O uso dessas tecnologias teve como principais objetivos:
 
- **Aprimoramento da Escrita:** Melhorar a clareza, coesão e correção gramatical dos textos, garantindo uma comunicação mais eficaz.
- **Geração de Estruturas:** Auxiliar na criação de estruturas iniciais para seções e tabelas, otimizando o tempo de desenvolvimento.
- **Refinamento de Ideias:** Servir como ferramenta de brainstorming para refinar conceitos e justificativas apresentadas no documento.
- **Consistência Terminológica:** Ajudar a manter a consistência dos termos técnicos utilizados ao longo da documentação.
 
É importante ressaltar que todo o conteúdo gerado por IA foi cuidadosamente revisado, editado e validado pelos membros da equipe para assegurar sua precisão, relevância e alinhamento com os objetivos da avaliação de qualidade. As ferramentas foram empregadas como um suporte ao processo de criação, e a responsabilidade final pelo conteúdo permanece com os autores do projeto.

---

## Referências
- Documento de **Fase 1 (Propósito de Avaliação)** como contexto normativo da Fase 2.
- Basili, V. R., et al. **GQM+Strategies: Aligning Software Measurement with Business Goals**. *IEEE Computer*, 2010.  
- Fenton, N., & Bieman, J. **Software Metrics: A Rigorous and Practical Approach** (3rd ed.). CRC Press.  
- ISO/IEC 25000 e 25010 — **SQuaRE**: modelos de qualidade e medição.  
- Notas de aula da disciplina de Qualidade de Software (GQM: introdução, planejamento, coleta e interpretação).

---

## Histórico de Versões
| Versão | Descrição | Autor(es) | Data |
|:--:|---|---|:--:|
| 2.1 | Alinhamento explícito com Fase 1 (público-alvo, prioridades, ODS, COTS) e inclusão da seção 0.8 de traço | ChatGPT + Equipe | 22/10/2025 |
| 2.0 | Revisão estrutural: inclusão de hipóteses por questão; diretrizes “Conhecer a métrica”; reformulação das perguntas; padronização de critérios; atualização do apêndice | ChatGPT + Equipe | 22/10/2025 |
