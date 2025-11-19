# Fase 4 - Execução da Medição

## Sumário

- [Execução da Medição Para a Adequação Funcional](#descrição-da-medição-para-a-adequação-funcional)
- [Execução da Medição Para a Confiabilidade](#descrição-da-medição-para-a-confiabilidade)
- [Execução da Medição Para a Manutenibilidade](#descrição-da-medição-para-a-manutenibilidade)
- [Uso de IA](#uso-de-ia)
- [Referências Bibliográfica](#referências-bibliográfica)
- [Histórico de Versões](#historico-de-versoes)

---

## Execução da Medição Para a Adequação Funcional

Após a entrevista modelamos a seguinte lista para os requisitos funcionais e não funcionais para o nosso estudo:

<font size="3">
    <p style="text-align: center">
        <b>Figura 1:</b> Requisitos funcionais
        <br>
    </p>
</font>

<div align="center">
  <img src="hã" width="600">
</div>

<font size="3">
    <p style="text-align: center">
        <b>Autores:</b> 
        [Felipe das Neves](https://github.com/FelipeFreire-gf) e [Mylena Mendonça](https://github.com/MylenaTrindade)
    </p>
</font>

<font size="3">
    <p style="text-align: center">
        <b>Figura 2:</b> Requisitos não funcionais
        <br>
    </p>
</font>

<div align="center">
  <img src="hã" width="600">
</div>

<font size="3">
    <p style="text-align: center">
        <b>Autores:</b> 
        [Felipe das Neves](https://github.com/FelipeFreire-gf) e [Mylena Mendonça](https://github.com/MylenaTrindade)
    </p>
</font>

Resultados

Melhorias


## Execução da Medição Para a Confiabilidade

A execução da medição de confiabilidade foi realizada no ambiente de teste previamente definido, seguindo rigorosamente os procedimentos detalhados na seção "Descrição da Medição Para a Confiabilidade" (Fase 3).

### Resultados da Tolerância a Falhas (Fault Tolerance)

**Objetivo:** Avaliar a capacidade do sistema de operar corretamente, mesmo na presença de falhas simuladas.

| Falha Simulada | Resultado da Operação | Mensagem de Erro (se houver) | Sobrevivência (Sim/Não) |
| :--- | :--- | :--- | :--- |
| Interrupção da Conexão com o Banco de Dados | O sistema exibiu uma tela de erro genérica e travou a operação. | "Erro de conexão com o servidor." | Não |
| Sobrecarga de Requisições (500 req/s) | O sistema ficou lento, mas não travou. As requisições foram processadas com atraso. | Nenhuma | Sim |
| Reinicialização Abrupta do Servidor Web | O serviço ficou indisponível por 45 segundos. | Nenhuma | Não |

**Métrica CF1 - Taxa de Sobrevivência a Falhas (TSF):**
- Total de Falhas Simuladas: 3
- Falhas que Sobreviveram: 1
- **TSF = 1/3 ≈ 33.33%**

**Análise:** A **Taxa de Sobrevivência a Falhas (TSF)** de 33.33% é considerada baixa. Este resultado indica que o sistema possui **Pontos Únicos de Falha (SPOF)**, especialmente na camada de persistência de dados. A falha na conexão com o banco de dados resultou em uma interrupção total da operação, demonstrando a ausência de um tratamento de exceção robusto ou de um mecanismo de *failover* para componentes críticos.

### Resultados da Recuperabilidade (Recoverability)

**Objetivo:** Avaliar o tempo e a integridade dos dados após uma falha que causou interrupção.

**Cenário de Teste:** Falha simulada de Reinicialização Abrupta do Servidor Web.

| Métrica | Valor Encontrado |
| :--- | :--- |
| **Tempo de Indisponibilidade (Downtime)** | 45 segundos |
| **Tempo de Retorno à Operação (Recovery Time)** | 12 segundos (após o servidor estar online) |
| **Total de Transações Perdidas** | 0 |
| **Total de Transações no Momento da Falha** | 10 |

**Métrica CF2 - Tempo Médio de Recuperação (TMR):**
- **TMR = 12 segundos**

**Métrica CF3 - Índice de Perda de Dados (IPD):**
- **IPD = 0/10 = 0%**

**Análise:** O sistema demonstrou uma excelente capacidade de **Recuperabilidade de Dados**, com um **Índice de Perda de Dados (IPD)** de 0%. Isso sugere que as transações são commitadas de forma eficiente ou que há um mecanismo de *rollback* eficaz. O **Tempo Médio de Recuperação (TMR)** de 12 segundos é aceitável, mas o tempo total de indisponibilidade (45 segundos) reforça a necessidade de melhorias na Tolerância a Falhas para evitar a interrupção inicial.

### Resultados da Disponibilidade (Availability)

**Objetivo:** Avaliar o grau em que o sistema está operacional e acessível.

**Período de Monitoramento:** 24 horas (1440 minutos).

| Métrica | Valor Encontrado |
| :--- | :--- |
| **Tempo Total de Operação** | 1440 minutos |
| **Tempo Total de Inatividade (Downtime)** | 45 segundos (0.75 minutos) |
| **Número de Falhas** | 1 (a falha simulada de reinicialização) |

**Métrica CF4 - Disponibilidade Percentual (DP):**
- $DP = \frac{1440 - 0.75}{1440} \times 100$
- $DP = 99.95\%$

**Métrica CF5 - Tempo Médio Entre Falhas (TMEF):**
- $TMEF = \frac{1440 \text{ minutos}}{1 \text{ falha}}$
- **TMEF = 1440 minutos (24 horas)**

**Análise:** A **Disponibilidade Percentual (DP)** de 99.95% é um resultado positivo. O **Tempo Médio Entre Falhas (TMEF)** de 24 horas reflete o período de monitoramento. Embora o sistema demonstre ser altamente disponível em condições normais, a vulnerabilidade a falhas de infraestrutura (conforme observado na Tolerância a Falhas) indica que a alta disponibilidade atual depende de um ambiente estável e não de mecanismos internos de resiliência.

---

## Conclusão da Avaliação de Confiabilidade

A avaliação de confiabilidade revela uma dicotomia importante: o sistema é **altamente recuperável** em termos de dados (IPD de 0%) e **disponível** (99.95%) em um cenário de falha única, mas possui **baixa tolerância a falhas** (TSF de 33.33%).

**Recomendação Principal:** A implementação de mecanismos de tratamento de exceção mais robustos e a adoção de arquitetura de alta disponibilidade (e.g., *failover* de banco de dados, balanceamento de carga) são cruciais para evitar que falhas em componentes críticos causem interrupção total do serviço, elevando assim a Tolerância a Falhas e garantindo a Confiabilidade a longo prazo.


## Descrição da Medição Para a Manutenibilidade

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

---

## Histórico de Versões

| Versão | Descrição | Autor(es) | Data de Produção | Revisor(es) | Data de Revisão | Observações / Incrementos |
|:------:|------------------|------------|:----------------:|--------------|:----------------:|---------------------------|
| `1.0` | Desenvolvimento dos objetivos do GQM. | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 17/11/2025 | — | — | Versão inicial do documento. |
| `1.1` | Inserção do que executamos para o artefato da adequação funcional. | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 17/11/2025 | [Mylena Mendonça](https://github.com/MylenaTrindade) | 17/11/2025 | Revisão da ideação do artefato. |
| `1.2` | Inserção do que executamos para o artefato da confiabilidade. | [Gustavo Gontijo Lima](https://github.com/Guga301104) | 18/11/2025 | [Ana Luiza Komatsu](https://github.com/luluaroeira) | 18/11/2025 | Revisão da ideação do artefato. |