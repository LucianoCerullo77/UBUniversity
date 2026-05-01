def vocalesEnMayuscula(frase):
    vocales = "aeiou"
    resultado = ""

    for caracter in frase:
        # si es vocal la pongo en mayuscula, sino la dejo igual
        if caracter.lower() in vocales:
            resultado = resultado + caracter.upper()
        else:
            resultado = resultado + caracter

    return resultado

# programa principal
texto = input("ingrese una frase: ")
resultado = vocalesEnMayuscula(texto)
print(resultado)
