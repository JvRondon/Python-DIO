valores = input().split()

horas = int(valores[0])
velocidade = int(valores[1])

carro = int(12) #km/h

litro = (horas*velocidade)
total = litro/carro

print("%.3f" % total)