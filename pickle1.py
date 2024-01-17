#import pickle,seriarizar objeto pegar algo da memoria,
#tornar persistente.

#import pickle

'''x = 1
# print(type(x))
print(pickle.dumps(x))'''
#import pickle,seriarizar objeto pegar algo da memoria,
#tornar persistente.
'''x = [1,2,3,4]
#print(type(x))
print(pickle.dumps(x))'''

#import pickle,seriarizar objeto pegar algo da memoria,
#tornar persistente.
'''x = [1,2,3,4]

string = pickle.dumps(x)
print(pickle.loads(string))'''
#import pickle,seriarizar objeto pegar algo da memoria,
#tornar persistente.
'''x = {'nome': 'irene','idade':20}

string = pickle.dumps(x)
print(pickle.loads(string)['nome'])'''

#import pickle,seriarizar objeto pegar algo da memoria,
#tornar persistente.

'''x = [1,2,3,4,]

arq = open('arquivo.pk1', 'wb')
pickle.dump(x, arq)

arq = open('arquivo.pk1', 'rb')
retornou = pickle.load(arq)

print(retornou)'''

'''import pickle
#import pickle,seriarizar objeto pegar algo da memoria,
#tornar persistente.

class Pessoa:
    nome = 'Irene'
    idade = 20


arq = open('arquivo.pk1', 'wb')
pickle.dump(Pessoa, arq)

arq = open('arquivo.pk1', 'rb')
retornou = pickle.load(arq)

print(retornou.idade)'''

'''import pickle
#import pickle,seriarizar objeto pegar algo da memoria,
#tornar persistente.

class Pessoa:
    nome = 'Irene'
    idade = 20

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoas('marcos' , 21)

with open('arquivo.pk1', 'wb') as arq:
pickle.dump(p1, arq)'''

#import pickle,seriarizar objeto pegar algo da memoria,
#tornar persistente.
import pickle

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criar uma instância da classe Pessoas
p1 = Pessoas('Marcos', 21)

# Salvar a instância p1 no arquivo usando pickle
with open('arquivo.pk1', 'wb') as arq:
    pickle.dump(p1, arq)



