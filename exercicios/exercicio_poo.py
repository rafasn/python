# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
# Crie uma instância da classe carro.
# Faça o carro "andar" utilizando os métodos da sua classe.
# Faça o carro "parar" utilizando os métodos da sua classe.
class Carro:
    def __init__(self):
        self.ligado=False
        self.vel=0
        self.vel_min =0
        self.vel_max=200

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        if self.vel == 0:
            self.ligado = False
    
    def acelerar(self):
        if not self.ligado:
            return

        if self.vel < self.vel_max:
            self.vel += 10

    def desacelerar(self):
        if not self.ligado:
            return

        if self.vel > self.vel_min:
            self.vel -= 10
        
    def __str__(self) -> str:
        return f'Carro - ligado {self.ligado} - velocidade {self.vel}'

meu_carro = Carro()

meu_carro.ligar()
for _ in range(3):
    meu_carro.acelerar()
print(meu_carro)

for _ in range(2):
    meu_carro.desacelerar()
meu_carro.desligar()
print(meu_carro)


