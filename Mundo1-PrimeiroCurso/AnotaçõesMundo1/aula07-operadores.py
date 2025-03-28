#- + - adição
#- - - menos
#- * - multiplicação
#- / - divisão
#- ** - potencia ou pow(n1,n2)
#- // - divisão inteira (5//2 = 2) é a divisão “arredondada”
#- % resto da divisão (5%2 =1) - (18%2 = 0, dá 0 pq não sobra nada na divisao)

n1 = int(input("Valor 1: "))
n2 = int(input("Valor 2: "))

s = n1 + n2
sub = n1 - n2
d = n1 / n2
m = n1 * n2
di = n1 // n2 # divisão inteira

print("A soma é {} \n, a subtração é {}, a divisão é {:.3f} e a multiplicação é {}".format(s, sub, d, m), end='') 
print("A divisõa inteira é: {}".format(di))
# {:.3f} - determina a quantidade maxima de casas
# end ='' - deixa os dois prints em uma linha só
# \n - quebra a linha