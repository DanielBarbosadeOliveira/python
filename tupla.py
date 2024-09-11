#Tupla é imutável

frutas = ("laranja", "maça", "melancia",)
letras = tuple("python")
numeros = tuple([1, 3, 5, 6])
pais = ("Brasil",)

tupla = ("p", "y", "t", "h", "o", "h", )
tupla[2:]
tupla[:2]
tupla[1:2]
#etc..

#Metodos
tupla.count("p") #Retorna quantas vezes aparece o elemento

tupla.index("p") #Retorna a primeira vez que aparece o elemento

len(tupla) #Retorna tamanho da tupla.

carros = ("gol")
print(isinstance(carros, tuple))

def soma_tupla(tupla):
    return sum(tupla)


if __name__ == "__main__":
    entrada = input()

    elementos = tuple(map(int, entrada.split()))
    
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")