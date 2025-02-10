"""Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, 
o valor que recebe por hora e calcula o salário desse funcionário.
A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
"""

num1 = int(input("Digite o numero do funcionario: "))
num2 =  int(input("Digite seu numero de horas trabalhadas: "))
num3 = float(input("Digite o valor da hora trabalhada: "))

salario = num2 * num3
print("Numero = ", num1)
print("Salario = ", salario) 