#Receba um número inteiro do usuário e mostre a tabuada deste número.

n1 = int(input('Digite qual número deseja saber a tabuada: '))

'''i = 1
while i <= 10:
    print(i)
    print(n1)
    i += 1'''

i = 1
while i <= 10:
    print(f"{n1} x {i} == {n1*i}")
    i += 1
