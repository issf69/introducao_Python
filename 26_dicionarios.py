#Estrutura de dados ,dicionarios pode comparar ,
#com lista,pode armazenar mais de um valor atraves
#de chaves.
#x = {'nome': 'Irene', 'idade':54, 'cep': '123456'}
#print(x)

#acessar uma unica posição
#print( x['nome'] )

#maneira mais organizada
'''pessoa = {'nome': 'Irene', 'idade':54, 'cep': '123456'}
pessoa['nome'] = 'Marcos'
print(pessoa)'''

'''pessoas = [{'nome':'Irene','idade': 54, 'altura': 162},
            {'nome':'Agatha', 'idade': 26, 'altura': 162},
            {'nome':'Thalita', 'idade': 29, 'altura':173}]

for pessoa in pessoas:
    print(pessoa['nome'])'''

#Iterar sobre chaves, valores  e chaves e valores juntos, usamos items

'''pessoa = {'nome':'Irene','idade': 54, 'altura': 162}
for i, j in pessoa.items():
    print(f'i = {i} j = {j}')'''

#caso queira somente as chaves

'''pessoa = {'nome':'Irene','idade': 54, 'altura': 162}
for i in pessoa.keys():
    print(i)'''

#caso queira somente valores
pessoa = {'nome':'Irene','idade': 54, 'altura': 162}
for i in pessoa.values():
    print(i)