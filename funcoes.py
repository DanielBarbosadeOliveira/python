def exibir_mensagem(nome):
    print(f"Olá {nome}")

#Podemos chamar a função assim: exibir_mensagem("Daniel") ou exibir_mensagem(nome="Daniel")

def exibir_mensagem_2(nome="Anônimo"):
    print(f"Olá {nome}")
#Caso não passe um parâmetro, tem uma valor default

def calcula_total(numeros):
    return sum(numeros)
#Retorna a soma dos números de uma lista

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero  - 1
    sucessor = numero + 1
    return antecessor, sucessor
#Retorna uma tupla

#Caso alguma função não explicite um return, de forma automática vai retornar None

def salvar_carro(marca, modelo, ano, placa):
    print(f"carro inserido com sucesso! {marca}| {modelo} |{ano} |{placa}")
    
salvar_carro("Volkswagem", "Jeta", 2025, "ABC1D56")
salvar_carro(marca="Volkswagem", modelo="Jeta", ano=2025, placa="ABC1D56")
salvar_carro(**{"marca": "Volkswagem", "modelo": "Jeta", "ano": 2025, "placa": "ABC1D56"})


def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
exibir_poema("31/08/2024", "Zen do python", "Bonito é melhor que feio", autor="Tim Peters", ano=1999)