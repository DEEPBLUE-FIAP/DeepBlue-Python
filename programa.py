import re
conta = dict()
def cadastro():    
    while True: 
        global conta  
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
    conta['usuario'] = usuario
    conta['senha'] = senha  
def login():
    global conta
    username = input('Digite o seu usuario ')
    password = input('Digite a senha ')
    if conta == {}:
        print('Você ainda não possui uma conta')
    elif username != conta['usuario'] or password != conta['senha']:
        print('Usuario ou senha inválido')
    