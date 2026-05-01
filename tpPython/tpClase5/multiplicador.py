multiplo = int(input("ingrese un numero entero: "))

sumaTotal = 0

for i in range(1, 13):
    resultado = multiplo * i
    sumaTotal = sumaTotal + resultado
    print(multiplo, "x", i, "=", resultado)

# muestro la suma de los 12 resultados
print("suma de los 12 numeros:", sumaTotal)