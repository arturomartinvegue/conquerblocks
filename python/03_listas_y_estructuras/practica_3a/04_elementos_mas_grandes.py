numeros = [3, 7, 2, 9, 1, 6]

limite = int(input("Introduce un número: "))

contador = 0
for num in numeros:
    if num > limite:
        contador += 1

print(f"Hay {contador} elementos mayores que {limite}")
