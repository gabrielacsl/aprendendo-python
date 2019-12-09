nome = input('Nome:')
idade = int(input('Idade:'))
prova1 = int(input('Primeira prova:'))
prova2 = int(input('Segunda prova:'))
media = (prova1 + prova2) / 2
nome = nome.title()


if idade >= 18 and media >= 6:
    print('{} Aprovado'.format(nome))
else:
    print("{} Reprovado".format(nome))
