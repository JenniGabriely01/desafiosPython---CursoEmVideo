# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
for c in range (1, 501):
    if c % 3 == 0: # se o num for divisivel p 3 ele é somado
        soma += c
print(soma)