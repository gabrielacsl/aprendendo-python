letra = input('Digite uma letra: ')[0]

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('{} é uma vogal.'.format(letra)) 
elif letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('{} é uma vogal.'.format(letra)) 
else:
    print('{} é uma consoante'.format(letra))