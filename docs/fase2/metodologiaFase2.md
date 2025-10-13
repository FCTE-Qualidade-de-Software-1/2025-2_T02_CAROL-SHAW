# Metodologia Fase 2

---
## Sumário
- [1. Visão Geral](#1-visão-geral)
- [2. Processo](#2-processo)
  - [2.1 Planejamento](#21-planejamento)
  - [2.2 Definição (GQM)](#22-definição-gqm)
  - [2.3 Preparação e Coleta](#23-preparação-e-coleta)
  - [2.4 Interpretação e Relato](#24-interpretação-e-relato)
  - [2.5 Governança](#25-governança)
- [3. Instrumentos (templates)](#3-instrumentos-templates)
- [4. Critérios de Aceitação (indicativos)](#4-critérios-de-aceitação-indicativos)
- [5. Riscos e Mitigação](#5-riscos-e-mitigação)
- [6. Bibliografia (selecionada)](#6-bibliografia-selecionada)

---

> Procedimento para executar o Planejamento GQM e medir **Adequação Funcional**, **Confiabilidade** e **Manutenibilidade**.

## 1. Visão Geral
Adotamos **GQM** em quatro macro etapas: **Planejamento → Definição → Coleta → Interpretação**, com governança leve e *checkpoints* por release.

## 2. Processo

### 2.1 Planejamento
1) Reuso do **propósito da Fase 1** como *Goal* raiz e definição de escopo (cenários, módulos e ambientes).
2) Seleção de **métricas fundamentais** (Tamanho/Esforço/Duração/Custo/Confiabilidade) para normalização.
3) Definição de papéis, calendário e critérios indicativos (*traffic lights*).

### 2.2 Definição (GQM)
- Derivar **questões** por objetivo (Adequação, Confiabilidade, Manutenibilidade) e mapear **métricas**: definição, fórmula, unidade, fonte, frequência, responsável, critério.
- Preparar **modelo de interpretação** (limiares, tendências, janelas móveis e normalização por tamanho).

### 2.3 Preparação e Coleta
- **Fontes**: repositórios MEPA, issues/MRs, CI, documentação de release, planilhas de cenário e logs operacionais.
- **Instrumentos**: planilha GQM; scripts para CC, cobertura e extração de issues; roteiros de cenário; *checklists* de qualidade de dados (completude/consistência/unicidade).
- **Amostragem**: cenários críticos **cadastro→análise→relatórios**, por ambiente suportado.
- **Ética/privacidade**: anonimização de dados sensíveis de faturas; coleta mínima.

### 2.4 Interpretação e Relato
- Consolidação por **release**: gráficos de tendência (densidade de defeitos, MTBF/MTTR, cobertura, tempo de correção, sucesso de cenários).
- Análise de **causas** e recomendações; *backlog* de melhoria priorizado por impacto/risco.

### 2.5 Governança
- **Papéis**: Sponsor (professor), Avaliador, Analista de Métricas, Testadores, Observador.
- **Ritos**: *kickoff*, checkpoints quinzenais e *post-mortem* por release.
- **Ferramentas**: Git/Issues/MRs, CI, scripts Python, planilhas e *dashboards*.

## 3. Instrumentos (templates)
- **Catálogo de Métricas** (ID, nome, objetivo, definição, fórmula, unidade, fonte, frequência, responsável, critério).
- **Roteiro de Cenários** (passos, dados, oráculo, oráculo de aceitação, sucesso/falha).
- **Planilha de Sessões** (ambiente, duração, falhas, MTBF/MTTR).

## 4. Critérios de Aceitação (indicativos)
- Adequação: cobertura RF ≥ 90%, precisão recomendação ≥ 95%, sucesso de cenários ≥ 85%, cobertura por RF ≥ 70%.
- Confiabilidade: densidade ≤ 0,5 bugs/KLOC; MTBF↑; MTTR P50 ≤ 15 min; disponibilidade ≥ 99%.
- Manutenibilidade: CC ≤ 10; P50 correção ≤ 7 dias; cobertura regressão ≥ 70%; esforço conforme *budget*.

## 5. Riscos e Mitigação
- Rastro requisito–teste–commit incompleto → fortalecer rastreabilidade.
- Dados heterogêneos/ambientes → matriz de ambientes e VMs padronizadas.
- Falta de apontamento de esforço → política mínima de time tracking.

---

## 6. Bibliografia (selecionada)

> - Fenton, N., & Bieman, S. **Software Metrics: A Rigorous and Practical Approach** (3rd ed.). CRC Press.

> - Basili, V. R., et al. **GQM+Strategies**. *IEEE Computer*, 2010.

> - Notas de aula da disciplina de Qualidade de Software: **GQM – Introdução, Planejamento, Definição, Coleta, Interpretação, Exemplo**.

> - Slides da disciplina de Qualidade de Software: **As cinco métricas fundamentais** (Tamanho, Esforço, Duração, Custo, Confiabilidade).

---

## Histórico de Versões

| Versão | Descrição | Autor(es) | Data de Produção | Revisor(es) | Data de Revisão | Incremento do Revisor|
| :----: | --------- | --------- | :--------------: | ----------- | :-------------: | :-------------: |
| `1.0` | Inserção da metodologia planejada para a fase 2 | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 13/10/2025 | | | |