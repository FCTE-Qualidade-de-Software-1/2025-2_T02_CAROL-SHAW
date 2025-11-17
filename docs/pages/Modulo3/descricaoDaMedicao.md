# Fase 3 - Descrição da Medição

## Sumário

- [Descrição da Medição Para a Adequação Funcional](#descrição-da-medição-para-a-adequação-funcional)
- [Descrição da Medição Para a Confiabilidade](#descrição-da-medição-para-a-confiabilidade)
- [Descrição da Medição Para a Manutenibilidade](#descrição-da-medição-para-a-manutenibilidade)
- [Uso de IA](#uso-de-ia)
- [Referências Bibliográfica](#referências-bibliográfica)
- [Histórico de Versões](#historico-de-versoes)

---

## Descrição da Medição Para a Adequação Funcional

Afim de permear nossa proposta inicial de abringir os escopos planejados para a adequação funcional:

   - Completude Funcional: todas as funções estão presentes?

   - Correção funcional: os resultados das funções estão corretos?

   - Pertinencia Funcional: essas funções de fato ajudam os usuários?

Mais detalhes em: [Fase 1 - Proposito de Avaliação](https://fcte-qualidade-de-software-1.github.io/2025-2_T02_CAROL-SHAW/pages/Modulo1/propositoDeAvaliacao/)

Nossa análise foram utilizados os seguintes artefatos na documentação pública do produto:

<font size="3">
    <p style="text-align: center">
        <b>Tabela 1:</b> Documentos analisados do Mepa
        <br>
    </p>
</font>

| Artefato | Descrição | Link |
|---|---|---|
| **Diagrama de Caso de Uso** | Descreve as interações entre os usuários (atores) e o sistema, detalhando as funcionalidades sob a perspectiva do usuário. | [Acessar](https://lappis-unb.gitlab.io/projetos-energia/mec-energia/documentacao/arquitetura/casos_de_uso) |
| **Diagrama de Arquitetura** | Apresenta a estrutura geral do sistema, seus principais componentes e como eles se comunicam e interagem entre si. | [Acessar](https://lappis-unb.gitlab.io/projetos-energia/mec-energia/documentacao/arquitetura/arquitetura) |
| **Diagrama de Infraestrutura** | Detalha a configuração de hardware e software onde o sistema opera, incluindo servidores, redes e outros elementos de infraestrutura. | [Acessar](https://gitlab.com/lappis-unb/projetos-energia/mepa/mepa-infrao) |

<font size="3">
    <p style="text-align: center">
        <b>Autor:</b> 
        [Felipe das Neves](https://github.com/FelipeFreire-gf)
    </p>
</font>

Esses foram os elementos encontrados na documentação, contudo, como estudado na referência <sup>[1]</sup> e <sup>[4]</sup>, o ideal é a utilização de requisitos funcionais para a completude da análise. Portanto, solicitamos uma entrevista com um dos desenvolvedores do produto: [Gabriel Ferreira](https://gitlab.com/oo7gabriel) para nos ajudar a melhor entender a aplicação e modelar de maneira mais completa esse artefato.

<a href="https://youtu.be/4CvQMOwoJzA" target="_blank">
    <p align="center"><strong>Entrevista com o desenvolvedor</strong></p>
</a>
<p align="center">
  <a href="https://youtu.be/4CvQMOwoJzA4" target="_blank">
    <img src="https://img.youtube.com/vi/4CvQMOwoJzA/0.jpg" alt="Vídeo 01" width="480">
  </a>
</p>

<font size="3">
    <p style="text-align: center">
        <b>Autores:</b> 
        [Felipe das Neves](https://github.com/FelipeFreire-gf) e [Mylena Mendonça](https://github.com/MylenaTrindade)
    </p>
</font>

### Procedimentos das Análises:

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
| **Software de Gravação (OBS Studio)** | Utilizado para gravar as sessões de teste em vídeo, documentando o fluxo de interação. |

---

## Descrição da Medição Para a Confiabilidade




---

## Descrição da Medição Para a Manutenibilidade


## Descrição da Medição Para a Manutenibilidade

A medição da Manutenibilidade é crucial para garantir a longevidade e a adaptabilidade do software MEPA, que é um projeto de código aberto e em constante evolução. Conforme definido no Planejamento de Avaliação (Fase 2), o foco está em avaliar a facilidade com que o sistema pode ser analisado, modificado e testado.

Nossa análise será baseada no acesso ao código-fonte e aos dados de gestão de projetos, conforme detalhado nos artefatos abaixo:

<font size="3">
    <p style="text-align: center">
        <b>Tabela X:</b> Documentos e Artefatos Analisados para Manutenibilidade
    </p>
</font>

| Artefato | Descrição | Link/Localização |
|---|---|---|
| **Repositório de Código-Fonte** | O código-fonte completo do projeto MEPA, essencial para a análise estática. | [Link para o Repositório Git] |
| **Sistema de Gestão de Issues** | Plataforma utilizada para rastrear defeitos e tarefas de manutenção (Lead Time de Correção). | [Link para o GitHub Issues/Jira] |
| **Relatórios de Cobertura de Testes** | Documentos gerados pelo CI/CD que indicam a cobertura de código por testes automatizados. | [Link para o Relatório de Cobertura] |

### Procedimentos das Análises:

Aqui descrevemos o passo a passo de como serão realizadas as medições para as questões de Manutenibilidade definidas na Fase 2.

#### Q8. A estrutura do código favorece a manutenção? (Complexidade Ciclomática Média - CCM)

- **Procedimento:** Utilizaremos a ferramenta de análise estática [Nome da Ferramenta, ex: SonarQube] para calcular a Complexidade Ciclomática (CC) em todos os módulos considerados críticos (ex: módulos de cálculo de faturas e geração de relatórios). A **CCM** será calculada como a média dos valores de CC para estas funções/módulos.
- **Métricas associadas:** MN4 (Complexidade Ciclomática), MN5 (Acoplamento).

#### Q9. Qual é a agilidade no fluxo de correção de defeitos? (Lead Time de Correção - LTC)

- **Procedimento:** Serão extraídos dados do [Nome do Sistema de Issues, ex: GitHub Issues] para um período de [X meses]. O **LTC** será calculado para uma amostra de [Y] defeitos críticos, medindo o tempo entre a abertura da *issue* e o *merge* da correção em produção.
- **Métricas associadas:** MN1 (Tempo de Resolução de Defeitos), MN2 (Tempo de Entrega de Correção).

#### Q10. O sistema possui proteção adequada contra regressão? (Cobertura de Testes de Regressão - CTR)

- **Procedimento:** O relatório de cobertura de código gerado pelo [Nome da Ferramenta de Cobertura, ex: JaCoCo, Coverage.py] será analisado. A **CTR** será calculada com base na cobertura de *branches* (ramificações) e linhas de código, focando nas áreas que sofreram modificações recentes.
- **Métricas associadas:** MN3 (Cobertura de Testes).

### Ambiente de Análise:
 
Os procedimentos de análise serão executados nos ambientes e com as ferramentas descritas na tabela abaixo:
 
| Componente | Especificação |
|---|---|
| **Ferramenta de Análise Estática** | [Nome e Versão da Ferramenta, ex: SonarQube 9.9 LTS] |
| **Sistema de Versionamento** | [Nome, ex: Gitlab/GitHub] |
| **Linguagem de Programação** | [Linguagem do Projeto, ex: Python 3.10] |

### Resumo dos Instrumentos de Medição:

Para a coleta de dados, foram utilizados os seguintes instrumentos:

| Instrumento | Descrição |
|---|---|
| **Relatório de Análise Estática** | Documento gerado pela ferramenta [Nome da Ferramenta] contendo as métricas de código (CCM, Coesão, Acoplamento). |
| **Query de Issues** | Consulta estruturada no [Sistema de Issues] para extrair os dados de tempo de vida dos defeitos (LTC). |
| **Relatório de Cobertura de Código** | Documento que detalha o percentual de código coberto por testes automatizados (CTR). |

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