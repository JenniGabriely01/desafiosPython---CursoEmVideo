nome = input("qual é o seu nome?") # Base

# Formatos
print("Prazem em te conhecer {:20}!".format(nome))
# Resultado = Prazem em te conhecer nome                !

print("Prazem em te conhecer {:>20}!".format(nome))
# Resultado - Prazem em te conhecer                nome!

print("Prazem em te conhecer {:<20}!".format(nome))
# Resultado - Prazem em te conhecer  nome              !

print("Prazem em te conhecer {:^20}!".format(nome))
# Resultado - Prazem em te conhecer        nome        !

print("Prazem em te conhecer {:=^20}!".format(nome))
# Resultado - Prazem em te conhecer =======nome========!