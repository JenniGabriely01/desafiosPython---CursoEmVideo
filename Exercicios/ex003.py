# Faça um programa que some dois números
num1 = int(input("Número 1:"))
num2 = int(input("Número 2:"))
# se o tipo for bool e eu não adicionar nenhum valo ele daria false, caso eu digite algum é true

soma = num1 + num2

# print(type(num1)) - descobre qual o tipo
# {} - mascara 
print("A soma entre {} e {} é {}".format(num1, num2, soma))