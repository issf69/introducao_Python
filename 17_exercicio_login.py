#Defina um usuário e senha e depois verifique se
#login do usuário é válido.

USUARIO = "irene"
SENHA = "minha_senha123"

while True:
    usuario_login = input('Didite seu nome de usuário: ')
    senha_login = input('Digite sua senha:')

    if usuario_login == USUARIO and senha_login == SENHA:
        print('Você foi logado no sistema!')
        break
    else:
        print('Usuario ou senha inválido.')