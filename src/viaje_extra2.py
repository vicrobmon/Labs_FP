print('Ejercicio 1')
distancia_km = 384400  # distancia Tierra - Luna
velocidad_kmh = 5000
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
if tiempo_dias >= 7:
    tiempo_semanas = tiempo_dias//7
    dias_restantes = tiempo_dias%7
    print(f"Tardarías {tiempo_semanas} semanas en llegar.")