# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ela
n1 = input("digite algo ")
print("Qual o tipo?", type(n1))
print("É um valor númerico?", n1.isnumeric())
print("É um valor alfabetico?", n1.isalpha())
print("Está em letra maiuscula?", n1.isupper())
print("Está em letra minucula?", n1.islower())
print("É uma letra ou número(alfanumerico)?", n1.isalnum())
print("Só tem espaços?", n1.isspace())
print("Está capitalizada?(Primeira letra maiuscula)", n1.istitle())

