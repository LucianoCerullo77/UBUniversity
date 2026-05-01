cantMenores = 0
cantAdultos = 0
sumaEdadesMenores = 0
sumaEdadesAdultos = 0

edad = int(input("ingrese una edad (-1 para terminar): "))

while edad != -1:
    # solo proceso edades validas entre 0 y 100
    if edad >= 0 and edad <= 100:
        if edad < 18:
            cantMenores = cantMenores + 1
            sumaEdadesMenores = sumaEdadesMenores + edad
        else:
            cantAdultos = cantAdultos + 1
            sumaEdadesAdultos = sumaEdadesAdultos + edad
    else:
        print("edad invalida, se descarta")

    edad = int(input("ingrese una edad (-1 para terminar): "))

print("menores de 18:", cantMenores)
print("de 18 o mas:", cantAdultos)

# solo muestro el promedio si hay al menos uno en el grupo
if cantMenores > 0:
    promMenores = sumaEdadesMenores / cantMenores
    print("promedio menores:", promMenores)

if cantAdultos > 0:
    promAdultos = sumaEdadesAdultos / cantAdultos
    print("promedio adultos:", promAdultos)