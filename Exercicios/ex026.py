# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input("Digite uma frase: ").strip().lower()
conta = frase.count("a")
posicao = frase.find('a')+1
uposicao = frase.rfind('a')+1
print(" A letra A aparece:  {}".format(conta))
print("A letra a apareceu pela primeira vez na posição {}".format(posicao))
print("A última letra a aparece na posição {}".format(uposicao))