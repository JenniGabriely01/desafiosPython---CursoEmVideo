# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
qtdDias = float(input("Quantos dias de uso? "))
kmPercorridos = float(input("Quantos km foram percorridos? "))
valor = (qtdDias * 60) + (0.15 * kmPercorridos)

print("O valor total a ser pago é: R${}".format(valor))