pessoa = {"nome": "Daniel", "idade": 25}

pessoa = dict(nome="Daniel", idade=25)

pessoa["telefone"] = "3333-1234"  #Acrescenta um elemento no dicionário

pessoa["nome"] #Retorna Daniel
pessoa["idade"] #Retorna 25

pessoa["nome"] = "Ester"
pessoa["idade"] = 6
pessoa["telefone"] = "123456789"

#Para acessar e alterar valores tem que colocar o nome da chave

#Dicionário aninhado
contatos = {
    "dan.dam@hotmail.com": {"nome": "Daniel", "telefone": "11111-1111"},
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "22222-2222"}
}

contatos["dan.dam@hotmail.com"]["nome"] #Daniel

for chave in contatos:
    print(chave, contatos[chave])
    
for chave, valor in contatos.items():
    print(chave, valor)
    

dict.fromkeys(["nome", "telefone"]) #{"nome": None, "telefone": None}
dict.fromkeys(["nome", "telefone"], "vazio") #{"nome": "vazio", "telefone": "vazio"}

#Se quando tentar chamar um elemento chamando a chave dessa forma: contatos["chave"], e a chave não existir, vai retornar um erro: KeyError e vai fazer o programa parar
contatos.get("chave") #Retorna None em  vez de KeyError e parar o programa
contatos.get("chave", {}) #Se não achar o valor da chave retorna um valor escolhido, nesse caso retorna um dicionário vazio: {}
contatos.get("dan.dam@hotmail.com", {}) # {"nome": "Daniel", "telefone": "11111-1111"}

print(contatos.items()) #Retorna uma lista de tuplas: dict_items([('dan.dam@hotmail.com', {'nome': 'Daniel', 'telefone': '11111-1111'}), ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '22222-2222'})])

contatos.keys() #Retorna uma lista de chaves: dict_keys(['dan.dam@hotmail.com', 'guilherme@gmail.com'])

contatos.pop("dan.dam@hotmail.com") #Remove E Retorna o valor removido.
contatos.pop("dan.dam@hotmail.com", "Não encontrado") #Caso não encontre a chave ele retorna o valor colocado no 2º argumento.

contatos.popitem() #Remove itens na sequencia, caso não tenha mais itens e seja usado, retornará um KeyError

contatos.setdefault("nome", "Guilherme") #Se o atributo não estiver no dicionário, ele adiciona com o valor informado, se o atributo existir no dicionário, retorna o
#valor que existe no dicionário e não altera ele
contatos.setdefault("idade", 28) #Adiciona a chave idade com o valor 28 e retorna o valor

contatos = {
    "dan.dam@hotmail.com": {"nome": "Daniel", "idade": 25}
}

contatos.update({"dan.dam@hotmail.com": {"nome": "Dan"}}) #Permite atualizar um dicionário, quando faz um update com uma chave que já existe, ele vai atualizar a chave,
#Em vez de ficar com a chave antiga que tinha mais chaves dentro, atualiza para um dicionário com uma chave só dentro do dicionário

contatos.update({"guilherme@gmail.com": {"nome": "Guilherme", "idade": 28, "telefone": "3322-8181"}}) #Fazer um update com um novo dicionário que tem chaves que não
#Existem no dicionário original, ele vai atualizar o dicionário original com o dicionário passado por parâmetro

contatos.values() #Retorna todos os valores dos dicionários das chaves, o contato.Keys retorna as chaves, e esse os valores

"dan.dam@hotmail.com" in contatos #Retorna True, verifica se uma chave está no dicionário

"nome" in contatos["dan.dam@hotmail.com"] #Retorna True se nome está dentro do dicionário interno

del contatos["dan.dam@hotmail.com"] ["nome"] #Vai deletar a chave "nome" e o seu valor
del contatos["guilherme@gmail.com"] #Vai deletar toda a chave "guilherme@gmail.com"

def contar_caracteres(string):
#TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}
    for letra in string:
        if letra not in contador:
            contador[letra]= 1
        else:
            contador[letra] = contador[letra] + 1
#TODO: Itere através de cada caractere na string string.
#TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)