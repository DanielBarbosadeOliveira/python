#Parâmetros Especiais

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    #Antes da barra (/) é obrigatório passar os parâmetros por posição, após a barra pode ser por posição ou nomeado.
    
criar_carro("Palio", 1999, "ABC1D23", "Fiat", "1.0", "Gasolina") #Válido
#criar_carro(modelo="Palio", ano=1999, placa="ABC1D23", marca="Fiat", motor="1.0", combustivel="Gasolina") #Inválido, pois só a marca, motor e combistível poderia ser passado nomeado

def criar_carro_2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    #Nesse caso, todos os parâmetros precisam ser passados por nome, tem que passar chave valor
    
criar_carro_2(modelo="Palio", ano=1999, placa="ABC1D23", marca="Fiat", motor="1.0", combustivel="Gasolina")#Válido
#criar_carro("Palio", 1999, "ABC1D23", "Fiat", "1.0", "Gasolina") #Inválido, pois precisa passar nomeado.

#Hibrido desses 2 de cima

def criar_carro_3(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_3("Palio", 1999, "ABC1D23",  marca="Fiat", motor="1.0", combustivel="Gasolina")#Válido

#Dá para fazer um negócio legal, escolher parametros a serem passados da forma que quiser

def criar_carro_4(modelo, ano, placa, /, marca, * , motor, combustivel): #A marca pode ser passada por posição e por nomeação
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro_4("Palio", 1999, "ABC1D23",  marca="Fiat", motor="1.0", combustivel="Gasolina")#Válido
criar_carro_4("Palio", 1999, "ABC1D23",  "Fiat", motor="1.0", combustivel="Gasolina")#Válido

#Funções são ojetos de primeira classe, é um objeto que pode ser passado por parametro para argumento de uma função, pode ser retornado por uma função e também
#Pode ser atribuido a ua variável

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da soma de {a} + {b} é {resultado}")
    
exibir_resultado(10, 10, somar)


op = somar
print(op(2, 4)) #Retorna 6, é possivel atribuir uma função dentro de uma variável