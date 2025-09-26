def dias (distancia, velocidad):
    tiempo_horas = distancia / velocidad
    tiempo_dias = tiempo_horas / 24
    print(f"Tardarías {tiempo_dias} días en llegar.")

control=0
while control == 0:

    distancia_km = int(input('Digame una distancia en km: '))  
    velocidad_kmh = int(input('Digame una velocidad en km/h: ')) 
    dias(distancia_km,velocidad_kmh)
    
    control_2 = 0

    while control_2 == 0:
        continuar = input("¿Quieres hacer otra simulación? (s/n) ")
        if continuar == 's':
            control = 0
            control_2 = 1
        elif continuar == 'n':
            control = 1
            control_2 = 1
        else:
            print('El caracter escrito no es s ni n')