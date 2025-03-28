#  Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = input("Digite seu nome completo: ").strip() # elimina espaços
nMa = nome.upper()
nMi = nome.lower()
cPNome = len(nome)-nome.count(' ') # tira os espaços no meio do nome
PNome = nome.split()[0] # separa o primeiro nome
Snome = nome.split()[1] # separa o segundo nome
qtdLetras = len(PNome) # conta as letras
qtdLetrasS = len(Snome)
print("Nome em maiusculo: {}\nNome em minusculo:{}\nQtd de caracteres no nome inteiro: {}\n Qtd de caracteres no primeiro nome: {}\nQtd de caracteres do segundo nome: {}".format(nMa, nMi, cPNome, qtdLetras, qtdLetrasS))