# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))
num3 = float(input("Digite o número 3: "))

lista = num1, num2, num3
maior = max(lista)
menor = min(lista)
 
print("O maior número é {}".format(maior))
print("O menor número é {}".format(menor))
