from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a tv")

    def desligar(self):
        print("Desligando a tv")


controle = ControleTV()
controle.ligar()
controle.desligar()