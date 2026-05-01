# si el importe abonado no alcanza aviso, si alcanza doy el vuelto

precioProd = float(input("precio del producto: "))
montoAbonado = float(input("monto abonado: "))

if montoAbonado < precioProd:
    print("monto insuficiente")
else:
    vuelto = montoAbonado - precioProd
    print("vuelto:", vuelto)
