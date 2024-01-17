#Funções ->estrutura da linguagem Python que pode ou,
#não receber um valor,processar alguma função, executar
#uma determinada ação.Dividir para conquistar.

'''def minha_funcao():
    soma = 0
    for i in range(0, 101):
        soma = soma + i
    print(soma)

def soma():
    print('Estou somando')

soma()
minha_funcao()
minha_funcao()
minha_funcao()'''

#Funções ->estrutura da linguagem Python que pode ou,
#não receber um valor,processar alguma função, executar
#uma determinada ação.Dividir para conquistar.
#parametros de entrada *args.

'''def soma_numeros(*args):
    soma = 0
    for i in args:
        soma = soma + i
    print(soma)

soma_numeros(1, 2, 3, 4, 5, 6, 7, 8)

#Funções ->estrutura da linguagem Python que pode ou,
#não receber um valor,processar alguma função, executar
#uma determinada ação.Dividir para conquistar.
#parametros de entrada *args.'''

#Funções ->estrutura da linguagem Python que pode ou,
#não receber um valor,processar alguma função, executar
#uma determinada ação.Dividir para conquistar.
#parametros de entrada *args dar ,empacota tudo dentro de tupla
#parametros de entrada **kwargs  nomes para parametro  empacota tudo dentro do dicionario.

'''def soma_numeros(**kwargs):
    x = kwargs.get('teste4')
    if x:
        print('foi passado')
    else:
        print('não foi passado')

soma_numeros(teste1 = 1, teste2 = 2, teste3 = 3, teste4 = 4)'''

# Retornar valores da função
#Cógigo abaixo do return não será executado nunca

def soma_valores(n1, n2):
    soma = n1 + n2
    if soma > 5:
        return soma
    print('TO AQUI')

soma = soma_valores(5, 2)
print (soma)
