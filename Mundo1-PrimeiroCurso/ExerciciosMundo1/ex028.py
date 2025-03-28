# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
# randint - gera um número inteiro
num = random.randint(0, 5)
numU = int(input("Digite um número de 0 a 5: "))
print("Processando...")
sleep(3)
if numU == num:
    print("Você acertou. Parabéns")
else:
    print("Não foi dessa vez. Tente novamente")