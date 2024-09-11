#List Comprehetion
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)


quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

#Metodos tipo lista:
lista = []
lista.append(1)
lista.append("Olá")
lista.append([1, 3, 4])

lista.copy() #Cria uma cópia da lista, só colocar em alguma outra variável

lista.count(1) #Conta quantas vezes um determinado objeto aparece na lista

lista.extend([3 , "salve Brasil"]) #Acrescenta os itens da lista colocada no parametro, no final da lista original
print(lista)

lista.index(1) #Passa a posição da primeira ocorrencia do item colocado no parâmetro

lista.pop() #Exclui o último elemento, pois na lista sem parametro funciona assim: first in first out
lista.pop(0) #Coloca o índice do item que quer excluir

lista.remove("Olá") #Passa objeto para remover a primeira ocorrencia daquele objeto

lista.reverse() #Espelha a lista

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.sort() #Ordena uma lista, tanto faz se for numérica ou alfabética
linguagens.sort(reverse=True) #Ordena a lista de trás para frente
linguagens.sort(key=lambda x:len(x)) #Ordena a lista por tamanho da palavra
linguagens.sort(key=lambda x: len(x), reverse=True) #Ordena a lista por tamanho da palabra de trás para frente
#O sort começa da esquerda para a direita, então na questão acima, o python fica na frente do csharp sempre, no caso da 3º e 4º função.

len(linguagens) #Retorna a quantidade de itens em uma lista

sorted(linguagens) #Igual com sort 
sorted(linguagens, key=lambda x: len(x)) #Mesma coisa de fazer com o sort
sorted(linguagens, key=lambda x: len(x), reverse=True) #Mesma coisa de fazer com o sort



lista.clear() #Limpar lista 
