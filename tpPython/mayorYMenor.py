numero = int(input("ingrese un numero entero positivo (-1 para terminar): "))

# inicializo con el primer valor valido
menor = numero
mayor = numero

while numero != -1:
    if numero > 0:
        if numero < menor:
            menor = numero
        if numero > mayor:
            mayor = numero
    else:
        print("numero invalido, solo enteros positivos")

    numero = int(input("ingrese un numero entero positivo (-1 para terminar): "))

print("el menor es:", menor)
print("el mayor es:", mayor)