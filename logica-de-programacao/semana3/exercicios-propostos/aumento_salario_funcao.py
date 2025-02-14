salario = float(input())

def reajuste_salario(salario):
    novo_salario = 0

    if (0 <= salario <= 400):
        aumento = salario * 0.15
    elif (400.01 <= salario <= 800):
        aumento = salario * 0.12
    elif (800.01 <= salario <= 1200):
        aumento = salario * 0.10
    elif (1200.01 <= salario <= 2000):
        aumento = salario * 0.07
    else:
        aumento = salario * 0.04

    novo_salario = salario + aumento
    return novo_salario

novo_salario = reajuste_salario(salario)
reajuste = novo_salario - salario
porcentagem = (reajuste / salario) * 100


print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {porcentagem:.0f} %')