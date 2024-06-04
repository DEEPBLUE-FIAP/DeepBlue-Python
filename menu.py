import programa

while True:
    print('''
        1 - Cadastre-se
        2 - Adicione alguma praia que precise de nossa atenção
        3 - Praias para inscrever-se
        4 - Sair
    ''')

    escolha = int(input('Escolha uma opção: '))
    match escolha:
        case 1:
            programa.cadastro()
        case 2:
            if not programa.login():
                print('''
        Cadastre-se.                
        1 - Cadastro
    ''')
                escolha_menu = int(input('Escolha uma opção: '))
                match escolha_menu:
                    case 1:
                        programa.cadastro()
                    
            praia = input('Digite o nome da praia: ')
            programa.lista_praias.append({"nome": praia, "votos": 0})
            print(f'Você adicionou a praia {praia}, agora ela será verificada pelo órgão regulador')   
            programa.num_praias += 1
                                    
        case 3:
            print("\nPraias disponíveis para votar:")
            for i, praia in enumerate(programa.lista_praias):
                print(f'{i} - {praia["nome"]} (votos: {praia["votos"]})')
            
            voto = int(input('Digite o número da praia que você deseja votar: '))
            if 0 <= voto < len(programa.lista_praias):
                programa.lista_praias[voto]["votos"] += 1
                print(f'Você votou na praia {programa.lista_praias[voto]["nome"]}. Agora ela tem {programa.lista_praias[voto]["votos"]} votos.')
            else:
                print("Número da praia inválido.")
        case 4:
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Tente novamente.")

    