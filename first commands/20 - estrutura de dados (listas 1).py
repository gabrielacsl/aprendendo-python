x = list(range(1, 101))

print(x)

numero = int(input('Numero para apagar: '))

if numero in x:
    x.remove(numero)
    print('Numero removido com sucesso.')
print(x)

y = [['Gabriela', 20], ['Lucas', 20], ['Barbara', 31]]
print(y[0])
print(y[1][1])
