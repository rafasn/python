def soma(a,b):
    calculo = a+b
    file = 'arquivo.txt'

    arquivo_escrita =  open(file, "w") 
    arquivo_escrita.write(f'O resultado da soma é:{calculo}')
    arquivo_escrita.close()

### leitura do arquivo
    arquivo_leitura =  open(file, "r") 
    leitura = arquivo_leitura.read()
    print(leitura)
    arquivo_leitura.close()
    
def subtracao(a,b):
    sub= a-b
    print(f'O resultado da subtração é:{sub}') 

a=int(input("Insira um número"))
b=int(input("Insira outro número"))

soma(a,b)
subtracao(a,b)