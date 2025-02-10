numero = int(input())

minutos = numero // 60
segundos = numero % 60
horas = minutos // 60
minutos = minutos % 60

print(f"{horas}:{minutos}:{segundos}")