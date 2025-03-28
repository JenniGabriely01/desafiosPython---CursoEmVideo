frase = "Curso em video python"
print(frase[3])
# resultado = s (pega a quarta letra)

print(frase[3:13])
# resultado = so em vide ( da quarta a decima segunda)

print(frase[13:])
# resultado = o python (da decima quarta para o final)

print(frase.upper())
print(frase.lower())
print(frase.count('o')) # conta os 0´s
print(frase.replace('python', 'android')) # apenas com esse codigo não muda efetivamente, apenas substitui naquele momento. Para salvar tenho que atribuir a var frase novamente com - frase = print(frase.replace('python', 'android'))
print('Curso' in frase)
dividido = frase.split() # separa a frase 
print(dividido[2]) # mostra a segunda palavra da frase
