class Cachorro:
    def __init__(self,nome,cor,acordado=True):
        print("Inicializando a classe....")
        self.nome= nome
        self.cor=cor
        self.acordado =acordado

    def __del__(self):
        print("Removendo classe..")

    def latir(self):
        print("AU AU")

    
    def criar_cachorro():
        c= Cachorro("Zeus", "Branco", False)
        print(c.nome)
    
    criar_cachorro()

# c = Cachorro("Gohan","Preto")

# c.latir()