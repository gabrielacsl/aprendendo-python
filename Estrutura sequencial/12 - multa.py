peso = int(input('Kg: '))

if peso > 50:
    multa = (peso - 50) * 4.00
    print('Valor a ser pago de multa: R${:.2f}'.format(multa))
else:
    print('Quantidade não excendente.')