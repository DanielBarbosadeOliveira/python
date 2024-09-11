set([1, 2, 3, 1, 3, 4]) #[1, 2, 3, 4]

set("abacaxi") # ["b", "a", "c", "x", "i"]

set(("palio", "gol", "celta", "palio")) #{"palio", "gol", "celta"}

numeros = {0, 1, 2, 3, 4}
lista = list(numeros)
print(lista[0])

#Conjunto não aceita indexação, porém da para iterar dentro de um for

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)
    
#Dá para usar enumerate com conjunto

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b)  #{1, 2, 3, 4}

conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

conjunto_c.intersection(conjunto_d) #{2, 3}
conjunto_c.difference(conjunto_d) #{1}
conjunto_d.difference(conjunto_c) #{4}
conjunto_c.symmetric_difference(conjunto_d) #{1, 4}

conjunto_e = {1, 2 , 3}
conjunto_f = {4, 1, 2, 5, 6, 3}

conjunto_e.issubset(conjunto_f) #True
conjunto_f.issubset(conjunto_e) #False

conjunto_e.issuperset(conjunto_f) #False
conjunto_f.issuperset(conjunto_e) #True

conjunto_g = {1, 2, 3, 4, 5}
conjunto_h = {6, 7, 8, 9}
conjunto_i = {0, 1}

conjunto_g.isdisjoint(conjunto_h) #True
conjunto_g.isdisjoint(conjunto_i) #False

sorteio = {1, 23}
sorteio.add(25)
sorteio.add(42)
sorteio.add(23) #Não vai adicionar pois já tem o número no conjunto.

sorteio.clear() #Limpa o conjunto

sorteio.copy() #Copia o conjunto, só colocar em uma variável

sorteio.discard(1) #Discarta o elemento, caso o elemento passado não tenha no conjunto, nada ocorre

sorteio.pop() #Remove os elemos da esquerda para a direita, first in first out

sorteio.remove(23) #Remove o elemento igual o discard, porém se colocar um elemento que não tem no conjunto, ele dá erro.

25 in sorteio #True
1 in sorteio #False


def elementos_comuns(set1, set2):
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))  

    return list(set1.intersection(set2))

# Leitura das listas
lista1 = input().split()
lista2 = input().split()

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")