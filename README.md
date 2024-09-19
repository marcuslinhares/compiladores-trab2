# Trabalho de Compiladores

Este repositório contém a implementação de um compilador para uma linguagem customizada, desenvolvido como parte do trabalho da disciplina de Compiladores. O compilador realiza todas as etapas do processo de tradução de uma linguagem, incluindo análise léxica, análise sintática, verificação semântica, e geração de código final em assembly.

## Estrutura do Projeto

O projeto é composto por diversos arquivos Python que implementam as várias fases e componentes do compilador. Cada arquivo desempenha um papel específico na pipeline de compilação, conforme descrito abaixo.

### Análise dos Arquivos

#### 1. **ASM.py**

Este arquivo trata da geração de código assembly. Ele converte a estrutura intermediária gerada pelo compilador em instruções de baixo nível que podem ser executadas diretamente em uma máquina. Isso inclui operações de manipulação de registradores, aritmética e controle de fluxo.

#### 2. **CodeGEN.py**

Responsável pela geração do código final a partir da árvore de sintaxe abstrata (AST). Ele percorre a AST e gera código intermediário ou de máquina. Esse arquivo é crítico para a transição entre a análise semântica e a geração de código executável, aplicando otimizações e garantindo que as operações sejam válidas.

#### 3. **Consts.py**

Este arquivo contém constantes usadas em várias partes do compilador, como palavras-chave, operadores e tipos de tokens. Essas constantes centralizam o gerenciamento de símbolos, facilitando a manutenção e a expansão do compilador.

#### 4. **Error.py**

Lida com o tratamento de erros em todas as fases da compilação, desde a análise léxica até a execução. Define como os erros são capturados, formatados e exibidos para o usuário, categorizando-os como erros de sintaxe, semântica ou de execução.

#### 5. **Grammar.py**

Define as regras gramaticais da linguagem e como o parser deve construir a árvore de sintaxe abstrata (AST). Este arquivo contém as produções da gramática e descreve como os tokens gerados pelo lexer devem ser combinados para formar expressões e declarações válidas na linguagem.

#### 6. **Lexer.py**

O lexer converte o código-fonte em uma sequência de tokens. Cada token representa uma unidade básica do código, como identificadores, operadores ou números. O lexer é a primeira fase do compilador e é essencial para preparar o código para as etapas seguintes.

#### 7. **main.py**

O ponto de entrada do compilador. Ele coordena todas as fases, desde a análise léxica até a geração de código final. O `main.py` gerencia o fluxo de execução do compilador e captura os erros que possam surgir durante o processo.

#### 8. **Memory.py**

Gerencia a alocação e o acesso à memória durante a execução do código compilado. Ele mantém o controle sobre variáveis e valores, garantindo que o compilador possa acessar e modificar corretamente os dados durante a execução do programa.

#### 9. **Parser.py**

Responsável por construir a árvore de sintaxe abstrata (AST) a partir da sequência de tokens gerada pelo lexer. O parser aplica as regras gramaticais definidas em `Grammar.py` e organiza o código-fonte em uma estrutura hierárquica que representa a lógica do programa.

#### 10. **Repl.py**

Implementa um REPL (Read-Eval-Print Loop), permitindo a interação em tempo real com o compilador. O REPL é útil para testar pequenos pedaços de código diretamente no terminal, fornecendo uma experiência interativa para o usuário.

#### 11. **SemanticVisitor.py**

Este arquivo define os visitantes da AST responsáveis pela verificação semântica. Ele percorre a árvore e verifica se as operações e os tipos são válidos, garantindo a consistência e a segurança do código. Ele também trata a execução das operações sobre os nós da árvore.

#### 12. **Token.py**

Define a estrutura de um token, que é a menor unidade sintática reconhecida pelo lexer. Cada token contém informações sobre o tipo e o valor, como identificadores, números, ou operadores. Tokens são os blocos de construção usados pelo parser para criar a AST.

#### 13. **TValue.py**

Este arquivo contém classes que representam os diferentes tipos de valores da linguagem, como números, strings, listas e tuplas. Essas classes são usadas durante a execução para manipular os dados corretamente, de acordo com as operações e tipos definidos na linguagem.

#### 14. **Util.py**

Contém funções auxiliares para leitura e gravação de arquivos, além de outras operações utilitárias que são utilizadas em várias partes do compilador. Essas funções facilitam a interação com arquivos de entrada e saída, como o código-fonte a ser compilado ou o código assembly gerado.

----------

## Integração dos Arquivos

Cada um desses arquivos desempenha um papel essencial no ciclo de vida do compilador, eles formam a espinha dorsal do compilador, desde a análise e validação do código-fonte até sua execução ou conversão para uma linguagem de baixo nível. A interação entre eles acontece da seguinte forma: 

1.  **Análise Léxica (Lexer.py e Token.py)**: O código-fonte é lido e transformado em uma sequência de tokens pelo lexer. Esses tokens representam as unidades básicas do código.
    
2.  **Análise Sintática (Grammar.py e Parser.py)**: Os tokens são organizados em uma árvore de sintaxe abstrata (AST) de acordo com as regras gramaticais definidas em `Grammar.py`. O parser aplica essas regras para validar a estrutura do código.
    
3.  **Análise Semântica (SemanticVisitor.py)**: A AST é então percorrida por visitantes que verificam a validade semântica do código, como a coerência de tipos e operações. Se houver erros semânticos, eles são reportados para o usuário.
    
4.  **Geração de Código (CodeGEN.py e ASM.py)**: Após a verificação semântica, o código intermediário é gerado a partir da AST. Esse código é traduzido para assembly por `ASM.py`, que pode ser executado diretamente em uma máquina.
    
5.  **Execução (TValue.py e Memory.py)**: Durante a execução, as variáveis e valores do programa são gerenciados por `Memory.py`, e os diferentes tipos de dados são manipulados pelas classes definidas em `TValue.py`.
    
6.  **Interatividade (Repl.py)**: O arquivo `Repl.py` permite que o compilador seja executado de forma interativa, aceitando e executando código diretamente no terminal.
    
7.  **Funções Utilitárias (Util.py)**: Várias partes do compilador utilizam funções auxiliares de `Util.py` para operações de leitura e gravação de arquivos, facilitando o fluxo de trabalho.
