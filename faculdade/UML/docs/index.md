<h2><a href= "https://www.mackenzie.br">Universidade Presbiteriana Mackenzie</a></h2>
<h3><a href= "https://www.mackenzie.br/graduacao/sao-paulo-higienopolis/sistemas-de-informacao">Ciencia da Computação</a></h3>


<font size="+12"><center>
## Be Present
</center></font>


**Conteúdo**

- [Autores](#autores)
- [Descrição do projeto](#Descrição-do-projeto)
- [Análise de requisitos funcionais e não-fucionais](#Análise-de-requisitos-funcionais-e-não-funcionais)
- [Diagrama de casos e uso](#Diagrama-de-casos-de-uso)
- [Descrição dos casos e uso](#Descrição-dos-casos-de-uso)
- [Diagrama de sequencia](#Diagrama-de-sequencia)
- [Diagrama de classes](#Diagrama-de-classes)
- [Diagrama de componentes](#Diagrama-de-Componentes)
- [Decisões de arquitetura](#Decisões-de-arquitetura)
- [Diagrama de implantação](#Diagrama-de-implantação)
- [Referências](#Referências)


# Autores

* Matteo Domiciano Varnier
* Felipe Mazzeo Barbosa 
* Daniel Reis Raske



# Descrição do projeto

*A Escola Infinito necessita de um sistema para controlar as presenças de seus
alunos, pois a operação ainda é realizada totalmente em papel.*

# Análise de requisitos funcionais e não-funcionais
### Requisitos Funcionais:

1. Permitir que professores registrem faltas de forma fácil e intuitiva.

2. O sistema deve ser capaz de gerar relatórios de faltas, permitindo o agrupamento por data, ano do ensino, turma, professor, disciplina e aluno. 

3. Facilitar a análise e o acompanhamento do número de faltas.

4. Enviar notificações por e-mail aos pais ou responsáveis quando a porcentagem de comparecimento às aulas estiver abaixo de 80%.

### Requisitos nao-funcionais:

1. O sistema deve ser implementado em lingugem HTML, CSS e JS
2. O sistema devera ser interligado com um banco de dados
3. O sistema devera ser funcional tanto na WEB quando mobile
4. O usuario devera ser capaz de suportar varios acessos simultaneos
5. O usuario devera escolher uma senha forte com no minimo 6 digitos, 1 caractere especial e 1 letra maiuscula. 

# Diagrama de casos e uso

![alt](/src/Caso_e_uso.png)

# Descrição dos casos e uso

### Registrar Falta:

**Ator: Professor**

**Descrição: O professor registra a falta de um determinado aluno em uma aula/dia em dois momentos diferentes.**

**Fluxo básico:**

- O professor acessa a funcionalidade "Registrar Falta".
- O sistema apresenta a lista de turmas e alunos.
- O professor seleciona a turma e o aluno que faltou.
- O professor registra a falta do aluno na data atual.
- O sistema salva a informação de falta registrada.

### Relatório de Faltas:

**Ator: Professor**

**Descrição: Gera um relatório com informações consolidadas sobre as faltas.**

**Fluxo básico:**
- O usuário acessa a funcionalidade "Gerar Relatório de Faltas".
- O sistema apresenta acessibilidade de busca (aluno, turma, data, disciplina, professor).
- O usuário seleciona os filtros desejados.
- O sistema gera o relatório de acordo com os filtros.
- O usuário visualiza o relatório de faltas gerado.
- O ususario visuzaliza a porcentagem de falta

### Notificação:

**Ator:Pais/Responsaveis**

**Descrição: Envia uma notificação por e-mail aos pais/responsáveis sobre a situação de faltas do aluno.**

 **Fluxo básico:**
- O sistema verifica diariamente o percentual de faltas de cada aluno.
- Para alunos com percentual abaixo do limite definido, o sistema automaticamente aciona o caso de uso "Enviar Notificação".
- O sistema busca os dados de e-mail dos pais/responsáveis.
- O sistema envia a notificação por e-mail

### Acessibilidae:

**Ator: Sistema**

**Descrição: Permite configurar as opções de acessibilidade e outras configurações do sistema.**

**Fluxo básico:**
- O administrador acessa a tela de configurações do sistema.
- O administrador altera as configurações de fonte, contraste, notificações, entre outras na WEB ou no mobile
- O sistema salva as configurações aplicadas.
- O sistema permite modificar o registro de faltas

### Qualquer Site/WEB:

**Ator: Professor, Adm Sistema, Pais/Responsaveis**

**Descrição: Permite configurar as opções de acessibilidade e outras configurações do sistema.**

**Fluxo básico:**
- O administrador acessa a tela de configurações do sistema.
- O administrador coloca todas as faltas no sistema.
- No sistema é possivel visualizar as notificacoes por aplicativo ou pelo site
- Professores e pais podem acessar o site pelo ID do aluno ou ID do professor
- Pais e professores veem a quantidade de falta
- Pais podem justificar a falta dos filhos com atestado



# Diagrama de sequencia

- Diagrama de sequencia da (sistema de chamada)

![alt](/src/chamada.png)

-Diagrama de Sequencia (gera Relatorio)

![alt](/src/Gera_Relatorio.png)

-Diagrama de Sequencia (email automatico relatorio)

![alt](/src/Email_auto.png)


# Diagrama de classes

![alt](/src/Diagrama_classe.png)

# Diagrama de Componentes

![alt](/src/Componentes.png)

# Decisões de arquitetura

- Aplicação web desenvolvida

- Banco de dados para armazenar os dados do sistema

- Hospedagem na nuvem para disponibilizar o acesso 
via navegador web

- APIs para possibilitar a integração com outros sistemas (por exemplo, para enviar e-mails ou notificações push)

- Front-end responsivo para garantir a acessibilidade e adaptação a dispositivos móveis

- Autenticação e autorização com tokens para controlar o acesso

- Fila para processamentos (envio de e-mails em segundo plano)

**Os professores acessariam o sistema via navegador para registrar presença e faltas. A aplicação web disponibilizaria dados e relatórios em tempo real sobre a situação de cada aluno. Notificações automáticas seriam disparadas conforme as regras de faltas configuradas.**

# Diagrama de implantação
![alt](/src/Implantacao.png)

# Referências

- https://uderson.medium.com/o-que-%C3%A9-um-registro-de-decis%C3%A3o-de-arquitetura-8e9055b740c7

- https://www.drawio.com/blog/uml-component-diagrams

- https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-component-diagram/