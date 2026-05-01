# calculo el nuevo limite segun el tipo de tarjeta

limiteActual = float(input("limite actual de la tarjeta: "))
tipo = int(input("tipo de tarjeta (1, 2 o 3): "))

if tipo == 1:
    aumento = (limiteActual * 25) / 100
elif tipo == 2:
    aumento = (limiteActual * 35) / 100
elif tipo == 3:
    aumento = (limiteActual * 40) / 100
else:
    # cualquier otro tipo tiene 50%
    aumento = (limiteActual * 50) / 100

nuevoLimite = limiteActual + aumento
print("nuevo limite:", nuevoLimite)
