# Planejamento da Avaliação (Fase 2) — MEPA Energia

---
## Sumário
- [1. Contexto e Escopo](#1-contexto-e-escopo)
- [2. Objetivos de Medição por GQM](#2-objetivos-de-medição-por-gqm)
  - [GQM-1 — Adequação Funcional](#gqm-1--adequação-funcional)
  - [GQM-2 — Confiabilidade](#gqm-2--confiabilidade)
  - [GQM-3 — Manutenibilidade](#gqm-3--manutenibilidade)
- [3. Plano de Coleta de Dados](#3-plano-de-coleta-de-dados)
- [4. Riscos e Mitigações](#5-riscos-e-mitigações)
- [5. Entregáveis](#6-entregáveis)
- [Apêndice — Tabela Resumo (Q→M)](#apêndice--tabela-resumo-qm)
- [Referências](#referências)

---

> Baseado no documento da Fase 1 (`propositoDeAvaliacao.md`) e na abordagem GQM (Goal–Question–Metric).

## 1. Contexto e Escopo
- **Sistema analisado:** Plataforma **MEPA Energia** (web), com foco em apoio à **gestão de contratos de energia** em IFES (gestores e técnicos).
- **Características priorizadas:** **Adequação Funcional**, **Confiabilidade**, **Manutenibilidade**.
- **Unidade de análise:** versão estável atual do MEPA e artefatos (código, issues, testes, releases).
- **Processos-alvo (macro):** 

(i) **Cadastro e validação** de faturas/insumos;

(ii) **Análise e recomendação** de contrato;

(iii) **Relatórios e dashboards**; 

(iv) **Exportação/integrações**.

- **Fronteiras:** funcionalidades usadas pelos perfis-alvo; ambiente web suportado; repositórios e documentação públicos do projeto.

---

## 2. Objetivos de Medição por GQM

### GQM-1 — Adequação Funcional

**Objetivo:** Avaliar, do ponto de vista do **gestor/técnico** ou seja o usuário final, o quanto as funções do MEPA **cobrem** e **entregam corretamente** as tarefas-alvo no contexto de gestão pública de energia. 

#### Questões
Q1. As funcionalidades essenciais (entrada/validação de dados, recomendação, relatórios, exportação) **cobrem** as necessidades do usuário?  
Q2. O **catálogo de requisitos** observados no diagrama de casos de uso estão **implementados** e **verificado por testes**?

#### Métricas
- M1. **Cobertura de funcionalidades priorizadas (%)** = RF implementados / RF priorizados × 100.
- M2. **Taxa de sucesso de cenários (%)** = cenários concluídos sem desvio / total × 100.
- M3. **Cobertura de testes por RF (%)** = RF com teste associado / RF implementados × 100.

**Critérios indicativos:** M1 ≥ 90%, M2 ≥ 95% (processo batch determinístico), M3 ≥ 85%, M4 ≥ 70%.


<font size="3">
    <p style="text-align: center">
        <b>Figura 1:</b> Diagrama GQM da Adequação Funcional.
        <br>
    </p>
</font>

<div align="center">
  <img src="https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2025-2_T02_CAROL-SHAW/refs/heads/main/docs/fase2/assets/adequa.png" alt="Diagrama GQM da adequacao" width="600">
</div>

<font size="3">
    <p style="text-align: center">
        <b>Fonte:</b> 
        Felipe das Neves
    </p>
</font>

---

### GQM-2 — Confiabilidade

| Campo                  | Descrição                                |
|-------------------------|------------------------------------------|
| **Analisar**            | O MEPA                      |
| **Para o propósito de** | Avaliar                                  |
| **Com respeito a**      | Confiabilidade operacional                      |
| **Do ponto de vista de**| Desenvolvedores                          |
| **No contexto da**      | Disciplina de Qualidade de Software      |

#### Goal (Objetivo)
Medir a confiabilidade operacional do MEPA nas rotinas de **ingestão e análise**, e a estabilidade percebida pelos usuários.


#### Questions (Questões)
- **Q1.** Qual a **densidade de defeitos (bugs)** em módulos do escopo por unidade de tamanho?  
- **Q2.** Qual a **disponibilidade** do serviço web em horário de expediente?


#### Metrics (Métricas)
- **M4. Densidade de defeitos** = bugs confirmados.  
- **M5. Disponibilidade (%)** = (tempo em operação / tempo total em janela de serviço) × 100.

#### Critérios indicativos:
- Densidade ≤ 0,5 bugs  
- MTBF crescente por release  
- MTTR P50 ≤ 15 min  
- Disponibilidade ≥ 99% em expediente


<font size="3">
    <p style="text-align: center">
        <b>Figura 2:</b> Diagrama GQM da Confiabilidade.
        <br>
    </p>
</font>

<div align="center">
  <img src="https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2025-2_T02_CAROL-SHAW/refs/heads/main/docs/fase2/assets/confiabilidade.png" alt="Diagrama GQM da confiabilidade" width="600">
</div>

<font size="3">
    <p style="text-align: center">
        <b>Fonte:</b> 
        Felipe das Neves
    </p>
</font>

---

### GQM-3 — Manutenibilidade

**Objetivo:** Avaliar a **facilidade de mudança** (correções/evoluções) nos módulos críticos do MEPA, garantindo **testabilidade** e **baixo acoplamento**.

#### Questões
Q1. Como estão **complexidade** e **acoplamento** dos módulos de ingestão/análise/relato?  
Q2. Qual o **lead time de correção** de defeitos priorizados?  

#### Métricas
- M6. **Tempo de correção (dias)** = data merge – data abertura do bug.
- M7. **Cobertura de regressão (%)** nos módulos modificados (linha/branch).
- M8. **Esforço por demanda (h)** = horas registradas por correção/evolução.

**Critérios indicativos:** CC média ≤ 10; P50 tempo de correção ≤ 7 dias; cobertura ≥ 70%; esforço dentro do *budget* por sprint.

<font size="3">
    <p style="text-align: center">
        <b>Figura 3:</b> Diagrama GQM da Manutenibilidade.
        <br>
    </p>
</font>

<div align="center">
  <img src="https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2025-2_T02_CAROL-SHAW/refs/heads/main/docs/fase2/assets/manutenibilidade.png" alt="Diagrama GQM da Manutenibilidade" width="600">
</div>

<font size="3">
    <p style="text-align: center">
        <b>Fonte:</b> 
        Felipe das Neves
    </p>
</font>

---

## 3. Plano de Coleta de Dados

- **Fontes**: repositórios MEPA (código), issues, documentação de releases, registros de disponibilidade.
- **Instrumentos**: planilha GQM, cobertura, extratores de issues.
- **Amostragem**: cenários críticos (cadastro→recomendação→relatório), módulos do escopo.
- **Periodicidade**: por release e por sprint.

## 4. Riscos e Mitigações

- **R1** Rastreabilidade requisito–teste–commit incompleta → política e revisão de *links*.
- **R2** Dados/ambiente heterogêneos → matriz de cenários e ambientes padronizados.
- **R3** Baixa disciplina de apontamento de esforço → definição mínima de apontamento.

## 5. Entregáveis

- Catálogo de métricas, planilha GQM, relatórios por release.

---

## Apêndice — Tabela Resumo (Q→M)
| Objetivo | Questão | Métrica | Fonte | Freq. |
|---|---|---|---|---|
| Adequação | Q1 | M1, M2 | releases | por release |
| Adequação | Q2 | M3 | testes | por release |
| Confiabilidade | Q1 | M4 | issues | mensal |
| Confiabilidade | Q2 | M5 | monitoria | mensal |
| Manutenibilidade | Q1 | M7, M8 | código | por mudança |
| Manutenibilidade | Q2 | M6 | issues | por bug |

---

## Referências
> - Notas de aula da disciplina de Qualidade de Software: **Conceitos GQM (introdução, planejamento, definição, coleta e interpretação)**.

> - Basili, V. R., et al. **GQM+Strategies: Aligning Software Measurement with Business Goals**. *IEEE Computer*, 2010.

> - Slides da disciplina de Qualidade de Software: **As cinco métricas fundamentais para normalização/controle**.

> - Fenton, N., & Bieman, S. **Software Metrics: A Rigorous and Practical Approach** (3rd ed.). CRC Press. (Fundamentos de medição e escalas).

---

## Histórico de Versões

| Versão | Descrição | Autor(es) | Data de Produção | Revisor(es) | Data de Revisão | Incremento do Revisor|
| :----: | --------- | --------- | :--------------: | ----------- | :-------------: | :-------------: |
| `1.0` | Desenvolvimento dos objetivos do gqm| [Felipe das Neves](https://github.com/FelipeFreire-gf) | 13/10/2025 | | | |
| `1.1` | Desenvolvimento dos gqms das caracteristicas de qualidade escolhidas na fase 1 | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 13/10/2025 | | | |
| `1.2` | Inserção das imagens do gqm para cada caracteristica de qualidade | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 13/10/2025 | | | |
| `1.3` | Sintetização dos entregáveis | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 13/10/2025 | | | | 
| `1.4` | Modificação da estrutura do GQM 2 | [Mylena Mendonça](https://github.com/MylenaTrindade) | 15/10/2025 | | | |