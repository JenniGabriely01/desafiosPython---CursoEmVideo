#  Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
# o valor das parcelas 
# salario - 30% * anos * 12 
# prestação = valordacasa / anos * 12
valorImovel = float(input('Qual é o valor do imovél que você deseja: '))
salario = float(input('Qual é o seu salario: '))
anos = float(input('Em quantos anos você deseja pagar: '))

prestacao = valorImovel / (anos * 12) 
trintaPorCentoDoSalario = salario * 0.3

if prestacao <= trintaPorCentoDoSalario:
    print('Você pode financiar esse imovel. Suas prestações seram de: {:.2f} que significa menos que 30% do seu salario'.format(prestacao))
else:
    print("Negado! Para pegar uma casa de {} suas prestações seriam de {:.2f} e isso execede 30% do seu salario que é {}".format(valorImovel, prestacao, trintaPorCentoDoSalario))