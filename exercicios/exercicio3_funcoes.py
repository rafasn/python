#Escreva um script que pergunta ao usuário se ele deseja converteruma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função.Plus: Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta

def conversao_cf():
    calculo_conversao_f = temp*1.8+32
    print(f'A temperatura {temp}°C é igual a: {calculo_conversao_f}°F')

def conversao_fc():
    calculo_conversao_c = (temp-32)/1.8
    print(f'A temperatura {temp}°F é igual a: {calculo_conversao_c}°C')
    
temp = int(input("Digite a temperatura: "))
menu=int(input("Digite 1 para converter para Celsius ou 2 para converter para Fahrenheit: "))
if menu == 1:
    conversao_fc()
elif menu == 2:
    conversao_cf()
else:
    print("Digite 1 ou 2.")



    