class Veiculo:
    def __init__(self, cor, num_roda, placa):
        self.cor = cor
        self.num_roda = num_roda
        self.placa = placa 

    def ligar_motor(self):
        print("Ligando...")

class Motocicleta(Veiculo):


    pass

class Carro(Veiculo):


    pass

class Caminhao(Veiculo):
    def __init__(self,cor, num_roda, placa, carregado):
        super().__init__(cor,num_roda,placa)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("Verde", 2,"JVR-0001")
moto.ligar_motor()

carro = Carro("Laranja", 4, "RDN-1234")
carro.ligar_motor()

caminhao = Caminhao("Preto", 8, "CHT-0000",False)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)