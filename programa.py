import re
import random

contas = []  # Mudança para armazenar múltiplas contas
login_status = False  # Variável global para rastrear o estado de login
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
condicao_praia = ['suja', 'muito suja', 'inabitável']

def cadastro():
    global login_status    
    usuario = input('Digite o seu usuario: ')
    nome = input('Digite seu nome completo: ')
    senha = input('Digite sua senha: ')
    cpf = input('Digite seu cpf: ')
    email = input('Digite seu email: ')
    while True:    
        # Validação de senha
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
            print('A senha deve conter pelo menos um caractere especial')
            senha = input('Digite sua senha: ')
        elif not re.search(r'[A-Z]', senha):
            print('A senha deve ter pelo menos uma letra maiúscula')
            senha = input('Digite sua senha: ')
        elif len(senha) < 8:
            print('A senha deve ter pelo menos 8 caracteres')
            senha = input('Digite sua senha: ')
        else:
            break
    
    contas.append({'usuario': usuario, 'nome': nome, 'senha': senha, 'cpf': cpf, 'email': email})
    print('Cadastro realizado com sucesso!')
    login_status = True  # Marca como logado após o cadastro

def login():
    global login_status
    usuario = input('Digite o seu usuario: ')
    senha = input('Digite a senha: ')
    
    for conta in contas:
        if conta['usuario'] == usuario and conta['senha'] == senha:
            print(f'Bem-vindo, {conta["usuario"]}!')
            login_status = True  # Marca como logado após um login bem-sucedido
            return True
    print('Usuario ou senha inválido')
    return False

def pontos():
    nome_pessoas = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa', 
                    'Felipe', 'Gabriela', 'Henrique', 'Isabela', 'João', 'Larissa', 'Marcos']
    num_pessoas = random.randint(10, 20)  # Ajuste para um número razoável de pessoas
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
        print(f'{praia["nome"]}: {praia["votos"]} votos - {condicao_praia[random.randint(0, 2)]}')
    
    # Após a classificação das praias, pergunta ao usuário se deseja se inscrever para ajudar a limpar a praia vencedora
    print('''
1-Sim
2-Não''')
    
    escolha_inscricao = int(input('Deseja se inscrever para ajudar limpar a praia vencedora? '))
    match escolha_inscricao:
        case 1:
            print(f'\nVocê está inscrito na praia {lista_praias[0]["nome"]}')
        case 2:
            print('\nEntendo... Poderia nos dizer porque não deseja participar?')
            motivo = input('=> ')
        case _:
            print('Opção inválida')
