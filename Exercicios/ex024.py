# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nomeCidade = input("Digite um nome de uma cidade: ").strip()
# startwith - verifica se começa com santp
pNome = nomeCidade.lower().startswith("santo")

# outra forma de resolver - print(cid[:5] == 'Santo') - verifica se as 5 primeiras letras são santo
print(pNome)  