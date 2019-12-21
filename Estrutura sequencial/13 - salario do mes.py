valor = float(input('Salario/h: '))
horas = int(input('Horas trabalhadas: '))

SalarioBruto = valor * horas
inss = SalarioBruto * 0.08
renda = SalarioBruto * 0.11
sindicato = SalarioBruto * 0.05
SalarioLiquido = SalarioBruto - inss - renda - sindicato

print('Salario bruto: R${:.2f}'.format(SalarioBruto))
print('Salario liquido: R${:.2f}'.format(SalarioLiquido))
print('Valor pago ao INSS: R${:.2f}'.format(inss))
print('Valor pago de imposto de renda: R${:.2f}'.format(renda))
print('Valor pago ao sindicato: R${:.2f}'.format(sindicato))