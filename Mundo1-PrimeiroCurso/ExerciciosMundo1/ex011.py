# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a qtd de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados
a = float(input("Digite a altura da parede(m):"))
l = float(input("Digite a largura da parede(m):"))

area = a * l
qtdDeTinta = area / 2

print("A área dessa parede é {}, se cada litro pinta 2m a quatidade de tinta necessaria é: {}".format(area, qtdDeTinta))