# condições aninhadas é quando tem uma coisa dentro da outra 
# if
# elif
# else (Em condições aninhadas o else é opcional)

nome = str(input('Qual é o seu nome? '))

if nome == 'Jennifer':
  print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
  print('Seu nome é bem comum no Brasil')
elif nome in 'Ana Claúdia Jessica':
  print('Belo nome feminino')
else:
  print('Seu nome é bem normal')
print('Tenha um bom dia, {}'.format(nome))