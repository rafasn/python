# MÓDULOS E NAMESPACE

## Módulo
    - Local onde define os nomes e funções para ficar visível para todo o sistema > podendo usar em diferentes arquivos
    - Espaço para declaração de nomes (namespace)

*variáveis* definidas dentro de um namespace > são chamadas de *atributos*

### Criando um módulo
1. criar arquivo
2. nomear .py
3. definir funções, atributos, variáveis, classe que desejar

### Importando um módulo para outro arquivo

uma de cada vez:

    - import nome_do_modulo.py
    - inserir o namespace antes da variável/atributo

tudo:

    -  from nome_do_modulo import *
    - não precisa especificar o namespace
    - não é considerada uma boa prática > muito informação que não é necessária e pode gerar conflitos
    - conflito: função ou variável com mesmo nomedo do namespace > pode confundir o programa 

específico:

    - from nome_do_modulo import componente
    - especificar os nomes que quer importar 

## Pacotes
    - Coleção de módulos que foi disponibilizada publicamente
    - Arquivos externos ao sistema que estamos desenvolvendo.

*Diversidade de pacotes:* 
- analisar dados (pandas, numpy, matplotlib)
- colorir o que é impresso no terminal (colorama)
- lidar com geração de boletos, converter moedas, etc.

O *Python Package index* contém a lista de todos os pacotes públicos que podem ser instalados utilizando o comando pip no terminal.

### Importando um pacote

    Mesma forma que importar módulos criados diretamente no sistema, exceto que precisamos *baixar o pacote primeiro para o ambiente.*

### Instalando um pacote
    Comando pip
    * Importante: O comando pip deve ser usado no terminal, não em um script python

#### Para instalar um pacote individualmente
- pip install [nome_do_pacote]

#### Arquivo com uma lista de todos os pacotes que são utilizados no projeto 
- o nome deste arquivo chamado costuma ser *requirements.txt*

- é preciso rodar no terminal o comando pip install -r requirements.txt > instalar as dependências listadas no arquivo requirements.txt

## Escopo
    Determinação se a variável é ###local ou global*

### Variável local
- Declaradas dentro de uma função e não podem ser acessadas fora dela.

### Variável global
- Declaradas fora de qualquer função

- Para alterar variáveis globais dentro de funções, precisamos indicar a função que estamos querendo alterar a variável do escopo global. Caso contrário, outra variável de mesmo nome é criada dentro do escopo da função e é alterada apenas localmente.

# CLASSES E OBJETOS

- Dados e funções são entidades diferentes, e que precisam ser combinadas para produzir o resultado esperado.

- Podemos pensar na programação orientada a objetos como uma forma de modelar os nossos programas como *objetos*

## Objetos

    Possuem dois componentes principais que não ficam separados, eles ficam associados ao objeto
        Propriedades: cor, forma, pesa, tamanho, etc.
        Comportamentos: são coisas que dá pra fazer com aquele objeto.
        
   São auto-contidos e reutilizáveis:

## Classes
    
    Define um novo tipo de dados (criado pela programadora).
    Descrevem o que um objeto vai ser > não criam o objeto em si
    
    São criadas com a palavra-chave *class*

    Conveção para nomes de classes em Python: *PascalCasing*

    Uma classe pode ter várias *instâncias*, e cada uma delas é isolada da outra e tem seus próprios atributos e métodos.

#### Método especial __init__
    - Chamado quando um novo objeto daquela classe é criado
    - Construtor porque ele inicializa os valores padrão do objeto

#### Método x função 
    - Método é uma função definidas dentro da classe 

#### self
    - primeiro parâmetro dos métodos de uma classe é chamado de self
    - representa a instância sobre a qual o método vai atuar
    - acesso a atributos e outros métodos daquela mesma instância
    - Declarar self como o primeiro parâmetro de seus métodos.
