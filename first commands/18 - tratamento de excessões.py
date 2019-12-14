try:
    x = int(input('idade: '))

except:
    print('Entrada inválida')
else:
    print(f'Sua idade é {x}')
finally:
    print('Obrigado.')