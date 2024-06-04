import re
import random

conta = dict()
lista_praias = []
num_praias = 0
votos = []
lista_pontos = []
nomes_praias = [
    "Praia de Ponta Negra, Natal - RN",
    "Praia de Boa Viagem, Recife - PE",
    "Praia de Ipanema, Rio de Janeiro - RJ",
    "Praia da Pajuçara, Maceió - AL",
    "Praia do Futuro, Fortaleza - CE",
    "Praia da Enseada, Guarujá - SP",
    "Praia de São Conrado, Rio de Janeiro - RJ",
    "Praia de Meaípe, Guarapari - ES",
    "Praia de Atalaia, Aracaju - SE",
    "Praia do Farol da Barra, Salvador - BA"
]

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

def pontos():
    nome_pessoas = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa', 
                    'Felipe', 'Gabriela', 'Henrique', 'Isabela', 'João', 'Larissa', 'Marcos']
    num_pessoas = random.randint(0, 255)
    lista_pontos = []
    for i in range(num_pessoas):
        lista_pontos.append({"nome": nome_pessoas[random.randint(0, 11)], "pontos": random.randint(50, 1000)})
    
    lista_pontos.sort(key=lambda x: x["pontos"], reverse=True)
    
    print('Classificação de cada pessoa:')
    for pessoa in lista_pontos:
        print(f'{pessoa["nome"]}: {pessoa["pontos"]} pontos')

def votos():
    while len(lista_praias) < random.randint(5, 10):
        i = len(lista_praias) % len(nomes_praias)
        lista_praias.append({"nome": nomes_praias[i], "votos": random.randint(0, 1000)})
    
    lista_praias.sort(key=lambda x: x["votos"], reverse=True)
    
    print('Classificação das praias:')
    for praia in lista_praias:
        print(f'{praia["nome"]}: {praia["votos"]} votos')