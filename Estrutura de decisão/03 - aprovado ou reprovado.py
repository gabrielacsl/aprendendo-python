nota1, nota2= map(int, input('Notas: ').split())

media = (nota1 + nota2)/2

if media == 10:
    print('Aprovado com distinção.')
elif media >= 7:
    print('Aprovado.')
else:
    print('Reprovado.')

