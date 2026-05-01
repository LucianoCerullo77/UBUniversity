# funcion que determina si las letras de una palabra estan en orden alfabetico
# ej: "amor", "chino", "himno" son palabras alfabeticas

def esAlfabetica(palabra):
    palabra = palabra.lower()

    # recorro desde la segunda letra y comparo con la anterior
    for i in range(1, len(palabra)):
        if palabra[i] < palabra[i - 1]:
            return False  # encontre una letra fuera de orden

    return True

# programa principal
palabra = input("ingrese una palabra: ")

if esAlfabetica(palabra):
    print(f"'{palabra}' es una palabra alfabetica")
else:
    print(f"'{palabra}' NO es una palabra alfabetica")
