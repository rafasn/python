#  Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos
def soma_tres(a,b,c):
    soma = a+b+c
    print(f'Soma de {a},{b},{c} é igual a: {soma}')

a=int(input("Digite o primeiro número:"))
b=int(input("Digite o segundo número:"))
c=int(input("Digite o terceiro número:"))

soma_tres(a,b,c)