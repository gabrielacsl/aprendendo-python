numero = []
for i in range(0, 3, 1): 
    numero.append(int(input('Valor para a posição {}: '.format(i))))
print('Você digitou os numeros {}'.format(numero))
numero.sort(reverse = True)
print(numero)