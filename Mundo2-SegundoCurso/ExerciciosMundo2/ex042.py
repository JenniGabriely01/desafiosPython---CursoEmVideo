#  Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes 

r1 = int(input("Digite o primeiro segmento: "))
r2 = int(input("Digite o segundo segmento: "))
r3 = int(input("Digite o terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os 3 podem ser um triangulo")
    
    if r1 == r2 == r3:
        print("É um triangulo equilátero") 
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print("É um triangulo escaleno ") 
    else:
        print("É um triangulo isósceles")
else:   
    print("Os 3 não podem ser um triangulo")    