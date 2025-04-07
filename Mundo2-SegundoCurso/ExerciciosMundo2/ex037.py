# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
valor = int(input('Digite um número inteiro: '))
print('---valores---\n[ 1 ] converter para binário \n[ 2 ] converter para OCTAL \n[ 3 ] converter para haxadecimal')
numeroEscolha = int(input('Digite o número referente a qual você deseja converter: '))

if numeroEscolha == 1:
    print('O valor {} convertido a binário é {}'.format(valor, bin(valor)[2:]))
elif numeroEscolha == 2:
    print('O valor {} convertido a Octal é {}'.format(valor, oct(valor)[2:]))
elif numeroEscolha == 3:
    print('o valor {} convertido a Hexadecimal é {}'.format(valor, hex(valor)[2:]))
else:
    print('Opção invalida')