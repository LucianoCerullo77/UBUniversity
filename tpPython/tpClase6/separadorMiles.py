# recibo un numero como string y devuelvo el mismo con puntos de miles

def agregarPuntosMiles(numero):
    resultado = ""
    contador = 0

    # recorro de atras para adelante y agrego un punto cada 3 digitos, tambien se puede de la manera que hicimos con rama 
    for i in range(len(numero) - 1, -1, -1):
        if contador > 0 and contador % 3 == 0:
            resultado = "." + resultado
        resultado = numero[i] + resultado
        contador = contador + 1

    return resultado

numero = input("ingrese un numero entero: ")

print("con separador de miles:", agregarPuntosMiles(numero))
