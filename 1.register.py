import time

Nombre1 = str('Cesarmanuel')
Nombre2 = str('Pepe123')
Nombre3 = str('Matiasdos')

input('Hola jugador para comenzar la partida ingrese su nombre :  ')
print('Lo siento ese nombre es muy comun...')
print('')
print('Eliga un nombre recomendado por nosotros (1), (2) o (3)')
print('1: ', Nombre1) 
print('2: ', Nombre2)
print('3: ', Nombre3)
print('')
Nombres = int(input('Seleccione un nombre: '))
print('')

def switch_case(Nombres):
    match Nombres:
        case 1:
            print('Elegiste como nombre: ', Nombre1)
            print('')
            print("................................ Cargando ................................")
            print('')
            print("Datos registrados, comencemos el juego... PLAY NOW!")
            print('')
        case 2: 
            print('Elegiste como nombre: ', Nombre2)
            print('')
            print("................................ Cargando ................................")
            print('')
            print("Datos registrados, comencemos el juego... PLAY NOW!")
            print('')
        case 3:
            print('Elegiste como nombre: ', Nombre3)
            print('')
            print("................................ Cargando ................................")
            print('')
            print("Datos registrados, comencemos el juego... PLAY NOW!")
            print('')
        case _:
            print('Opcion invalida')
switch_case(Nombres)