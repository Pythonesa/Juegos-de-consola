'''
    Juego donde el usuario deberá adivinar una palabra aleatoria 
    e irá recibiendo pistas con letras en colores para aquellas que esten 
    en el lugar correcto(verde) o existan en la palabra pero esten en otro lugar(amarillo).
'''

import random

def get_palabra():
    palabras = ['salsa', 'perro', 'lucha', 'playa', 'cebra', 'tabla', 'queso', 'nieve', 'nubes', 'cabra', 'elevo', 'fresa', 
                'garra', 'hojas', 'madre', 'olivo', 'quema', 'ruido', 'unico', 'vacas', 'yegua', 'zarza', 'bicho', 'clima', 
                'duelo', 'falda', 'grito', 'herir', 'jefes', 'kilos', 'locos', 'manos', 'noche', 'osito', 'plaza', 'roble', 
                'sable', 'tigre', 'verde', 'zanja', 'abuso', 'bruto', 'causa', 'dardo', 'focas', 'helio', 'iluso', 'jaula', 
                'kendo', 'limbo']
    return random.choice(palabras)

def get_seguir_jugando():
    seguir = 's'
    seguir = input("Quieres seguir jugando? [s/n]")
    if seguir == 'n' or seguir == 'N':
        return 'n'
    else:
        return 's'

def get_palabra_mostrada(palabra_secreta , palabra_ingresada):
    palabra_mostrada = []
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == palabra_ingresada[i]:
            palabra_mostrada.append(f'\033[32m {palabra_ingresada[i]} \033[0m')
        elif palabra_ingresada[i] in palabra_secreta:
            palabra_mostrada.append(f'\033[33m {palabra_ingresada[i]} \033[0m')
        else:
            palabra_mostrada.append(f'\033[31m {palabra_ingresada[i]} \033[0m')
    return palabra_mostrada


def jugar():
    seguir = 's'
    while True:
        palabra_secreta = get_palabra()
        intentos = 0

        print('Deberás adivinar una palabra de 5 letras.')

        while True:
            try:
                palabra_ingresada = input("Ingresa tu palabra de 5 letras: ").lower()
                if len(palabra_ingresada) < 5 or len(palabra_ingresada) > 5:
                    raise(Exception('Debes ingresar una palabra de 5 letras, la que ingresaste no es válida intenta de nuevo.'))
                elif palabra_ingresada == palabra_secreta:
                    print(f'\033[32m¡Felicitaciones! Adivinaste la palabra {palabra_secreta} en {intentos} intentos.\033[0m')
                    seguir = get_seguir_jugando()
                    if seguir == 'n':
                        break
                else:
                    print(' '.join(get_palabra_mostrada(palabra_secreta,palabra_ingresada)))
                    intentos += 1
            except Exception as e:
                print(e)
        if seguir == 'n':
            break

if __name__ == '__main__':
    jugar()