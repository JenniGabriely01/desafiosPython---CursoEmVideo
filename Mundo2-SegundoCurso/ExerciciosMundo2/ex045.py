from random import randint

# Lista de opções
itens = ['Pedra', 'Papel', 'Tesoura']
itemSort = randint(0, 2)

print('''Opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura 
''')

opcao = int(input('Digite sua opção: '))

# Verifica se a opção é válida
if opcao < 1 or opcao > 3:
    print('Opção inválida!')
else:
    jogador = itens[opcao - 1]
    computador = itens[itemSort]

    print(f"Jogador jogou {jogador}")
    print(f"Computador jogou {computador}")

    if jogador == computador:
        print('EMPATE!!')
    elif (jogador == 'Pedra' and computador == 'Tesoura') or \
         (jogador == 'Papel' and computador == 'Pedra') or \
         (jogador == 'Tesoura' and computador == 'Papel'):
        print('JOGADOR VENCEU!')
    else:
        print('COMPUTADOR VENCEU!')
