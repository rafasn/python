# Crie uma função chamada contar_vogais que recebe uma string como parâmetro. Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.

def contar_vogais():
    string= input("Insira uma frase: ")
    contador = 0
    tam_string=len(string)

    for c in range(0,(tam_string)):
       if (string[c]=="a") or (string[c]=="e") or (string[c]=="i") or (string[c]=="o") or (string[c]=="u"):
         contador= contador + 1
    print(contador)

contar_vogais()

