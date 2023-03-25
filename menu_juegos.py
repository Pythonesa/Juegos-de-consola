import adivina_el_numero
import ahorcado

def print_menu():
    print('Estas son las opciones de juegos para ti:')
    print('1 - Adivina el número.')
    print('2 - Ahorcado.')
    print('Para salir presiona q')

def print_fin_juego():
    print('Tu juego ha terminado.')

def init():
    print('¡Bienvenid@ a la colección de juegos de consola!')
    while True:
        print_menu()
        opcion = input('Ingresa el número del juego que deseas jugar: ')
        match opcion:
            case '1':
                adivina_el_numero.jugar()
                print_fin_juego()
            case '2':
                ahorcado.jugar()
                print_fin_juego()
            case 'q' | 'Q':
                break
            case _:
                print('Debes ingresar el número que aparece delante del juego que quieras jugar, lo que has ingresado no es un valor válido.')

if __name__ == '__main__':
    init()
