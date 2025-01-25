"""
Faça um programa que leia dois valores e apresente o maior entre os valores 
lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
MaiorAB = (a+b+abs(a-b)) / 2

Obs¹.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
Obs².: a função abs retorna o valor absoluto de um número, ou seja, o número sem o seu sinal

Entrada
O arquivo de entrada contém dois valores inteiros.
Saída
Imprima o maior entre os valores seguido por um espaço e a mensagem "eh o maior".
"""

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
maiorAB = (a + b + abs(a - b)) // 2

print(f"{maiorAB} é o maior!")
