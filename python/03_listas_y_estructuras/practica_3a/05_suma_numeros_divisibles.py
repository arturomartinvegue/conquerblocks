# Crear un script que dado un número, realice la suma de aquellos números que sean divisibles por dicho número
numero = int(input("Introduzca un número: "))


# Bucle donde el rango máximo es el número introducido por el usuario +1.
# Inicializar la variable antes del Bucle
suma_total = 0

for i in range(1,numero + 1):
    if numero % i == 0:
        suma_total += i 


# Mostrar resultado en pantalla
print(f"La suma de los números divisibles de {numero} es: {suma_total}")

