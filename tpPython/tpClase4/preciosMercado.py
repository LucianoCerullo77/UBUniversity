# pido precios uno por uno hasta que ingrese 0
# el cliente siempre compra al menos uno, uso do-while con while True

totalCompra = 0
cantProductos = 0

# como python no tiene do-while lo simulo con while True y break
while True:
    precio = float(input("ingrese precio del producto (0 para terminar): "))

    if precio == 0:
        break  # salgo del bucle cuando ingresa 0

    totalCompra = totalCompra + precio
    cantProductos = cantProductos + 1

print("total de la compra:", totalCompra)
print("cantidad de productos:", cantProductos)
