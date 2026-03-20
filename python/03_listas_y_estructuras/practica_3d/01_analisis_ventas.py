# Crear un script que analice las ventas del último mes.
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120,
          170, 190, 250, 300, 95, 110, 140, 180, 200, 160, 120, 80, 170,
          150, 210, 190, 230, 250]

dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]

ventas_dia = [0, 0, 0, 0, 0, 0, 0]

for i in range(len(ventas)):
    ventas_dia[i % 7] += ventas[i]

for i in range(len(ventas_dia)):
    print(f"Día: {dias_semana[i]} = {ventas_dia[i]}")

print(f"El día con mayor número de ventas es: {dias_semana[ventas_dia.index(max(ventas_dia))]}")
