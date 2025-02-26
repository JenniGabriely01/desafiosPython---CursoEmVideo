# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
a = float(input("Digite o angulo que você deseja: "))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print("O seno desse ângulo é: {:.2f} \nO cosseno desse ângulo é: {:.2f}\nA tangente desse ângulo é: {:.2f}".format(s, c, t))