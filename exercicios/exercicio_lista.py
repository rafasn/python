#Exercicio 1 - classificação crime

lista_perguntas =[]
pergunta1=input("Telefonou para a vítimia?")
pergunta2 = input("Esteve no local do crime?")
pergunta3 = input("Mora perto da vítima?")
pergunta4 = input("Devia para vítima?")
pergunta5 = input("Já trabalho com a vítima?")
contador = 0
c=1

lista_perguntas.append(pergunta1)
lista_perguntas.append(pergunta2)
lista_perguntas.append(pergunta3)
lista_perguntas.append(pergunta4)
lista_perguntas.append(pergunta5)

print(lista_perguntas)

for c in range(0,5,1):
    if lista_perguntas[c]=="sim":
        contador = 1 + contador
    else:
        contador = 0 + contador
if contador==2:
    print("suspeito.")
elif contador==5:
    print("assassino!!!!")
elif contador == 1:   
    print("inocente.")
else:
      print("cumplice.")

