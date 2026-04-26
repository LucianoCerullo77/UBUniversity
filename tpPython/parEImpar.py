n = int(input("ingrese un numero entero mayor a cero: "))

# rechazo valores invalidos
while n <= 0:
    print("valor invalido, tiene que ser mayor a cero")
    n = int(input("ingrese un numero entero mayor s cero: "))

factorial = 1

# multiplico de 1 hasta n
for i in range(1, n + 1):
    factorial = factorial * i

print("el factorial de", n, "es:", factorial)