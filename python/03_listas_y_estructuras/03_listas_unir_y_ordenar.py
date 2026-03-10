# Unión de dos listas y ordenarlas de forma ascendente
lista_uno = [1, 2, 4, 6, 7, 10, 15, 11, 5]
lista_dos = [3, 5, 6, 2, 1, 0, 12, 9, 8]

print(f"""Unión de dos listas: 
      lista_uno: {lista_uno}
      lista_dos: {lista_dos}""")


# Suma de las dos listas en una lista nueva
lista_tres = lista_uno + lista_dos
print(f"""Lista resultante de las dos anteriores:
      lista_tres = {lista_tres}""")


# Ordenar la lista de forma ascendente
print(f"""Lista ordenada de forma ascendente:
      lista_tres = {sorted(lista_tres)}""")
