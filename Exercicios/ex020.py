#  O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))

lista = [ a1, a2, a3, a4 ]
lSorteado = random.sample(lista, 4)
# sample - serve para sortear uma qtd especifica de elementos
# shuffle -  Embaralha os elementos de uma lista existente aleatoriamente. 
print("A ordem de apresentação será {}".format(lSorteado))