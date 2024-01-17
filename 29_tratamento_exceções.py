#Tratamento de exceções #1  tente fazer alguma coisa ,
# se não,se conseguir ok, senão tente outra,
#try = tente except = se não consegui finally = finalizado

'''n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))

try:
    print(n1/n2)
except:
    print('Não consegui')
finally:
    print('Finalizado!')'''



#Tratamento de exceções #1  tente fazer alguma coisa ,
# se não,se conseguir ok, senão tente outra,
#try = tente except = se não consegui finally = finalizado
# vamos tratar cada exceção de  forma diferente

'''try:
    x = int(input('Digite um número: '))
    print(5/x)
except ValueError:
    print('Digite um número!')
except ZeroDivisionError:
    print('Não digite 0')'''

#Tratamento de exceções #1  tente fazer alguma coisa ,
# se não,se conseguir ok, senão tente outra,
#try = tente except = se não consegui finally = finalizado
# vamos tratar cada exceção de  forma diferente
# Vamos capturar a exceção que foi dada.

try:
    x = int(input('Digite um número: '))
    print(5/x)
except Exception as e:
    print('Erro interno do sistema')