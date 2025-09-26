distancia_km = int(225000000)
# velocidad_kmh = [10000, 20000, 30000, 40000, 50000]


for velocidad in range (10000,50001,10000):
    tiempo_horas = distancia_km / velocidad
    tiempo_dias = tiempo_horas / 24
    print('Velocidad: ' , velocidad, 'km/h -> Tiempo:' , tiempo_dias, 'días.')

'''  
for i in range (10000,50001):
    tiempo_horas = distancia_km / i
    tiempo_dias = tiempo_horas / 24
    print('Velocidad: ' , i, 'km/h -> Tiempo:' , tiempo_dias, 'días.')
''' 