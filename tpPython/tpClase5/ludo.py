# el usuario ingresa el valor del dado manualmente
# gana cuando la suma de tiradas llega a 24 o mas

sumadorTiradas = 0
contadorTiradas = 0

# uso do-while con while True porque siempre tira al menos una vez
while True:
    valorDadoTirado = int(input("ingrese el valor del dado: "))

    # valido que el dado este entre 1 y 6
    if valorDadoTirado >= 1 and valorDadoTirado <= 6:
        sumadorTiradas = sumadorTiradas + valorDadoTirado
        contadorTiradas = contadorTiradas + 1
    else:
        print("valor invalido, ingrese un numero de entre 1 y 6")

    if sumadorTiradas >= 24:
        break  # gano, salgo del bucle

print("GANASTE!!!")
print("las veces que lanzo el dado fueron:", contadorTiradas)