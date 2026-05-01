# version repetitiva del ejercicio de vuelto
# termina cuando el precio del producto es 0

precioProd = float(input("precio del producto (0 para salir): "))

while precioProd != 0:
    montoAbonado = float(input("monto abonado: "))

    if montoAbonado < precioProd:
        print("monto insuficiente")
    else:
        vuelto = montoAbonado - precioProd
        print("vuelto:", vuelto)

    # pido el siguiente producto
    precioProd = float(input("precio del producto (0 para salir): "))

print("fin del programa")
