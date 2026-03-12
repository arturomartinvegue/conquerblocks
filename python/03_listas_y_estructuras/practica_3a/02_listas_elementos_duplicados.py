# Borrar elementos duplicados de listas
lista_compra = ["leche", "tomates", "huevos", "leche", "sal", "agua", "vinagre", "aceite", "sal", "huevos", "lechuga", "tomates", "pescado"]
unicos = []
duplicados = []

for elemento in lista_compra:
    if elemento not in unicos:
        unicos.append(elemento)
    else:
        duplicados.append(elemento)

print(f"La lista de la compra final sin duplicados es: {unicos}")


# Borrado de duplicados en lista original
for elemento in duplicados:
    if elemento in lista_compra:
        lista_compra.remove(elemento)

print(f"Resultado de lista_compra es: {lista_compra}")

# Nota: El borrado iterando la lista es complejo en python. Desordena los elementos al borrar en orden de aparición empezando
# por el índice 0 con el método .remove().
