#nomes = ['Thalita', 'Agatha', 'Reinaldo' , 'Irene']

#print(type(nomes))
#print(nomes)
#print(nomes[0])#print(nomes[1])
#print(nomes[2])
#print(nomes[3])
# se colocar indice que não existe apresenta erro, porque colocamos somente 4 nomes ,
#e o primeiro começa com 0
#print(nomes[4])
# acrescentando Len para ver o tamanho da lista
#print(len(nomes))

# Vamos alterar valores.
#nomes = ['Thalita', 'Agatha', 'Reinaldo' , 'Irene']
#nomes[0] = "Thalita França"
#print(nomes[0])
# O python permite varios tipos de dados em um lista.
# #nomes = ['Thalita', 'Agatha', 'Reinaldo' , 'Irene', 21, 2.05, True, 'thalita.encode()']

#print(nomes)

#append adiciona nomes na lista
#nomes = ['Thalita', 'Agatha', 'Reinaldo' , 'Irene']
#nomes.append('Madruguinha')
#nomes.append('Vida')
#print(nomes[5])

#nomes = []
#while True:
    #nome = input('Digite -1 para sair ou cadastre um nome: ')
    #if nome == "-1":
    # break
# nomes.append(nome)

#print(nomes)

#append adiciona nomes na lista  no final .
#Para adicionar em qualquer posição veja abaixo usando insert:

#nomes = ['Thalita', 'Agatha', 'Reinaldo' , 'Irene']
#nomes.insert(1, 'Madruguinha')

#print(nomes)

# pop remove o ultimo valores da lista.

#nomes = ['Thalita', 'Agatha', 'Reinaldo' , 'Irene']
#nomes.pop()
#nomes.pop(0)
#nomes.pop(1)
#Erro apagar indice que não existe.
#nomes.pop(10)
#print(nomes)

#Remover valores de uma lista .remove

#nomes = ['Thalita', 'Agatha', 'Reinaldo' , 'Irene' ,'Thalita']
#remove somente uma Thalita
#nomes.remove('Thalita')
# para remover duas Thalita
#nomes.remove('Thalita')
#nomes.remove('Madruguinha')
#Apresenta erro porque não existe Madruguinha na Lista.

#print(nomes)

#Vamos aprender qual índice está em um determinado elemento método index.
#nomes = ['Thalita', 'Agatha', 'Reinaldo' , 'Irene' ,'Thalita']
#nomes = ['Thalita', 'Agatha', 'Agatha', 'Reinaldo' , 'Irene' ,'Thalita']
#Mesmo colocando dois nomes Agatha pemanece na mesma posição 1
#print(nomes.index('Agatha'))
#Se colocarmos nome que não existe vai apresentar erro
#print(nomes.index('Madruguinha'))
#print(nomes)
#nomes = ['Thalita', 'Agatha', 'Agatha', 'Reinaldo' , 'Irene' ,'Thalita']
#nomes.pop(nomes.index('Reinaldo'))
# melhor forma para se fazer
#nomes.remove('Reinaldo')
#print(nomes)

# Ordenar uma determinada lista na Linguagem Python  (sort)
#ordem alfabética pode ser lista de string ou números
#nomes = ['Thalita', 'Agatha','Reinaldo' , 'Irene' ,]
#nomes = [3, 5, 7, 27, 45, 60, 1.6]
#nomes.sort()
#nomes.sort(reverse=True)
#decrescente
# caso não queira mudar a lista usamos  sorted
#não altera lista original
#sorted(nomes)
#print(sorted(nomes))
#para sorted não mexer na list original
#nomes_ordenado = sorted(nomes)
#nomes_ordenado = sorted(nomes,reverse=True)
#Sempre  que quiser alterar usa( .sorted )   alterar lista original ,
# (sorted )cria uma nova lista ou mantem
#print(nomes_ordenado)

#Iteração, iterar sobre uma lista

#for i in range(0, 5)
#x = list( range(0, 5))
#print(x)

#idades = [3, 5, 7, 27, 45, 60, 1.6]

#for i in range(0, len(idades)):
    #print(idades[i])
    #printar valor e posição
    #print(idades[i], i)

    #no python
    #for i in idades
    # #enumerate:
#x = list(enumerate(idades))
#print(x)
#idades = [3, 5, 7, 27, 45, 60, 1.6]
#for i in enumerate(idades):
#for i,j in enumerate(idades):
#print(i)
#print(type(i))
# diferentes da lista tuple não pode mudar de valor
#print(i[0])
#print(i[1])
#idades_pares = []
#for i in idades:
    #print(f'i = {i} j = {j}')
    #if i % 2 == 0:
        #idades_pares.append(i)
    #print(i)
#print(idades_pares)

