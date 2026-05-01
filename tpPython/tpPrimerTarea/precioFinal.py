# calculo del precio final con descuento del 20% y luego IVA del 21%

precioOriginal = float(input("precio del articulo: "))

# primero aplico el descuento
descuento = (precioOriginal * 20) / 100
precioConDescuento = precioOriginal - descuento

# despues le sumo el IVA sobre el precio ya descontado
iva = (precioConDescuento * 21) / 100
totalFinal = precioConDescuento + iva

print("precio con descuento:", precioConDescuento)
print("precio final con IVA:", totalFinal)
