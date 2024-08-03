#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira

real= float(input("Insira quanto dinheiro você tem na carteira"))

dolar_amer= round(real*4.91,3)
peso_arg = round(real*0.02,3)
dolar_aus=round(real*3.18,3)
dolar_canad=round(real*3.64,3)
franco_sui=round(real*0.42,2)
euro= round(real* 5.36,3)
libra= round(real* 6.21,3)

print(f" Real: {real} \n Dolar Americano: {dolar_amer} \n Dolar Australiano: {dolar_aus}\n Dolar Canadense: {dolar_amer} \n Peso Argentino: {peso_arg} \n Franco Suiço: {franco_sui} \n Euro {euro} \n Libra {libra} ")