# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print("Sua média é: {}".format(media))

if media < 5.0:
    print("Reprovado")
elif media >= 5 and media < 7: # entre 5 e 6.9
    print("Recuperação")
elif media >= 7.0:
    print("Aprovado") 