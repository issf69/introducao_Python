#Lambda - programação funcional sempre retorna algo

'''def teste():
    return lambda *idade: print(idade)

x = teste()

x('Irene', 'Agatha')'''

# Filter - programação funcional ,
'''x = [{'nome': 'Irene', 'idade': 54}, {'nome': 'Thalita', 'idade': 29}]

x = list(filter(lambda x: x['nome'] == 'Irene', x))

print(x)'''

# MAP programação funcional mudança em uma determinada lista,

x = [{'nome': 'Irene', 'idade': 20}, {'nome': 'Agatha', 'idade': 22}]

x = list(map(lambda x: {'nome': x['nome'], 'idade': 'menor que  30 anos'} if x['idade'] < 30 else(x), x))

print(x)