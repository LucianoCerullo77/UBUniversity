import math

def calcularRaiz(a,b,c):
    discriminante = (b ** 2) - (4 * a * c)

    if discriminante < 0:
        ## aca habia que poner none, sino recibia mas de un valor, es medio raro, tuve que verlo con IA para corregirlo
        ## codigo anterior todo igual pero acá había un:
        ## return "el discriminante no puede ser 0"
        ## despues de este cambio el codigo funciono bien!
        return None, None
    
    primerRaiz = (-b + math.sqrt(discriminante)) / (2 * a)
    segundaRaiz = (-b - math.sqrt(discriminante)) / (2 * a)

    return primerRaiz, segundaRaiz

a = float(input("ingrese a: "))
b = float(input("ingrese b: "))
c = float(input("ingrese c: "))

raizUsuario1,raizUsuario2 = calcularRaiz(a, b, c)

if raizUsuario1 is None:
    print("raices imaginarias")
else:
    print(f"raiz 1:  {raizUsuario1:.2f}")
    print(f"raiz 2: {raizUsuario2:.2f}")