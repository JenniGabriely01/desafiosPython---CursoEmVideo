# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
t = int(input('Digite um número: '))

for c in range(1, 11):
    res = c * t
    print('{} x {} = {}'.format(t, c, res))