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

| Campo                  | Descrição                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------|
| **Analisar**            | A plataforma MEPA Energia                                                                  |
| **Para o propósito de** | Avaliar                                                                                    |
| **Com respeito a**      | Adequação Funcional (cobertura e conformidade funcional)                                   |
| **Do ponto de vista de**| Gestores e técnicos de IFES (usuários finais)                                              |
| **No contexto da**      | Gestão de contratos de energia (cadastro, recomendação, relatórios e exportação de dados)  |

#### Goal (Objetivo)
Avaliar se as funcionalidades principais da plataforma MEPA cobrem e executam corretamente as tarefas críticas do processo de gestão de energia, atendendo aos requisitos funcionais definidos e testados.

#### Questions (Questões)
- **Q1.** As funcionalidades essenciais (entrada/validação de dados, recomendação, relatórios, exportação) **cobrem** as necessidades do usuário?  
- **Q2.** O **catálogo de requisitos** observados no diagrama de casos de uso está **implementado** e **verificado por testes** automatizados ou manuais?  
- **Q3.** As funcionalidades implementadas possuem **testes associados e rastreáveis**?

#### Metrics (Métricas)

| ID  | Nome da Métrica                              | Fórmula                                                                                           | Unidade | Fonte                                | Frequência   | Responsável        |
|-----|-----------------------------------------------|---------------------------------------------------------------------------------------------------|---------|----------------------------------------|-------------|--------------------|
| M1  | **Cobertura de funcionalidades priorizadas**  | $$\frac{\text{RF implementados}}{\text{RF priorizados}} \times 100$$               | %       | Backlog / releases                     | Por release | Owner de produto   |
| M2  | **Taxa de sucesso de cenários críticos**      | $$\frac{\text{Cenários concluídos sem desvio}}{\text{Total de cenários executados}} \times 100$$ | % | Testes funcionais / registros de execução | Por release | QA responsável     |
| M3  | **Cobertura de testes por RF**               | $$\frac{\text{RF com teste associado}}{\text{RF implementados}} \times 100$$       | %       | Repositório de testes / CI             | Por release | QA responsável     |

> **Notas formais:**  
> • “RF priorizados” = requisitos funcionais marcados como *in scope* para a release em avaliação.  
> • “Cenário sem desvio” = execução bem-sucedida no ambiente de teste, sem incidentes nem reprocessamento.  
> • “Teste associado” = caso de teste automatizado ou manual vinculado ao requisito no sistema de rastreabilidade.

#### Critérios indicativos (Semáforo)

| Métrica | Verde (OK) | Amarelo (Atenção) | Vermelho (Crítico) |
|---------|------------|--------------------|---------------------|
| M1      | ≥ 90 %     | 75 – 89 %          | < 75 %              |
| M2      | ≥ 95 %     | 85 – 94 %          | < 85 %              |
| M3      | ≥ 85 %     | 70 – 84 %          | < 70 %              |

- Esses limiares foram definidos com base em **práticas de referência de qualidade funcional** e normas de medição de software.  
- Recomenda-se manter histórico de 3 releases para avaliação de tendência.

#### Diagrama GQM

<font size="3">
    <p style="text-align: center">
        <b>Figura 1:</b> Diagrama GQM da Adequação Funcional.
        <br>
    </p>
</font>

<div align="center">
  <img src="https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2025-2_T02_CAROL-SHAW/refs/heads/main/docs/fase2/assets/DiagramaGQM1.png" alt="Diagrama GQM da adequacao" width="600">
</div>

<font size="3">
    <p style="text-align: center">
        <b>Fonte:</b> 
        Gustavo Gontijo Lima
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
Avaliar a confiabilidade operacional do MEPA, considerando a estabilidade e disponibilidade percebida pelos usuários durante o uso do sistema.


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
  <img src="https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2025-2_T02_CAROL-SHAW/refs/heads/main/docs/fase2/assets/DiagramaGQM2.png" alt="Diagrama GQM da confiabilidade" width="600">
</div>

<font size="3">
    <p style="text-align: center">
        <b>Fonte:</b> 
        Gustavo Gontijo Lima
    </p>
</font>

---

### GQM-3 — Manutenibilidade

**Objetivo:** Avaliar a **facilidade de mudança** (correções e evoluções) nos módulos críticos do MEPA, garantindo **testabilidade**, **baixo acoplamento** e **complexidade controlada**, com foco na manutenção contínua da qualidade do código.

<table border="1">
  <tr>
    <td><b>Analisar</b></td>
    <td>o MEPA</td>
  </tr>
  <tr>
    <td><b>Para o propósito de</b></td>
    <td>avaliar</td>
  </tr>
  <tr>
    <td><b>Com respeito a</b></td>
    <td>Manutenibilidade</td>
  </tr>
  <tr>
    <td><b>Do ponto de vista de</b></td>
    <td>desenvolvedores e equipe de manutenção</td>
  </tr>
  <tr>
    <td><b>No contexto da</b></td>
    <td>disciplina de Qualidade de Software</td>
  </tr>
</table>

#### Questões

- **Q5.** Como estão os níveis de **complexidade** e **acoplamento** nos módulos de ingestão, análise e relato?  
- **Q6.** Qual o **lead time de correção** de defeitos priorizados e o **esforço médio por demanda**?  
- **Q7.** Qual o **nível de cobertura de regressão** nos módulos alterados, indicando **testabilidade**?

#### Métricas

| ID  | Nome da Métrica | Fórmula / Definição |
|-----|------------------|----------------------|
| **M5** | Tempo de correção (dias) | Data de merge – Data de abertura do bug         |
| **M6** | Cobertura de regressão (%) | (Linhas/branches cobertos ÷ total) × 100      | 
| **M7** | Esforço por demanda (h) | Horas registradas em correções/evoluções         |
| **M8** | Acoplamento entre módulos (CBO) | Média de dependências por módulo         | 
| **M9** | Complexidade Ciclomática Média (CC) | Valor médio de CC por módulo crítico | 

<font size="3">
    <p style="text-align: center">
        <b>Figura 3:</b> Diagrama GQM da Manutenibilidade.
        <br>
    </p>
</font>

<div align="center">

  <img src="https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2025-2_T02_CAROL-SHAW/refs/heads/main/docs/fase2/assets/DiagramaGQM3.png" alt="Diagrama GQM da Manutenibilidade" width="600">
</div>

<font size="3">
    <p style="text-align: center">
        <b>Fonte:</b> 
        Felipe Freire, com revisão e adesão de Pedro Barbosa
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
| `1.5` | Modificação da estrutura do GQM 1 | [Ana Luiza Komatsu](https://github.com/luluaroeira) | 15/10/2025 | | | |
| `1.6` | Revisão e aprimoramento do GQM-3 (Manutenibilidade) | [Pedro Barbosa](https://github.com/pedrobarbosaocb) | 15/10/2025 | | | |
| `1.7` | Adicionando Diagramas corrigidos e corrigindo formulas GQM 1 | [Gustavo Gontijo Lima](https://github.com/Guga301104) | 20/10/2025 | | | |

