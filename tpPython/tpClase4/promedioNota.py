# calculo el promedio del curso con la nota y cantidad de alumnos de cada examen

cantExamenes = int(input("cuantos examenes hay?: "))

sumaTotal = 0
alumnosTotal = 0

for i in range(1, cantExamenes + 1):
    print("examen", i)
    nota = float(input("nota del examen: "))
    cantAlumnos = int(input("cantidad de alumnos que lo rindieron: "))

    # acumulo nota * alumnos para despues dividir bien el promedio
    sumaTotal = sumaTotal + (nota * cantAlumnos)
    alumnosTotal = alumnosTotal + cantAlumnos

promedio = sumaTotal / alumnosTotal
print("nota promedio del curso:", promedio)
