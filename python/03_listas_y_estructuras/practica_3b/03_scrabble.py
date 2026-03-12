# Contar los puntos de una mano de Srabble con strings.


# Inicializar la lista con la mano de Scrabble.
palabras = ["A5", "B3", "C7", "D1", "E3", "F5", "G10", "H9"]


# Recorrer la lista y extraer el string con el número y convertirlo a Entero.
# Inicializar lista vacía con los puntos.
puntos = []

for ficha in palabras:
    puntos.append(int(ficha[1:]))

# Recorrer la lista de enteros y sumarlos.
sum_puntos = 0

for num in puntos:
    sum_puntos += num

print(f"""La suma de los puntos de la siguiente mano de Scrabble: {palabras}
      es: {sum_puntos}""")

