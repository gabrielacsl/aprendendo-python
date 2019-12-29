nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media > 9:
    print('Media: {:.1f}'.format(media))
    print('Conceito: A')
elif media > 7.5:
    print('Media: {:.1f}'.format(media))
    print('Conceito: B')
elif media > 6:
    print('Media: {:.1f}'.format(media))
    print('Conceito: C')
elif media > 4:
    print('Media: {:.1f}'.format(media))
    print('Conceito: D')
elif media < 4:
    print('Media: {:.1f}'.format(media))
    print('Conceito: E')