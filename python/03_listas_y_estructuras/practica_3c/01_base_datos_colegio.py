# Seguimiento de las notas de un colegio con manejo de listas anidadas.

# Inicialización de las listas, alumnos y notas
alumnos = ["Arturo", "Jose", "Ana", "Perico", "Baldomero"]
notas = [[5, 4, 8], [10, 10, 0], [8, 6, 10], [0, 10, 5], [5, 2, 7]]


# Bucle para recorrer los alumnos y las notas.
media_clase = 0
for nombre in range(len(alumnos)):
    media_alumno = 0
    suma_notas = 0
    for nota in notas[nombre]:
        suma_notas += nota
    media_alumno = suma_notas / len(notas[nombre])
    media_clase += media_alumno
    print(f"Nota media de {alumnos[nombre]} es: {round(media_alumno, 2)}")


print(f"La media de la clase es: {round(media_clase / len(alumnos), 2)}")
