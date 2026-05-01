# cuantos meses faltan para comprar algo ahorrando un % del salario

salario = float(input("salario mensual: "))
porcentajeAhorro = float(input("porcentaje que ahorra (ej: 10 para 10%): "))
precioProducto = float(input("precio del producto: "))

ahorroPorMes = (salario * porcentajeAhorro) / 100
mesesNecesarios = precioProducto / ahorroPorMes

print("meses necesarios para comprarlo:", mesesNecesarios)
