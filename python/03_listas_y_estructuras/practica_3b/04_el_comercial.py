# Lista de productos y precios
lista_precios = [30.0, 9.8, 42.5, 32.6, 71.5, 44.0, 21.2, 53.2, 25.3, 57.8]
user_input = []
for i in range(0, len(lista_precios)):
    user_input.append(int(input(f"¿Cuántas unidades del producto {i + 1} se han vendido? ")))


# Inicializo variables antes de entrar al bucle.
total_ventas = 0 
dinero_total = 0 
dinero_facturado_producto = []


# Recorro con un bucle que recorre un índice de cada lista para realizar las operaciones
for j in range(0, len(user_input)):
    total_ventas += user_input[j]
    dinero_total += user_input[j] * lista_precios[j]
    dinero_facturado_producto.append(user_input[j] * lista_precios[j])


# Imprimo los resultados en pantalla.
for i in range(0, len(dinero_facturado_producto)):
    print(f"\nSe ha facturado del Producto {i + 1}: {dinero_facturado_producto[i]}")

print(f"El número total de ventas es: {total_ventas}")
print(f"El dinero total ganado por las ventas es: {dinero_total}")
