# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

anoNascimento = int(input("Que ano você nasceu: "))
anoAtual = datetime.date.today().year
idade = anoAtual - anoNascimento
print("Você tem {}".format(idade))

if idade == 18:
    print("Está na hora do seu alistamento")
elif idade < 18:
    idadeAlista = 18 - idade
    print("Ainda não é a hora do seu alistamento, espere {} anos".format(idadeAlista))
elif idade > 18:
    atraso = idade - 18
    print("Você está atrasado. Seu alistamento era para ter ocorrido a {} anos".format(atraso))
