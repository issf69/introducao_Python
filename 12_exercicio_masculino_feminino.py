#Receba F para feminino e M para masculino e exiba o sexo da pessoa.

sexo = input(' Digite F para feminono e M para masculino: ')

if sexo == 'F' or sexo == 'f':
    print("Você é do sexo Feminino.")
elif sexo == 'M' or sexo == 'm':
    print("Você é do sexo Masculino.")
else:
    print('Valor inválido')

