# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input("Digite seu peso: "))
altura = float(input('DIgite sua altura (cm): ')) / 100 # converte pra metros

imc = peso / (altura ** 2)
print("seu imc é {:.2f}".format(imc))

if imc < 18.15:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal')
elif imc >= 30 and imc <= 40:
    print('Você está em um caso de obesidade')
elif imc > 40:
    print('Você está em obesidade móbida')