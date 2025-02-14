X = int(input())
Y = float(input())

def calculo_de_consumo(distancia, combustivel):
    media = distancia / combustivel
    return media

media = calculo_de_consumo(X, Y)
print(f"{media:.3f} km/l")