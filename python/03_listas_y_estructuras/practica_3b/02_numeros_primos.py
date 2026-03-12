# Dada una lista de números enteros, escribir un script que devuelva una nueva lista
# con los números primos de la lista original. Además, debe devolver el número total de números
# primos encontrados y la suma de ellos.


# Crear la lista de números enteros.
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]


# Recorrer la lista para encontrar los números primos.
lista_primos = []
for num in num_list:
    numero_primo = True
    if num == 1:
        continue
    for i in range(2, (num - 1)):
        if num % i == 0:
            numero_primo = False
    if numero_primo == True:
        lista_primos.append(num)

# Recorrer lista de números primos para sumarla.
sum_total = 0

for num in lista_primos:
    sum_total += num


# Imprimir resultados en pantalla.
print(f"""De la siguiente lista numérica: {num_list}
      Se han encontrado los siguientes números primos: {lista_primos}
      El número de primos encontrados es: {len(lista_primos)}
      Y la suma total de los primos es: {sum_total}""")
