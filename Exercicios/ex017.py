# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
h = hypot(co, ca)

print("A hiponesuna é: {:.2f}".format(h))