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