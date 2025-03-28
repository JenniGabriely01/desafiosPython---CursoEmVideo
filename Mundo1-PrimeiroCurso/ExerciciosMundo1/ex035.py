# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# Para que três segmentos formem um triângulo, a soma de dois lados deve ser sempre maior que o terceiro lado. 
r1 = float(input("Digite o valor 1: "))
r2 = float(input("Digite o valor 2: "))
r3 = float(input("Digite o valor 3: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os 3 podem ser um triangulo")
else:
    print("Os 3 não podem ser um triangulo")