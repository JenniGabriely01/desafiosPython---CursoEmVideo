# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere: US$1,00 - R$5,77

v = float(input("Digite o valor que você tem em real para converter a dólar: "))
c = v / 5.77

print("O valor R${} convertido a dólar é US${:.2f}".format(v, c))