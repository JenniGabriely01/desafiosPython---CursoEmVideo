# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

valor = float(input("Digite o valor: "))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista/cheque
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: preço formal 
[ 4 ] 3x ou mais no cartão: 20% de juros
      ''')
opcao = int(input('Qual opção você deseja: '))

if opcao == 1:
    descontoDez = valor - (valor * 0.1)
    print('Você ganhou 10% de desconto. O valor final ficou em {}'.format(descontoDez))
elif opcao == 2:
    descontoCinco = valor - (valor * 0.05)
    print('Você ganhou 5% de desconto. O valor final ficou em {}'.format(descontoCinco))
elif opcao == 3: 
    print('O seu preço ficará {}'.format(valor))
elif opcao == 4:
    juros = valor + (valor * 0.2)
    print('O seu valor terá um acrescimo de {}'.format(juros))