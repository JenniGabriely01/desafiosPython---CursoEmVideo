# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nomeCompleto = str(input("Digite seu nome inteiro: ")).strip()
pNome = nomeCompleto.split()[0]
print("O primeiro nome é {}".format(pNome))
print("O seu segundo nome é {}".format(nomeCompleto[len(nomeCompleto)-1]))
