#  Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles
from time import sleep

for c in range (10, 0, -1): # coloca 10 a 0
    print(c)
    sleep(1) # coloca 1s
print('PÁ, PÁ, PÁ')