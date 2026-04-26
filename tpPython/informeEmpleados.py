n = int(input("cuantos empleados hay?: "))

# acumuladores e inicializaciones
totalSalarios = 0
cantGananMas200k = 0
cantCat3Menos50k = 0
legajoMayorSueldo = 0
sueldoMayor = 0
sueldoMenor = -1  # lo inicializo en -1 para detectar el primero
totalCat1 = 0
totalCat2 = 0
totalCat3 = 0

for i in range(1, n + 1):
    print("-- empleado", i, "--")
    legajo = int(input("legajo: "))
    categoria = int(input("categoria (1, 2 o 3): "))
    salario = float(input("salario: "))

    # acumulo el total de salarios
    totalSalarios = totalSalarios + salario

    # cuento los que ganan mas de 200000
    if salario > 200000:
        cantGananMas200k = cantGananMas200k + 1

    # cuento los de categoria 3 que ganan menos de 50000
    if categoria == 3 and salario < 50000:
        cantCat3Menos50k = cantCat3Menos50k + 1

    # guardo el legajo del que mas gana
    if salario > sueldoMayor:
        sueldoMayor = salario
        legajoMayorSueldo = legajo

    # guardo el sueldo mas bajo
    if sueldoMenor == -1 or salario < sueldoMenor:
        sueldoMenor = salario

    # acumulo por categoria
    if categoria == 1:
        totalCat1 = totalCat1 + salario
    elif categoria == 2:
        totalCat2 = totalCat2 + salario
    elif categoria == 3:
        totalCat3 = totalCat3 + salario

# calculo el promedio al final
promedio = totalSalarios / n

print("-- INFORME --")
print("total de salarios pagados:", totalSalarios)
print("empleados que ganan mas de $200000:", cantGananMas200k)
print("empleados cat3 que ganan menos de $50000:", cantCat3Menos50k)
print("legajo del que mas gana:", legajoMayorSueldo)
print("sueldo mas bajo:", sueldoMenor)
print("total salarios categoria 1:", totalCat1)
print("total salarios categoria 2:", totalCat2)
print("total salarios categoria 3:", totalCat3)
print("salario promedio:", promedio)