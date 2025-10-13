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
- [3. Bibliografia (selecionada)](#6-bibliografia-selecionada)

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
- **Fontes**: repositórios MEPA, issues, documentação de release e logs operacionais.
- **Instrumentos**: planilha GQM; cobertura e extração de issues; *checklists* de qualidade de dados (completude/consistência/unicidade).
- **Amostragem**: cenários críticos **cadastro→análise→relatórios**, por ambiente suportado.
- **Ética/privacidade**: anonimização de dados sensíveis de faturas; coleta mínima.

### 2.4 Interpretação e Relato
- Consolidação por **release**: gráficos de tendência (densidade de defeitos, cobertura, tempo de correção, sucesso de cenários).
- Análise de **causas** e recomendações; *backlog* de melhoria priorizado por impacto/risco.

---

## 3. Bibliografia (selecionada)

> - Fenton, N., & Bieman, S. **Software Metrics: A Rigorous and Practical Approach** (3rd ed.). CRC Press.

> - Basili, V. R., et al. **GQM+Strategies**. *IEEE Computer*, 2010.

> - Notas de aula da disciplina de Qualidade de Software: **GQM – Introdução, Planejamento, Definição, Coleta, Interpretação, Exemplo**.

> - Slides da disciplina de Qualidade de Software: **As cinco métricas fundamentais** (Tamanho, Esforço, Duração, Custo, Confiabilidade).

---

## Histórico de Versões

| Versão | Descrição | Autor(es) | Data de Produção | Revisor(es) | Data de Revisão | Incremento do Revisor|
| :----: | --------- | --------- | :--------------: | ----------- | :-------------: | :-------------: |
| `1.0` | Inserção da metodologia planejada para a fase 2 | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 13/10/2025 | | | |