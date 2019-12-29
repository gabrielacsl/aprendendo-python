idade = [1, 2, 3, 4, 5]
idade.append(18) #adicionado ao final da lista
idade.insert(2, 25) #posição, inserção 
idade.pop() #remove pelo indice, sem parametro, remove a ultima posição da lista
idade.remove(1) #remove pelo valor atribuido ao indice 
idade.sort() #ordena os elementos em forma crescente
idade.sort(reverse = True)
idade.reverse() #inverte os elementos 

print(idade)
print(max(idade)) # maior valor da lista
print(min(idade)) # menor valor da lista