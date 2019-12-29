print('M - matutino\nV - vespertino\nN - noturno\n')
turno = input('Periodo de estudo: ')


if turno == 'm' or turno == 'M':
    print('Bom dia!')
elif turno == 'v' or 'V':
    print('Boa tarde!')
else:
    print('Boa noite!')