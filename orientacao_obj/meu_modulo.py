import colorama

colorama.init()

nome_do_usuario = input("Insira seu nome:")

def mensagem_usuario ():
        print(f"Bem vinda, " + colorama.Fore.LIGHTBLUE_EX + nome_do_usuario)