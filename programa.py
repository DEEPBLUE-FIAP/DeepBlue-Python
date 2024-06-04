import re
cadastro = {}
def cadastro():
    while True:    
        usuario = input('Digite o seu usuario ')
        nome = input('Digite seu nome completo')
        senha = input('Digite sua senha ')
        cpf = int(input('Digite seu cpf '))
        email = input('Digite seu email ')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
            print('A senha deve conter pelo menos um caractere especial')
        elif not re.search(r'[A-Z]', senha):
            print('A senha deve ter pelo menos uma letra maíuscula')
        elif len(senha) < 8:
            print('A senha deve ter pelo menos 8 caracteres')
        else:
            break