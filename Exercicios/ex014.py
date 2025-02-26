# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
Tc = int(input("Digite a temperaura em Celsius: "))
TcF = Tc * 1.8 + 32

print("O valor da temperatura {} em Fahrenheit é: {}F".format(Tc, TcF))