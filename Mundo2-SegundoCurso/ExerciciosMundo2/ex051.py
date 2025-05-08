#  Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print( ''' 
======  10 termos de uma PA   ======  
      ''')

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
for c in range(termo, 11, razao):
    print(c, end=' ')