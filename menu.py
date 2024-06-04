import programa
print('''
    1-Cadastre-se
    2-Inscrever-se para ajudar em uma praia
    3-Adicione alguma praia que precise de nossa atenção
      
''')
escolha = int(input(''))
match escolha:
    case 1:
        programa.cadastro()
    case 2:
        if programa.login == {}:
            print('''
    Faça o login primeiro ou cadastre-se.                
    1-Cadastro
    2-Login
''')
            escolha_menu = int(input(''))
        match escolha_menu:
            case 1:
                programa.cadastro()
            case 2:
                programa.login()
            
