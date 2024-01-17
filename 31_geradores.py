#Geradores para evitar gastar memoria ram
#Instale a Biblioteca, pympler = pip install pympler
#yield função geradora
'''import re
from pympler.asizeof import asizeof

def dobro(lista):
    for i in lista:
        yield i*2

def dobro2(lista):
    lista_2 = []
    for i in lista:
        lista_2.append(i)
    return lista_2

y = dobro2(range(0, 10000))
x = dobro(range(0, 10000))

print(asizeof(y))
print(asizeof(x))'''

#Geradores para evitar gastar memoria ram
#Instale a Biblioteca, pympler = pip install pympler
#yield função geradora

from pympler.asizeof import asizeof

def dobro(lista):
    for i in lista:
        yield i*2

x = dobro(range(0, 100))

for i in x:
print(x)