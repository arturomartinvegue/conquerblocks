# Contar el número de apariciones en una lista.
lista = [23, 65, 23, 11, 65, 23, 7]


# Pedir al usuario que elija un número de la lista.
user_num = int(input(f"Elija un número de la siguiente lista: {lista} "))


# Recorrer la lista para saber el número de apariciones.
# Declarar la variable que hace el conteo de apariciones.
conteo = 0

for num in lista:
    if num == user_num:
        conteo += 1

# Devolver el resultado en pantalla.
print(f"El número de apariciones de {user_num} en la lista son: {conteo}")
