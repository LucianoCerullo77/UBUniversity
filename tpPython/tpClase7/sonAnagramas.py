# funcion que determina si dos palabras son anagramas
# dos palabras son anagramas si tienen las mismas letras en distinto orden

def sonAnagramas(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()

    # si tienen distinta longitud no pueden ser anagramas
    if len(p1) != len(p2):
        return False

    # convierto p2 en lista para poder tachar letras ya usadas
    letrasP2 = list(p2)

    for letra in p1:
        encontrada = False

        # busco la letra manualmente sin usar in ni count
        for i in range(len(letrasP2)):
            if letrasP2[i] == letra:
                letrasP2[i] = None  # la marco como usada para no contarla dos veces
                encontrada = True
                break

        if not encontrada:
            return False

    return True

# programa principal
p1 = input("ingrese la primera palabra: ")
p2 = input("ingrese la segunda palabra: ")

if sonAnagramas(p1, p2):
    print(f"'{p1}' y '{p2}' son anagramas")
else:
    print(f"'{p1}' y '{p2}' NO son anagramas")
