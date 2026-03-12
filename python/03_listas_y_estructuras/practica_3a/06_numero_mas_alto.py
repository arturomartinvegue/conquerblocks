# Dado un número y dada una lista, encontrar el número más alto que es inferior al número dado.


# Pedir un número al usuario
user_num = int(input("Introduzca un número: "))
num_list = [1, 4, 6, 7, 8, 10, 15, 29, 25, 23, 32, 50, 75, 65]

# Usaré bucle for para determinar el número más alto.
# Inicializar variable dónde se almacenará el número.
higher_num = float("-inf")

for num in num_list:
    if num < user_num:
        if num > higher_num:
            higher_num = num

print(f"El número mas alto anterior a {user_num} es: {higher_num}")
    
