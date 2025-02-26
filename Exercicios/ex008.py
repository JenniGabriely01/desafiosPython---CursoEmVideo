# Escreva um programa que leia um valor em metros e a exiba convertido em cm e milimetros
v = float(input("Digite um valor em metros:"))
cm = v * 100
mm = v * 1000
print(" O valor {}m convertido a milimetros é {:.0f}mm\n Convertido para cm é {:.0f}cm".format(v, mm, cm))