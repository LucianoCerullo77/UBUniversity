# venta de boletos, si pide 5 o mas no se puede

precio = float(input("precio del boleto: "))
cantidad = int(input("cantidad de boletos: "))

# si pide 5 o mas no se puede por cupo limitado
if cantidad >= 5:
    print("error: cupo limitado, no se puede realizar la venta")
else:
    total = precio * cantidad
    print("total a pagar:", total)
