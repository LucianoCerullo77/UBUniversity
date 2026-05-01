## aca me tuve que apoyar en la IA porque era demasiado complejo, tambien esta formateado por la IA

vocales = "aeiouAEIOU"

def esConsonante(caracter):
    # solo considero letras consonantes, no espacios ni puntuacion
    return caracter.isalpha() and caracter not in vocales

def fase1(mensaje):
    # se identifican grupos de consonantes y los invierto
    resultado = list(mensaje)
    i = 0

    while i < len(mensaje):
        if esConsonante(mensaje[i]):
            # encontre el inicio de un grupo
            inicio = i
            while i < len(mensaje) and esConsonante(mensaje[i]):
                i = i + 1
            fin = i - 1

            # invierto el grupo dentro de resultado
            izq = inicio
            der = fin
            while izq < der:
                resultado[izq], resultado[der] = resultado[der], resultado[izq]
                izq = izq + 1
                der = der - 1
        else:
            i = i + 1

    return "".join(resultado)

def fase2(mensaje):
    # tomo letras alternando desde el principio y desde el final
    resultado = ""
    izq = 0
    der = len(mensaje) - 1

    while izq <= der:
        resultado = resultado + mensaje[izq]
        izq = izq + 1
        if izq <= der:
            resultado = resultado + mensaje[der]
            der = der - 1

    return resultado

def desencriptarFase2(mensaje):
    # invierto la fase 2: separo las letras en dos mitades
    # las de indice par van a la izquierda, las de indice impar van a la derecha (al reves)
    izquierda = ""
    derecha = ""

    for i in range(len(mensaje)):
        if i % 2 == 0:
            izquierda = izquierda + mensaje[i]
        else:
            derecha = mensaje[i] + derecha  # agrego al principio para invertir

    return izquierda + derecha

def desencriptarFase1(mensaje):
    # fase 1 es su propio inverso, aplicarla de nuevo la revierte
    return fase1(mensaje)

# --- encriptacion ---
mensajeOriginal = input("ingrese el mensaje a encriptar: ")

resultadoFase1 = fase1(mensajeOriginal)
resultadoFase2 = fase2(resultadoFase1)

print(f"fase 1: {resultadoFase1}")
print(f"encriptado final (fase 2): {resultadoFase2}")

# --- desencriptacion ---
print()
mensajeEncriptado = input("ingrese el mensaje encriptado para desencriptar: ")

desencFase2 = desencriptarFase2(mensajeEncriptado)
desencFase1 = desencriptarFase1(desencFase2)

print(f"tras desencriptar fase 2: {desencFase2}")
print(f"mensaje original: {desencFase1}")
