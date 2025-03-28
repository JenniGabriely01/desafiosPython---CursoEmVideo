#  Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input("Qual a distância da sua viagem(km)? "))

if distancia <= 200:  
    valor1 = distancia * 0.50
    print("Essa viagem tera o custo de {}".format(valor1))
else:
    valor2 = distancia * 0.45
    print("Essa viagem tera o custo de {}".format(valor2)) 
       