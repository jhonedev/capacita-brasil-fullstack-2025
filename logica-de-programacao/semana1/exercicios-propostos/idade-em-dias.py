valor = int(input())
ano = valor // 365
meses = (valor % 365) // 30 
dias = (valor % 365) % 30

print(f"{ano} ano (s)")
print(f"{meses} mes (es)")
print(f"{dias} dia (s)")