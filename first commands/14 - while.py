decisao = 0
testani = 0

while decisao != 3:
    decisao = int(input('1 para logar: \n2 para cadastrar: \n3 para sair: '))

    if decisao == 1:
        print('Logado')
    elif decisao == 2:
        print('Cadastrado')
    else:
        print('hm, saido?')

while testani < 10:
    print('{}'.format(testani))
    testani = testani + 1
