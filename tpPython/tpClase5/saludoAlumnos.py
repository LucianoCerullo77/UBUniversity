# pido nombres hasta que ingrese FIN
# cuento cuantos alumnos hay con un contador

contadorAlumnos = 0

nombreAlumno = input("para salir, escriba FIN entre comillas, sino ingrese el nombre del alumno: ")

while nombreAlumno != "FIN":
    print("Bienvenido", nombreAlumno)
    contadorAlumnos = contadorAlumnos + 1
    nombreAlumno = input("ingrese el nombre del alumno: ")

print("total de alumnos presentes:", contadorAlumnos)
