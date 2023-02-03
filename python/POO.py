class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("bi bi BIIIII")

    def parar (self):
        print("parando")
        print("parou")

    def correr(self):
        print("stutututu")

    # def __str__(self):
    #     return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b2 = Bicicleta("amarela", "Raptor", 2000, 1200) 
        
print(b2)

# b1.buzinar()
# b1.parar()
# b1.correr()

# print(b1.cor, b1.modelo, b1.ano, b1.valor)