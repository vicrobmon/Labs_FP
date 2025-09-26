edad = int(input('Digame su edad: '))
nivel_fisico = int(input('Digame su nivel físico (en un rango de 1 a 10): '))

if 0 < nivel_fisico < 11:
    if edad > 18:
        if nivel_fisico > 5:
            print('¡Listo para despegar!')
        else:
            print("Debes estar en mejor forma.")
    else:
        print('Debes ser mayor de edad')
else:
    print('El valor del nivel físico está fuera de rango.')