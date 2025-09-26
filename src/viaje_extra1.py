max_repostaje = 150000

distancia_km = int(input('Introduce la distancia total en km: '))

n_paradas = distancia_km // max_repostaje
paradas = n_paradas*max_repostaje

for i in range (max_repostaje, distancia_km+1, max_repostaje):
    print('Parada en el km', i)

print('Total de paradas para repostar:',n_paradas)
    