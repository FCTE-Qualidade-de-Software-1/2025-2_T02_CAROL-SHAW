# Fase 2 - Planejamento da Avaliação

## Sumário

- [2. Metodologia e Diretrizes de Medição](#2-metodologia-e-diretrizes-de-medicao)
- [3. Objetivos de Medição por GQM](#3-objetivos-de-medicao-por-gqm)
  - [GQM-1 — Adequação Funcional](#gqm-1-adequacao-funcional)
  - [GQM-2 — Confiabilidade](#gqm-2-confiabilidade)
  - [GQM-3 — Manutenibilidade](#gqm-3-manutenibilidade)
- [Apêndice — Tabela Resumo (Q→M)](#apendice-tabela-resumo-qm)
- [Bibliografia](#bibliografia)
- [Histórico de Versões](#historico-de-versoes)

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
| **Do ponto de vista de** | Gestores e técnicos |
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

#### Diagrama GQM da Adequação Funcional

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

#### Diagrama GQM da Confiabilidade

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

### GQM-3 — Manutenibilidade

| Campo | Descrição |
|---|---|
| **Analisar** | O MEPA |
| **Para o propósito de** | Avaliar |
| **Com respeito a** | Manutenibilidade (testabilidade, acoplamento, complexidade) |
| **Do ponto de vista de** | Desenvolvedores e equipe de manutenção |
| **No contexto da** | Disciplina de Qualidade de Software |

**Objetivo**: avaliar **facilidade de mudança** nos módulos críticos (correções/evoluções), mantendo **testabilidade** e **complexidade controlada**.

#### Questões 

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

| Versão | Tipo de Alteração | Descrição Detalhada | Autor(es) | Data de Produção | Revisor(es) | Data de Revisão | Observações / Incrementos |
|:------:|------------------|--------------------|------------|:----------------:|--------------|:----------------:|---------------------------|
| `1.0` | Criação | Desenvolvimento dos objetivos do GQM. | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 13/10/2025 | — | — | Versão inicial do documento. |
| `1.1` | Expansão | Desenvolvimento dos GQMs das características de qualidade escolhidas na Fase 1. | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 13/10/2025 | — | — | Complemento da versão 1.0. |
| `1.2` | Inserção de conteúdo visual | Inserção das imagens do GQM para cada característica de qualidade. | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 13/10/2025 | — | — | — |
| `1.3` | Síntese | Sintetização dos entregáveis. | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 13/10/2025 | — | — | — |
| `1.4` | Reestruturação | Modificação da estrutura do GQM 2, seguindo os padrões propostos para melhor coerência entre métricas e objetivos. | [Mylena Mendonça](https://github.com/MylenaTrindade) | 15/10/2025 | — | — | Complemento técnico, sem aumento de escopo. |
| `1.5` | Reestruturação | Modificação da estrutura do GQM 1, para adequações ao padrão solicitado. | [Ana Luiza Komatsu](https://github.com/luluaroeira) | 15/10/2025 | — | — | — |
| `1.6` | Reestruturação | Revisão e aprimoramento do GQM-3 para adequação à estrutura GQM (Manutenibilidade). | [Pedro Barbosa](https://github.com/pedrobarbosaocb) | 15/10/2025 | — | — | — |
| `1.7` | Complemento | Ajuste de fórmulas, explicações adicionais e tabela de critérios. | [Mylena Mendonça](https://github.com/MylenaTrindade) e [Ana Luiza Komatsu](https://github.com/luluaroeira) | 16/10/2025 | [Felipe das Neves](https://github.com/FelipeFreire-gf) | — | Ajustes na tabela de critérios e unificação com a tabela de métricas. |
| `1.8` | Correção técnica | Adição dos diagramas corrigidos e correção das fórmulas do GQM. | [Gustavo Gontijo Lima](https://github.com/Guga301104) | 20/10/2025 | [Marcos Bittar ](https://github.com/leozinlima) | — | Revisão final com ajustes. |
| `1.9` | Revisão final | Reunião para verificação final e validação do documento. | [Gustavo Gontijo Lima](https://github.com/Guga301104), [Pedro Barbosa](https://github.com/pedrobarbosaocb) e [Felipe das Neves](https://github.com/FelipeFreire-gf) | 21/10/2025 | — | — | Versão estável. |
| `2.0` | Padronização | Reunião para verificação de padronização e histórico de versão. | [Felipe das Neves](https://github.com/FelipeFreire-gf) e [Mylena Mendonça](https://github.com/MylenaTrindade) | 22/10/2025 | — | — | — |
