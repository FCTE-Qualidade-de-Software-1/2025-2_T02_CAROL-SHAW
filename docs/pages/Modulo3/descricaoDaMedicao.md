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

Aqui vamos descrever todo o passo a passo de como iremos realizar as medições para as perguntas feitas na [Fase 2 - Planejamento de Avaliação](https://fcte-qualidade-de-software-1.github.io/2025-2_T02_CAROL-SHAW/pages/Modulo2/planejamentoDaAvaliacao/#2-metodologia-e-diretrizes-de-medicao):

#### Completude Funcional: todas as funções estão presentes?

- Utilizaremos como insumos a lista de requisitos funcionais (obtida na entrevista) e a análise dos documentos públicos (Tabela 1) para verificar se as funcionalidades especificadas estão implementadas.

#### Correção funcional: os resultados das funções estão corretos?

- Nesta análise, o foco é a precisão dos resultados. Realizaremos testes manuais na aplicação online, inserindo dados de faturas e comparando os resultados gerados pela plataforma com cálculos de referência.

#### Pertinencia Funcional: essas funções de fato ajudam os usuários?

A análise de pertinência busca entender se as funcionalidades existentes são de fato úteis e relevantes para os objetivos dos gestores públicos.

Detalhes a ser pensado:

- **Simulação de Tarefas do Usuário:** Realizar um passo a passo simulando as tarefas de um gestor (ex: cadastrar uma fatura, gerar um relatório de economia) para avaliar se o fluxo de trabalho é lógico e se as funções facilitam a conclusão dessas tarefas.

- **Questionário de Percepção:** Aplicar um questionário direcionado ao desenvolvedor (ou a um usuário-chave, se possível) para coletar feedback qualitativo sobre quais funcionalidades são mais valorizadas e quais poderiam ser otimizadas ou removidas.

---

## Descrição da Medição Para a Confiabilidade




---

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
>
> [4] Qualidade de Software - Visão geral em 20 minutos. Canal Vitor Maia. Publicado em 25 de ago. de 2025. Disponível em: <https://www.youtube.com/watch?v=Gv5H9XgWOJ0>. Acesso em: 17 de nov. de 2025.

---

## Histórico de Versões

| Versão | Descrição | Autor(es) | Data de Produção | Revisor(es) | Data de Revisão | Observações / Incrementos |
|:------:|------------------|------------|:----------------:|--------------|:----------------:|---------------------------|
| `1.0` | Desenvolvimento dos objetivos do GQM. | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 17/11/2025 | — | — | Versão inicial do documento. |
| `1.1` | Inserção das técnicas de medição para a adequação funcional. | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 17/11/2025 | [Mylena Mendonça](https://github.com/MylenaTrindade) | 17/11/2025 | Revisão da ideação do artefato. |