# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
num1 = float(input('Digite o primeiro num: '))
num2 = float(input('Digite o segundo num: '))

if num1 > num2:
    print('Número 1 é maior')
elif num2 > num1:
    print('Número 2 é maior')
elif num1 == num2:
    print('Os dois são iguais') 