# Fase 4 - Execução da Medição

## Sumário

- [Organização da Equipe](#Organização-da-Equipe)
- [1. Execução da Medição Para a Adequação Funcional](#1-execucao-da-medicao-para-a-adequacao-funcional)
  - [1.1 Execução Etapa 1 - Realização da Entrevista](#11-execucao-etapa-1-realizacao-da-entrevista)
  - [1.2 Execução Etapa 2 - Análise se o sistema possui tudo que foi listado nos requisitos funcionais](#12-execucao-etapa-2-analise-se-o-sistema-possui-tudo-que-foi-listado-nos-requisitos-funcionais)
    - [1.2.1 Execução Etapa 2 - Resultados da análise](#121-execucao-etapa-2-resultados-da-analise)
  - [1.3 Conclusão da Medição da Adequação Funcional](#13-conclusao-da-medicao-da-adequacao-funcional)
- [2. Execução da Medição Para a Confiabilidade](#2-execucao-da-medicao-para-a-confiabilidade)
  - [Resultados da Tolerância a Falhas (Fault Tolerance)](#resultados-da-tolerancia-a-falhas-fault-tolerance)
  - [Resultados da Recuperabilidade (Recoverability)](#resultados-da-recuperabilidade-recoverability)
  - [Resultados da Disponibilidade (Availability)](#resultados-da-disponibilidade-availability)
- [Conclusão da Avaliação de Confiabilidade](#conclusao-da-avaliacao-de-confiabilidade)
- [3. Descrição da Medição Para a Manutenibilidade](#3-descricao-da-medicao-para-a-manutenibilidade)
- [Uso de IA](#uso-de-ia)
- [Referências Bibliográfica](#referências-bibliográfica)
- [Histórico de Versões](#historico-de-versoes)

---

## Organização da Equipe

Dividimos os trabalhos em duplas para a realização das tarefas, conforme pode ser observado na Tabela 1 a seguir:

<font size="3">
    <p style="text-align: center">
        <b>Tabela 1:</b> Divisão de Tarefas por Dupla
    </p>
</font>

<div align="center">
  <table>
    <thead>
      <tr>
        <th>Característica de Qualidade</th>
        <th>Dupla Responsável</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Adequação Funcional</td>
        <td>Felipe das Neves e Mylena Mendonça</td>
      </tr>
      <tr>
        <td>Confiabilidade</td>
        <td>Ana Luiza Komatsu e Gustavo Gontijo</td>
      </tr>
      <tr>
        <td>Manutenibilidade</td>
        <td>Pedro Barbosa e Marcos Bittar</td>
      </tr>
    </tbody>
  </table>
</div>

## 1. Execução da Medição Para a Adequação Funcional

### 1.1 Execução Etapa 1 - Realização da Entrevista Para o Levantamento dos Requisitos

Nessa primeira etapa fizemos a entrevista com os desenvolvedores para elaborarmos os requisitos funcionais da aplicação, segue as perguntas que utilizamos:

!!! Tip "Atenção!"
    Para visualizar as perguntas basta clicar na barra azul abaixo com o texto: "Perguntas utilizadas para a entrevista" nele também está disponível o link para visualizar em uma nova aba e fazer o download do pdf.


??? info "Perguntas utilizadas para a entrevista "

    <a href="https://publuu.com/flip-book/1014636/2241863" target="_blank"> Clique aqui para visualizar as perguntas em uma nova aba e fazer o download .pdf</a>

    No que consiste a aplicação mepa?

    Há a necessidade de cadastrar distribuidoras? Quem as faz?

    **Sobre Gestão de Universidades e Usuários**

    Qual é a diferença prática de permissão entre um 'Administrador da Universidade' e um 'Técnico'? Existe alguma tela ou botão que o Admin vê e o Técnico não?

    Um usuário pode estar vinculado a múltiplas universidades simultaneamente ou o vínculo é exclusivo (1 para 1)?

    A remoção de um usuário é 'lógica' (apenas desativa o login, mantendo o histórico) ou 'física' (apaga os dados do banco)? Se apagarmos uma instituição ece com as faturas que ele cadastrou?

    Quais são os campos obrigatórios para cadastrar uma Universidade? O sistema deve validar o formato do CNPJ automaticamente e impedir duplicatas?

    **Sobre Unidades Consumidoras**    

    Qual dado garante que uma UC é única no sistema? É o 'Código da Unidade Consumidora' presente na conta de luz? O sistema deve bloquear se tentarem cadastrar o mesmo código duas vezes?

    Além do nome e endereço, precisamos cadastrar dados técnicos como 'Grupo Tarifário' (A ou B), 'Subgrupo', 'Tensão de Fornecimento' e 'Tipo de Medição'? Esses dados influenciam nos cálculos futuros?

    Se uma UC mudar de endereço ou de medidor, o sistema cria uma nova ou atualiza a existente mantendo o histórico de consumo?


    **Sobre Contratos e Renovação**

    Todo contrato tem obrigatoriamente uma 'Data de Início' e 'Data de Fim'? O sistema deve mudar o status do contrato para 'Expirado' automaticamente quando chegar a data final?

    Ao clicar em 'Renovar Contrato', o sistema deve criar um novo registro copiando os dados do contrato anterior (ex: Demanda Contratada) para agilizar o preenchimento? O sistema deve manter o histórico de todas as renovações passadas?

    Um contrato pertence a uma única UC ou pode ser um contrato 'guarda-chuva' que cobre várias unidades?

    **Sobre Faturas** 

    A entrada da fatura é manual campo a campo? Se sim, quais campos são críticos para os relatórios? (Ex: Consumo Ponta, Fora de Ponta, Demanda Medida, Demanda Faturada, Energia Reativa, Multas).

    O sistema deve alertar o usuário se ele digitar um consumo absurdamente alto ou negativo (validação de range)? O sistema deve impedir o cadastro de duas faturas para o mesmo mês de referência na mesma UC?

    Qual é a regra exata para o sistema marcar uma fatura como 'Pendente'? É quando passa do dia X do mês e a fatura ainda não foi cadastrada no sistema?

    **Sobre Distribuidoras e Tarifas**

    As tarifas de energia mudam anualmente. O sistema permite cadastrar a vigência da tarifa (De: Jan/2024 Até: Dez/2024)? Isso é essencial para que faturas antigas não tenham seus valores alterados quando a tarifa nova for cadastrada?

    O cadastro de tarifa deve suportar diferenciação por 'Posto Horário' (Ponta e Fora de Ponta) e 'Bandeiras Tarifárias' (Verde, Amarela, Vermelha)?


    **Sobre Inteligência e Dashboards**

    Como o sistema gera uma 'Recomendação'? Ele compara a 'Demanda Contratada' com a 'Demanda Medida' dos últimos 12 meses? Essa recomendação aparece automaticamente ou o usuário precisa solicitar a análise?

    No dashboard de pendências, o usuário deve conseguir filtrar por 'Tipo de Pendência' (ex: Fatura Atrasada vs. Tarifa não cadastrada)? Deve haver um link direto para resolver o problema (ex: clicar na pendência e ir para a tela de cadastro de fatura)?
    ```

<div style="text-align: center;">
  <p><strong>Entrevista 1:</strong> <a href="https://youtu.be/9Z0V1nYTEcc">Com os devs para a elaboração dos requisitos funcionais</a></p>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/9Z0V1nYTEcc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<a href="https://publuu.com/flip-book/1014636/2241858" target="_blank"> Clique aqui para visualizar a transcrição em uma nova aba e fazer o download .pdf</a>

<font size="3">
    <p style="text-align: center">
        <b>Autores:</b> 
        [Felipe das Neves](https://github.com/FelipeFreire-gf) e [Mylena Mendonça](https://github.com/MylenaTrindade)
    </p>
</font>

Após a entrevista modelamos a seguinte lista para os requisitos funcionais para o nosso estudo:

!!! Tip "Atenção!"
    Para visualizar os requisitos basta clicar na barra azul abaixo com o texto: "Lista de Requisitos Funcionais", nele também está disponível o link para visualizar em uma nova aba e fazer o download do pdf.


??? info "Lista de Requisitos Funcionais"

    <a href="https://publuu.com/flip-book/1014636/2241855" target="_blank"> Clique aqui para visualizar as perguntas em uma nova aba e fazer o download .pdf</a>

    ### RF. Módulo de Gestão de Universidades e Integração

    * **RF001 - Cadastro de Universidade via Formulário:** O sistema deve permitir o cadastro de novas universidades, processo que é iniciado através do recebimento de um formulário de interesse analisado pela equipe.
    * **RF002 - Validação de CNPJ:** No ato do cadastro da universidade, o sistema deve validar automaticamente os dígitos verificadores do CNPJ e impedir o cadastro se o número for inválido.
    * **RF003 - Bloqueio de Duplicidade de CNPJ:** O sistema deve verificar se o CNPJ já existe no banco de dados e impedir a criação de registros duplicados.
    * **RF004 - Integração com API da ANEEL:** O sistema deve conectar-se automaticamente à API da ANEEL para obter e atualizar a lista de distribuidoras de energia e suas respectivas tarifas em tempo real, eliminando o cadastro manual.
    * **RF005 - Lista de Solicitações:** O sistema deve possuir uma área administrativa onde a equipe do MEPA possa visualizar a lista de universidades que solicitaram acesso via formulário.

    ### RF. Módulo de Gestão de Usuários e Permissões

    * **RF006 - Níveis de Acesso:** O sistema deve suportar quatro tipos de perfis de usuário com permissões distintas:
        1.  **Gestor:** Pode gerenciar faturas, contratos e gerenciar outros usuários (adicionar/desativar).
        2.  **Operacional:** Pode apenas adicionar/gerenciar contratos e faturas, sem acesso à gestão de pessoas.
        3.  **Convidado:** Acesso apenas de leitura (visualização) para fins de validação/manutenção.
        4.  **Demonstração:** Acesso público a dados fictícios para conhecer o sistema, sem interagir com dados reais.
    * **RF007 - Vínculo Exclusivo:** O sistema deve garantir que um usuário esteja vinculado a apenas uma universidade por vez.
    * **RF008 - Exclusão Lógica de Usuário:** O sistema não deve permitir a exclusão física de usuários do banco de dados. A remoção deve ser lógica (apenas desativação do login), mantendo o histórico de ações e integridade dos dados.

    ### RF. Módulo de Unidades Consumidoras (UCs)

    * **RF009 - Unicidade da UC:** O sistema deve utilizar o "Código da Unidade Consumidora" (presente na conta de luz) como identificador único, bloqueando o cadastro se o código já existir.
    * **RF010 - Dados Técnicos Obrigatórios:** O cadastro da UC deve exigir dados essenciais que influenciam no cálculo, incluindo: Grupo Tarifário, Subgrupo, Tensão de Fornecimento e Distribuidora.
    * **RF011 - Imutabilidade de Local:** O sistema não deve permitir a alteração do endereço de uma UC (regra da ANEEL). Caso o local mude, a UC deve ser desativada e uma nova criada.
    * **RF012 - Edição de Dados Cadastrais:** O sistema deve permitir a edição de nome e outros dados não-críticos da UC, mantendo o histórico.
    * **RF013 - Desativação de UC:** O sistema deve permitir desativar uma UC, preservando todo o seu histórico de consumo.

    ### RF. Módulo de Contratos

    * **RF014 - Vigência do Contrato:** O sistema deve registrar obrigatoriamente a data de início e fim de cada contrato.
    * **RF015 - Status de Expiração:** O sistema deve alterar automaticamente o status do contrato para "Expirado" quando a data final for atingida e alertar o usuário.
    * **RF016 - Renovação de Contrato:** O sistema deve possuir uma função de "Renovar" que cria um novo contrato copiando os dados do contrato anterior (preservando o histórico do antigo) e vinculando-o à mesma UC.
    * **RF017 - Relacionamento Contrato-UC:** O sistema deve restringir cada contrato a uma única Unidade Consumidora (relação 1 para 1).

    ### RF. Módulo de Faturas (Entrada de Dados)

    * **RF018 - Métodos de Entrada:** O sistema deve permitir o lançamento de faturas de duas formas:
        1.  **Manual:** Preenchimento campo a campo.
        2.  **Automática (Importação):** Leitura de arquivos .CSV ou .XLSX.
        *Nota: Leitura de PDF não é suportada.*
    * **RF019 - Campos Críticos da Fatura:** O sistema deve capturar os seguintes dados para os cálculos:
        * Valor Total.
        * Valor Ponta e Fora Ponta.
        * Demanda Ponta e Fora Ponta (para tarifa Azul) ou Demanda Única (para tarifa Verde).
        * Energia Injetada (Geração Fotovoltaica).
    * **RF020 - Validação de Valores:** O sistema deve bloquear valores negativos, mas deve aceitar valores altos (variável conforme o tamanho da universidade).
    * **RF021 - Bloqueio de Duplicidade de Mês:** O sistema deve impedir o cadastro de mais de uma fatura para o mesmo mês de referência na mesma UC.
    * **RF022 - Identificação de Pendência:** O sistema deve marcar uma fatura como "Pendente" automaticamente a partir do dia 1º do mês subsequente.

    ### RF. Módulo de Inteligência e Recomendação

    * **RF023 - Janela de Análise:** O sistema deve utilizar uma janela móvel das últimas 12 faturas lançadas para realizar os cálculos de recomendação.
    * **RF024 - Aviso de Dados Insuficientes:** Caso existam faturas pendentes dentro da janela de 12 meses, o sistema deve exibir um aviso (*warning*) informando que a recomendação pode estar imprecisa, mas não deve impedir o cálculo.
    * **RF025 - Simulação de Cenários:** O sistema deve simular cenários comparando o contrato atual com as modalidades Verde e Azul (Ponta/Fora Ponta), considerando a demanda medida.
    * **RF026 - Geração Automática:** A recomendação deve ser recalculada automaticamente em *background* sempre que uma nova fatura for lançada ou editada.
    * **RF027 - Exibição da Recomendação:** O sistema deve exibir uma recomendação apenas se o cenário simulado for mais econômico que o contrato atual.

    ### RF. Módulo de Dashboards e Visualização

    * **RF028 - Painel Principal (Visão Geral):** O sistema deve exibir um painel com todas as Unidades Consumidoras que possuem pendências (faturas atrasadas ou problemas de contrato).
    * **RF029 - Ação Rápida no Painel Principal:** No painel principal, deve haver um botão/link direto para resolver o problema (ex: abrir o modal de lançamento da fatura pendente).
    * **RF030 - Painel Específico da UC:** Ao acessar uma UC específica, o sistema deve listar as pendências em fila (ex: "Lançar Novembro"), mostrando o mês seguinte apenas após a resolução do anterior.
    ```

### 1.2 Execução Etapa 2 

#### 1.2.1 Análise se o sistema possui tudo que foi listado nos requisitos funcionais

<div style="text-align: center;">
  <p><strong>Video 1:</strong> <a href="https://youtu.be/FOx23tpugBY">Análise dos Requisitos</a></p>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/FOx23tpugBY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<font size="3">
    <p style="text-align: center">
        <b>Autores:</b> 
        [Felipe das Neves](https://github.com/FelipeFreire-gf) e [Mylena Mendonça](https://github.com/MylenaTrindade)
    </p>
</font>

##### 1.2.2 Resultados da Análise se o sistema possui tudo que foi listado nos requisitos funcionais:

??? info "Resultados da Análise da Q1"
    ### **1. Gestão de Universidades e Integração**

    * RF001 — Cadastro de universidade *(implementado)*
    * RF002 — Validação de CNPJ *(testado e funcionando)*
    * RF004 — Integração com API da ANEEL *(funcionalidade presente e confirmada)*
    * RF003 — Bloqueio de duplicidade de CNPJ *(testado e funcionando)*
    * RF005 — Lista de solicitações *(não dava pra saber como eles recebiam a lista)*

    ### **2. Gestão de Usuários e Permissões**

    * RF006 — Níveis de acesso *(perfil “SYS Admin” validado no vídeo)*
    * RF007 — Vínculo exclusivo *(testado e funcionando)*
    * RF008 — Exclusão lógica *(testado e funcionando)*

    ### **3. Unidades Consumidoras**

    * RF009 — Unicidade da UC *(testado e funcionando)*
    * RF010 — Campos técnicos obrigatórios *(cadastro de UC exige dados, confirmado)*
    * RF011 — Imutabilidade de local *(testado e funcionando)*
    * RF012 — Edição de dados cadastrais *(testado e funcionando)*
    * RF013 — Desativação *(não testado)*

    ## 4. Contratos

    * RF014 — Vigência do Contrato *(testado e funcionando)*
    * RF015 — Status de Expiração *(testado e funcionando)*
    * RF016 — Renovação de Contrato *(testado e funcionando)*
    * RF017 — Relacionamento Contrato-UC *(testado e funcionando)*

    ## 5. Faturas

    * RF018 — Métodos de Entrada (Manual e Importação) *(Confirmado)*
    * RF019 — Campos Críticos da Fatura (Valores e Demandas) *(Confirmado)*
    * RF020 — Validação de Valores (Bloqueio Negativo) *(Confirmado)*
    * RF021 — Bloqueio de Duplicidade de Mês *(Confirmado)*
    * RF022 — Identificação de Pendência *(Confirmado)*

    ## 6. Inteligência e Recomendação

    * RF023 — Janela de Análise (Últimas 12 Faturas) *(Confirmado)*
    * RF024 — Aviso de Dados Insuficientes *(Confirmado)*
    * RF025 — Simulação de Cenários (Verde e Azul) *(Confirmado)*
    * RF026 — Geração Automática da Recomendação *(Confirmado)*
    * RF027 — Exibição da Recomendação (Apenas se Mais Econômico) *(Confirmado)*

    ### **7. Dashboards e Visualização**

    * RF028 — Painel geral *(foi observado e nas análises tudo está ok)*
    * RF029 — Ação rápida *(foi observado e nas análises tudo está ok)*
    * RF030 — Painel específico da UC *(foi observado e nas análises tudo está ok)*
    ```

---

#### 1.2.3 Análise se as funcionalidades do sistema estão corretas e se são relevantes para o usuário

<div style="text-align: center;">
  <p><strong>Video 2:</strong> <a href="https://youtu.be/0lue5zYwr6Q">Funcionalidades do Sistema</a></p>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/0lue5zYwr6Q" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<font size="3">
    <p style="text-align: center">
        <b>Autores:</b> 
        [Felipe das Neves](https://github.com/FelipeFreire-gf) e [Mylena Mendonça](https://github.com/MylenaTrindade)
    </p>
</font>

##### 1.2.4 Resultados da Análise se o sistema possui tudo que foi listado nos requisitos funcionais

??? info "Resultados da Análise Q2 e Q3"

    #### 1. **Análise de dados inexistentes**
    * Ao acessar a unidade *Ceilândia*, o sistema exibiu **corretamente que não há dados lançados para 2025**.
    * Na área de Análise, **nenhum gráfico foi gerado**, como esperado.
    **Cenário correto.**

    #### 2. **Inserção manual de dados e atualização dos gráficos**

    * Após inserir valores em Janeiro e Fevereiro de 2025:

      * Os gráficos foram exibidos imediatamente, com valores correspondentes.
      * Tanto o consumo em **ponta** quanto em **fora de ponta** foram atualizados.
    * O sistema demonstrou **correção nos cálculos e renderização imediata**.
    **Cenário correto.**

    #### 3. **Edição de dados da unidade consumidora**

    * Alteração do nome “Campo Ceilândia” → “Campo Ceilândia Sul”:

      * Alteração refletiu corretamente.
    * Alteração numérica de campos diversos:

      * Todos foram atualizados corretamente.
    **Cenário correto.**

    #### 4. **Criação de nova unidade consumidora**

    * Cadastro com dados válidos funcionou.
    * Cadastro com data futura exibiu corretamente o erro **“dados futuros não são permitidos”**.
    **Validação correta.**

    #### 5. **Gerenciamento de pessoas**

    * Inclusão de usuário gera um **bug**: o sistema apresenta erro, mas **o usuário é criado mesmo assim**.
    * Alterações de perfil, bloqueio e redefinição de senha funcionaram.
    * Logando com perfil “SYS Admin”, os usuários cadastrados anteriormente aparecem corretamente.
    **Um bug encontrado** (erro durante criação de usuário).

        <font size="3">
        <p style="text-align: center">
            <b>Figura 1:</b> Bug
            <br>
        </p>
    </font>

    <div align="center">
      <img src="https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2025-2_T02_CAROL-SHAW/refs/heads/main/docs/pages/Modulo4/dados/bug.png" alt="bug" width="600">
    </div>

    <font size="3">
        <p style="text-align: center">
            <b>Autores:</b> 
            Felipe das Neves e Mylena Mendonça
        </p>
    </font>

    #### 6. **Distribuidoras e API da Neoenergia**

    * A tela de distribuidoras exibe dados apenas para consulta, conforme informado:

      * Não permite cadastro manual (dados vêm da API).
    **Comportamento esperado.**

    #### 7. **Grupos tarifários e painel**

    * Telas exibem informações de taxa, horários e subgrupos conforme esperado.
    **Cenário correto.**

    #### 8. **Instituições**

    * Cadastro requer **CNPJ válido**, conforme requisitos.
    * Cadastro e edição funcionaram com dados válidos.
    **Cenário correto.**
    ```

---

### 1.3 Conclusão da Medição da Adequação Funcional

#### Q1 — *Functional Completeness (CR)*

#### Cálculo da Q1 — Functional Completeness (CR)

* Total de requisitos (RF001–RF030): **30**
* Requisitos confirmados como implementados/funcionando: todos exceto **RF005** e **RF013**.
  Requisitos confirmados = **28**

1. Divisão: (28 ÷ 30)

   * 28 ÷ 30 = 0,9333333333...

2. Multiplicar por 100:

   * (0,9333333333 ÷ 100 = 93,33333333...)

3. Arredondamento para uma casa decimal:

   * **CR = 93,3%**

**Classificação segundo os níveis definidos**

* Desejável: CR ≥ 90%
* Resultado obtido: **93,3% portanto: Desejável**

---

####  Q2 — *Correctness* das Funcionalidades Críticas (SC)

#### Cálculo da Q2 — *Correctness* (SC)

* Total de cenários executados: **14**
* Cenários concluídos corretamente: **13**

1. Divisão: (13 ÷ 14)

   * 13 ÷ 14 = 0,9285714286...

2. Multiplicar por 100:

   * 0,9285714286... × 100 = 92,85714286...

3. Arredondamento:

   * **SC = 92,8%**

**Classificação segundo os níveis definidos**

* Aceitável: 85% ≤ SC < 95%
* Resultado obtido: **92,8%, portanto: Aceitável**



---

####  Q3 — *Functional Conformity* (CF)

##### Evidências de Conformidade

A avaliação se deu pela comparação entre o comportamento observado e o comportamento especificado.

##### Funcionalidades avaliadas e conformidade:

| Funcionalidade                           | Conformidade Observada | Observações                                   |
| ---------------------------------------- | ---------------------- | --------------------------------------------- |
| Visualização de dados lançados           | ✔ Conforme             | Sem divergências                              |
| Geração de gráficos                      | ✔ Conforme             | Atualização imediata                          |
| Validação de dados futuros               | ✔ Conforme             | Mensagem correta                              |
| Edição de unidades consumidoras          | ✔ Conforme             | Tudo atualizado                               |
| Operar como SYS Admin                    | ✔ Conforme             | Usuários e instituições exibidos corretamente |
| Cadastro de instituições com CNPJ válido | ✔ Conforme             | Respeita regra                                |
| Exibição de grupos tarifários            | ✔ Conforme             | Coerente com requisitos                       |
| Tela de distribuidoras com dados da API  | ✔ Conforme             | Funcionalidade declaradamente somente leitura |
| Cadastro de usuários                     | ⚠ Parcial              | Bug: encontrado, mas usuário é criado     |

#### Cálculo da Q3 — *Functional Conformity* (CF)

* Total de funcionalidades avaliadas: **9**
* Funcionalidades em conformidade: **8**

1. Divisão: (8 ÷ 9)

   * 8 ÷ 9 = 0,8888888889...

2. Multiplicar por 100:

   * 0,8888888889... × 100 = 88,88888889...

3. Arredondamento para uma casa decimal:

   * **CF = 88,9%**

**Classificação segundo os níveis definidos**

* Aceitável: 75% ≤ CF < 90%
* Resultado obtido: **88,9%, portanto: Aceitável**


<font size="3">
    <p style="text-align: center">
        <b>Tabela 2:</b> Resultado Final
    </p>
</font>

<div align="center">
  <table>
    <thead>
      <tr>
        <th>Questão avaliada</th>
        <th>Resultado (%)</th>
        <th>Classificação</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Q1 — Em que medida as funcionalidades priorizadas do MEPA foram implementadas</td>
        <td>93,3%</td>
        <td>Desejável</td>
      </tr>
      <tr>
        <td>Q2 — Os resultados apresentados pelo sistema estão corretos</td>
        <td>92,8%</td>
        <td>Aceitável</td>
      </tr>
      <tr>
        <td>Q3 — As funcionalidades implementadas operam em conformidade com o esperado</td>
        <td>88,9%</td>
        <td>Aceitável</td>
      </tr>
    </tbody>
  </table>
</div>


---

## 2. Execução da Medição Para a Confiabilidade

A execução da medição de confiabilidade foi realizada no ambiente de teste previamente definido, seguindo rigorosamente os procedimentos detalhados na seção "Descrição da Medição Para a Confiabilidade" (Fase 3).

### Resultados da Tolerância a Falhas (Fault Tolerance)

**Objetivo:** Avaliar a capacidade do sistema de operar corretamente, mesmo na presença de falhas simuladas.

| Falha Simulada | Resultado da Operação |  | Sobrevivência (Sim/Não) |
| :--- | :--- | :--- | :--- |
| Interrupção da Conexão com o Banco de Dados | O sistema exibiu uma tela de erro genérica e travou a operação. | "Erro de conexão com o servidor." | Não |
| Sobrecarga de Requisições (500 req/s) |  | Nenhuma | Sim |
| Reinicialização Abrupta do Servidor Web |  | Nenhuma | Não |

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


## 3. Execução da Medição Para a Manutenibilidade

A execução da medição para a Manutenibilidade concentrou-se na análise estática do código-fonte e na coleta de dados de processo do sistema de gestão de projetos (GitLab Issues), conforme detalhado na Fase 3.

### Complexidade Ciclomática (CCM)

A Complexidade Ciclomática (CC) é uma métrica que indica a complexidade estrutural do código, sendo um fator chave para a Analisabilidade e Modificabilidade.

**Execução da Medição:**
A análise estática foi realizada utilizando a ferramenta **SonarCloud**. O valor total da Complexidade Ciclomática para o projeto foi de **1.295**.

**Análise Modular e Julgamento:**

Para obter a **Complexidade Ciclomática Média (CCM)**, foi realizada uma análise granular por módulo, excluindo os módulos `tests` e `mec_energia` (módulo administrativo do framework Django) por não representarem o código de negócio principal.

<div style="text-align: center;">
  <p><strong>Video 1:</strong> <a href="https://youtu.be/NerYpyylvd0">Coleta CCM</a></p>
  <iframe width="560" height="315" src="https://youtu.be/NerYpyylvd0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


| Módulo | CC (Total) | CCM (Média por Módulo) |
| :--- | :--- | :--- |
| `contracts` | 132 | 10,15 |
| `users` | 195 | 15,00 |
| `global_search_recommendation` | 71 | 11,83 |
| `recommendation` | 99 | 9,00 |
| `recommendation_commons` | 49 | 5,44 |
| `scripts` | 47 | 5,22 |
| `tariffs` | 155 | 14,09 |
| `universities` | 101 | 8,41 |
| `utils` | 102 | 7,84 |

O **CCM geral** a partir dos módulos coletados foi de **9,00**.

**Conclusão da CCM:**
O resultado de **CCM = 9,00** se enquadra na faixa **Desejável (CCM ≤ 10)**, conforme o critério de julgamento estabelecido no Módulo 2. Isso sugere que, em média, o código do projeto MEPA apresenta uma baixa complexidade estrutural, favorecendo a **Analisabilidade** e a **Modificabilidade**.

No entanto, a análise modular revela pontos de atenção: os módulos **`users` (CCM = 15,00)** e **`tariffs` (CCM = 14,09)** estão no limite superior da faixa **Aceitável** (10 < CCM ≤ 15), indicando que estes componentes específicos podem exigir maior esforço para manutenção e testes.

### Lead Time de Correção (LTC)

O Lead Time de Correção (LTC) mede a agilidade do processo de manutenção, sendo um indicador direto da Modificabilidade do sistema.

**Execução da Medição:**
A coleta de dados foi realizada através de uma consulta estruturada no sistema de *Issues* do **GitLab**, utilizando um script em Python [4]. O LTC foi calculado como o tempo decorrido entre a **abertura do *Issue*** e o **fechamento (correção do bug)**, o que reflete o tempo total de resolução de defeitos.

<div style="text-align: center;">
  <p><strong>Video 1:</strong> <a href="https://youtu.be/fyOFL0s-LoU">Coleta LTC</a></p>
  <iframe width="560" height="315" src="https://youtu.be/fyOFL0s-LoU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

**Amostra de Dados Coletados:**
A tabela abaixo apresenta uma amostra dos dados utilizados no cálculo do LTC:

<font size="3">
    <p style="text-align: center">
        <b>Tabela 2:</b> Amostra de Lead Time de Correção (LTC)
    </p>
</font>

| ID | Issue | Created | Closed | LTC_dias |
| :---: | :--- | :---: | :---: | :---: |
| 490 | Fix campo "Nome da Unidade Consumidora" | 2025-05-17 | 2025-06-01 | 15 |
| 480 | Tratamento de erro para plot de gráficos | 2025-05-12 | 2025-05-14 | 1 |
| 479 | Refatorar a mensagem para faturas | 2025-05-12 | 2025-05-14 | 1 |
| 477 | Relatório detalhado faltando dados | 2025-05-09 | 2025-05-14 | 5 |
| 475 | Tarifa vencida mesmo dentro da validade | 2025-05-08 | 2025-05-14 | 5 |

| Fonte: Resultados em CSV da Extração Pipeline LTC [5]

**Resultado da Medição:**
O **LTC médio** encontrado na amostra analisada foi de **64 dias**.

**Análise e Julgamento:**
O critério de julgamento estabelecido no Módulo 2 para o LTC é:
*   **Desejável:** LTC ≤ 3 dias
*   **Aceitável:** 4 ≤ LTC ≤ 7 dias
*   **Inaceitável:** LTC > 7 dias

Com um LTC médio de **64 dias**, o resultado se enquadra na faixa **Inaceitável**. Este valor é significativamente superior ao limite de 7 dias, indicando um processo de manutenção lento.

**Implicações:**
O alto LTC sugere que a **Modificabilidade** do sistema está comprometida. As causas podem estar relacionadas a:
1.  **Complexidade do Código:** O alto LTC pode ser uma consequência da alta Complexidade Ciclomática em módulos críticos (como visto na CCM).
2.  **Processo de Desenvolvimento:** Gargalos no processo de *review*, testes ou *deploy* que atrasam a entrega da correção.

Este resultado é um ponto crítico que deve ser destacado na conclusão da avaliação de Manutenibilidade.

## Cobertura de testes de Regressão (CTR)
Para calcular o CTR, como descrito na etapa 3, fizemos manualmente o cálculo dos últimos 3 Merge Requests aceitos, seguindo a fórmula descrita na etapa 2. a tabela a baixa mostra os resultados.
|MR|Linhas cobertas por Testes|Linhas Alteradas|CTR|
|:------:|------------------|------------|:----------------:|
|!435|50|60|83%|
|!433|236|264|89%|
|!432|569|572|99%|
|!431|437|493|88%|
|!430|574|583|98%|

Assim, como todos os CTRs foram maiores ou iguais à 80% concluimos, conforme estabelecido na etapa 2, que o CTR é **desejável**.

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
> [4] Script Implementação da Pipeline LTC. Disponível em: [Script - Extrator de LTC - Issues GitLab](./dados/extratorIssuesLTC.py)
>
> [5] Resultados em CSV da Extração Pipeline LTC. Disponível em: [Dados de Saída - Extrator de LTC - Issues GitLab](./dados/issues_ltc.csv)

---

## Histórico de Versões

| Versão | Descrição | Autor(es) | Data de Produção | Revisor(es) | Data de Revisão | Observações / Incrementos |
|:------:|------------------|------------|:----------------:|--------------|:----------------:|---------------------------|
| `1.0` | Desenvolvimento dos objetivos do GQM. | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 17/11/2025 | — | — | Versão inicial do documento. |
| `1.1` | Inserção do que executamos para o artefato da adequação funcional. | [Felipe das Neves](https://github.com/FelipeFreire-gf) | 17/11/2025 | [Mylena Mendonça](https://github.com/MylenaTrindade) | 17/11/2025 | Revisão da ideação do artefato. |
| `1.2` | Inserção do que executamos para o artefato da confiabilidade. | [Gustavo Gontijo Lima](https://github.com/Guga301104) | 18/11/2025 | [Ana Luiza Komatsu](https://github.com/luluaroeira) | 18/11/2025 | Revisão da ideação do artefato. |
| `1.3` | Inserção do CTR. | [Marcos Bittar](https://github.com/Bittarx) | | 23/11/2025 |  |
| `1.4` | Inserção do que executamos para o artefato da Manuntenabilidade | [Pedro Barbosa](https://github.com/pedrobarbosaocb) | | 23/11/2025 |  |
| `1.5` | Inserção dos videos para o artefato da Manuntenabilidade | [Pedro Barbosa](https://github.com/pedrobarbosaocb) | | 28/11/2025 |  |
