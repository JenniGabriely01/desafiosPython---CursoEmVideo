# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date

anoNascimento = int(input("Digite o ano do seu nascimento: "))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
if idade <=9:
    print("Mirim")
elif idade >=10 and idade <= 14:
    print("Intantil")
elif idade >= 15 and idade <= 19:
    print("Junior")
elif idade >= 20 and idade <= 25:
    print("Pleno")
elif idade >= 26:
    print("Master")