import programa

while True:
    print('''
        Bem-vindo ao DeepBlue, aqui você ajuda tudo e todos, tornando o mundo um lugar melhor.
        1 - Cadastre-se
        2 - Adicione alguma praia que precise de nossa atenção
        3 - Praias para votar
        4 - Simulação da praia e pessoa vencedora
        5 - Sistema de pontos
        6 - Deslogar
        7 - Sair
    ''')

    escolha = int(input('Escolha uma opção: '))
    match escolha:
        case 1:
            usuario = input('Digite o seu usuário: ')
            nome = input('Digite seu nome completo: ')
            senha = input('Digite sua senha: ')
            cpf = input('Digite seu CPF: ')
            email = input('Digite seu email: ')
            programa.cadastro(usuario, nome, senha, cpf, email)
            programa.login_status = True  # Marca como logado após o cadastro
        case 2:
            if not programa.login_status:
                print('Você não está logado')
                if not programa.login():
                    print('''
        Cadastre-se.
        1 - Cadastro
        2 - Sair
    ''')
                    escolha_menu = int(input('Escolha uma opção: '))
                    match escolha_menu:
                        case 1:
                            usuario = input('Digite o seu usuário: ')
                            nome = input('Digite seu nome completo: ')
                            senha = input('Digite sua senha: ')
                            cpf = input('Digite seu CPF: ')
                            email = input('Digite seu email: ')
                            programa.cadastro(usuario, nome, senha, cpf, email)
                            programa.login_status = True  # Marca como logado após o cadastro
                        case 2:
                            print('Voltando à tela inicial...')
            if programa.login_status:
                praia = input('Digite o nome da praia: ')
                programa.lista_praias.append({"nome": praia, "votos": 0})
                print(f'Você adicionou a praia {praia}, agora ela será verificada pelo órgão regulador')
                programa.num_praias += 1
        case 3:
            print("\nPraias disponíveis para votar:")
            for i, praia in enumerate(programa.lista_praias):
                print(f'{i} - {praia["nome"]} (votos: {praia["votos"]})')

            voto = int(input('Número da praia que você deseja votar: '))
            if 0 <= voto < len(programa.lista_praias):
                programa.lista_praias[voto]["votos"] += 1
                print(f'Você votou na praia {programa.lista_praias[voto]["nome"]}. Agora ela tem {programa.lista_praias[voto]["votos"]} votos.')
            else:
                print("Número da praia inválido.")
        case 4:
            print('''
                1 - Simulação de pontos
                2 - Simulação de votos
''')
            escolha_simulacao = int(input('Digite qual você quer: '))
            match escolha_simulacao:
                case 1:
                    programa.pontos()

                case 2:
                    programa.votos()
        case 5:
            print('''
                1 - Cadastro -> 50 pontos.
                2 - Voto -> 05 pontos.
                3 - Presença no evento -> 20 pontos.
                4 - Destaque no evento -> 100 pontos.
                5 - Contribuir com informações sobre espaços sujos -> 1 ponto.
                6 - Adicionar nova praia -> 100 pontos.
                No fim do mês quem juntou mais pontos ganha:
                    O primeiro lugar ganha uma viagem para Pensilvânia.
                    O segundo lugar ganha uma viagem para Angra dos Reis.
                    O terceiro lugar ganha um kit da empresa ou do órgão que cuidou da empresa.
''')
        case 6:
            if not programa.login_status:
                print('Você não está logado.')
            else:
                print('Saindo da conta...')
                programa.login_status = False
        case 7:
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Tente novamente.")
