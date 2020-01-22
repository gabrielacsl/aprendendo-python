arquivo = open('aulaPython.txt', 'w') # a para alterar / r para ler

texto = ''' 
Texto longo que não vou escrever e tambem nao vou colocar lorem ipsum

'''
arquivo.write(texto)

arquivo.close