# Extraer los elementos comunes de dos listas.
lista1 = [1, 4, 7, 3, 9, 2]
lista2 = [4, 6, 2, 8, 3, 5]

common_list = []

for i in lista1:
    for j in lista2:
        if i == j:
            common_list.append(i)

print(f"""Los elementos comunes entre:
      Lista 1: {lista1}
      Lista 2: {lista2}

      Son: {common_list}""")