# Matrizes e listas de listas
#uma lista pode  conter uma lista dentro dela
#vamos subdividir entre lista e colunas
'''idades = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 14, 15]]'''

#No python não precisa necessariamente,
#ter uma matriz pode ter listas de listas
# lista dentro de lista bidimensional ou  trimedissional.

# para iterar este elementos
'''for i in range(0, len(idades)):
    #print(idades [i])
    for j in range(0, len(idades[i])):
        print(idades[i] [j])'''

#Porque uma lista é igual a outra.
# x = 2
# y = x
# y = 3
#print(x)
#print(y)
#x = 2
#y = x
#print(id(x))
#print(id(y))
# #print(hex(id(x)))
#print(hex(id(x)))
#x = [1, 2, 3]
#print(hex(id(x)))
#x = [1, 2, 3]
#y = x
#print(hex(id(x)))
#print(hex(id(y)))

'''x = [1, 2, 3]
y = x
y[0] = 0

print(x)
print(y)
Algo não esperado'''
'''x = [1, 2, 3]
y = x.copy()
y[0] = 0

print(x)
print(y)
#dois valores diferente'''
'''x = [1, 2, 3]
y = x
z = x.copy()
y[0] = 0

print(hex(id(x)))
print(hex(id(y)))
print(hex(id(z)))

#.copy'''

#Lista permite que tenha dados repetidos --> ,
#Conjuntos não permite que tenha dados repetidos
'''x ={1, 2, 3, 4, 5,}
y ={5, 7, 8, 8, 8,}

x = x.difference(y)
print(x)'''

#Lista permite que tenha dados repetidos --> ,
#Conjuntos não permite que tenha dados repetidos
#set conjuntos
'''x =[1,1,1,2,2,3,4,5]
x = set(x)
print(x)'''
#Lista permite que tenha dados repetidos --> ,
#Conjuntos não permite que tenha dados repetidos
#set conjuntos
#criar um set diretamente
'''x ={1,1,2,3,4,5}
print(x)'''


#Lista permite que tenha dados repetidos --> ,
#Conjuntos não permite que tenha dados repetidos
#set conjuntos
#criar um set diretamente
#união de conjuntos

'''x = {1,2,3,4,5}
y = {6,7,8,9,10}

t = x.union(y)
print(t)'''

#Lista permite que tenha dados repetidos --> ,
#Conjuntos não permite que tenha dados repetidos
#set conjuntos
#criar um set diretamente
#união de conjuntos
#intersessão (intersection)

'''x = {1,7,3,4,5}
y = {5,7,8,9,10}

x = x.intersection(y)
print(x)'''

#Lista permite que tenha dados repetidos --> ,
#Conjuntos não permite que tenha dados repetidos
#set conjuntos
#criar um set diretamente
#união de conjuntos
#intersessão (intersection)
#diferença

'''x = {1,2,3,4,5}
y = {5,7,8,9,10}

x = x.difference(y)
print(x)'''

#Conjuntos não permite que tenha dados repetidos
#set conjuntos
#criar um set diretamente
#união de conjuntos
#intersessão (intersection)
#diferença
#symmetric_difference , pega os dois conjuntos e vai retornar a ,
#soma dos conjunto,igual união a detalhe interção não conta não entra
#porque aparece nos dois conjuntos

'''x = {1,2,3,4,5}
y = {5,7,8,9,10}

x = x.symmetric_difference(y)
print(x)'''

# Arquivos #1  armazenamento persistente dos dados,
# Abre o arquivo no modo de leitura ('r')

'''arquivo = open('pessoas.txt', 'a')
i = 0
while True:
    if i > 4:
        break
    arquivo.write(input('Digite o nome da pessoa') + " " + input("Digite a idade") + "\n")
    i += 1'''

'''arquivo = open('pessoas.txt', 'r')

resultados = arquivo.readlines()
x = []
for i in resultados:
    x.append(i.split())

print(x[1][1])
arquivo.close()'''

# Arquivos #1  armazenamento persistente dos dados,
# Abre o arquivo no modo de leitura ('r')
'''with open('pessoas.text', 'r') as arq:
    x = arq.read()
    print'''
# Abre o arquivo no modo de leitura ('r')
'''arquivo = open('pessoas.txt', 'r')

# Lê todas as linhas do arquivo e armazena em 'resultados'
resultados = arquivo.readlines()

# Cria uma lista vazia 'x' e divide cada linha em palavras
x = [linha.split() for linha in resultados]

# Fecha o arquivo após a leitura
arquivo.close()

# Imprime o elemento na segunda coluna da segunda linha (considerando que o índice começa em 0)
print(x[1][1])'''

with open('pessoas.text', 'r') as arq:
    x = arq.read()
    print(x)