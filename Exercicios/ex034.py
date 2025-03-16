# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("digite seu salario: "))

if salario >= 1250: 
    salarioNovo = (salario * 0.10) + salario
    print("Seu salario com aumento é {}".format(salarioNovo))
else: 
    salarioNovo2 = (salario * 0.15) + salario
    print("Seu salario com aumento é {}".format(salarioNovo2))
