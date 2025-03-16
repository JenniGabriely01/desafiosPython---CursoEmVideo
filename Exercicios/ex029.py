#  Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual a velocidade do carro(km)? '))
if velocidade <= 80:
    print("Você está na velocidade permitida")
else: 
    m = (velocidade - 80) * 7
    print("Voce foi multado!!! O limite é 80km")
    print("você pagará uma multa de R${:.2f}".format(m))