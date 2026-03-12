# Creación de una lista numérica
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Lista de números pares a partir de la lista "numeros"
even_list = numeros[-1::-2]


# Bucle que imprime los cuadrados de la lista "numeros"
for num in numeros:
    print(f"El cuadrado del número {num} es: {num ** 2}")


# Paso 2 y 3 con el método de comprensión
even_list = [n for n in numeros [::-1] if n % 2 == 0]
[print(f"Cuadrado de {n}: {n**2}") for n in numeros]


# Imprimir el numero mas alto y mas bajo de la lista "even_list"
print(f"Mayor: {max(even_list)}")
print(f"Menos: {min(even_list)}")


# Sumar todos los elementos de la lista "even_list" con y sin bucle 
sum_total_uno = sum(even_list)

sum_total_dos = 0

for i in even_list:
    sum_total_dos += i
    print(f"La suma los valores es: {sum_total_dos}")


# Encontrar el índice correspondiente al número 8 en la lista "numeros" y en la lista de pares
for num in range(len(numeros)):
    if numeros[num] == 8:
        print(f"Indice correspondiente para el número 8 es: {num}")

for num in range(len(even_list)):
    if even_list[num] == 8:
        print(f"Indice correspondiente para el número 8 en la lista de numeros par es: {num}")
