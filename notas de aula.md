# Funções
 
    grupo de instruções relacionadas que executa uma tarefa

## 1. declaração
    def função():

## 2. chamada da função
    função()


 operação e função não podem ter o mesmo nome

## parâmetros
    funcao(x,y)
    x,y > parâmetros
## manipulação de arquivos
- criar arquivo
    - file = 'arquivo.txt'
    - criar pasta manual no vscode > mesma pasta

 ### abertura de arquivos
    arquivo_leitura =  open(file, "r") > apenas para leitura 

    arquivo_escrita =  open(file, "w") > para escrita

    arquivo_leitura =  open(file, "wb") > arquivos binários

### escrita no arquivo
    arquivo_escrita =  open(file, "w") 
    arquivo_escrita.write('texto a ser escrito')
    arquivo_escrita.close()

### leitura do arquivo
    arquivo_leitura =  open(file, "r") 
    leitura = arquivo_leitura.read()
    print(leitura)
    arquivo_leitura.close()

# Tratamento de exceções
pensar onde poderia dar erro
    
    try:
        calculo
    excpet TypeError as e
        print("Mensagem do erro. \n Detalhe:", e) 
