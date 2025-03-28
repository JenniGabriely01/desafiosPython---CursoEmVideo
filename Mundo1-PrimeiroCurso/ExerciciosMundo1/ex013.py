# Faça um algorimo que leia o salario de um funcionário e coloque um aumento de 15%
s = float(input("Digite o salario: "))
sAumento = s * 15/100 + s
print("o salario {:.2f} com um aumento de 15% é: {:.2f}".format(s, sAumento))