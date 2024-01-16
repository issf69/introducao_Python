#Faça um programa que o usuário possa cadastrar n ,
# pessoas,armazenando seu nome idade e altura.

'''pessoas = []
while True:
    decisão = int(input('Digite 1 para cadastrar uma pessoa e 2 par sair: '))
    if decisão == 2:
        break

    pessoa = {'nome': input('Digite o nome:'),
            'idade': input('Digite a idade:'),
            'altura': input('Digite a altura: ')}

    pessoas.append(pessoa)

print(pessoas)'''

#Criar chaves que não foram predefinidas em um dicionário.
pessoa = {'nome': 'Thalita França', 'idade': 29, 'altura': 175}
pessoa.update({'cep': '34000000', 'rua': 'Minha rua'})

print(pessoa)