numero = []
for i in range(0, 5, 1): 
    numero.append(int(input('Valor para a posição {}: '.format(i))))
print('Você digitou os numeros {}'.format(numero))
print(max(numero))