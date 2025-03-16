# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input("DIgite um nome: ")).strip()
silva ='silva' in nome.lower()
print(silva)