import menu
print('''
    1-Cadastre-se
    2-Inscrever-se para ajudar em uma praia
    3-Adicione alguma praia que precise de nossa atenção
      
''')
escolha = int(input(''))
match escolha:
    case 1:
        menu.cadastro()

