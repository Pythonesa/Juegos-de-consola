'''
    Un juego que elige un número random del 1 al 100,
    le pide al usuario que lo adivine,
    dándole como pistas de si el número a adivinar es mayor o menor al ingresado.
'''

import random

def get_numero_aleatorio():
    return random.randint(1,100)

def print_pista(numero_secreto, numero_ingresado):
    if numero_ingresado < numero_secreto:
        print("El número que buscas es mayor.")
    else:
        print("El número que buscas es menor.")

def jugar():
    numero_secreto = get_numero_aleatorio()
    intentos = 1
    print("Deberás adivinar un número entre 1 y 100.")
    while True:
        try:
            numero_ingresado = int(input("Ingresa un número: "))
            if numero_ingresado not in range(1,101):
                raise(ValueError)
            elif numero_ingresado == numero_secreto:
                print(f'¡Felicidades adivinaste el número {numero_secreto} en {intentos} intentos!')
                break
            else:
                print_pista(numero_secreto, numero_ingresado)
                intentos += 1
        except ValueError as ve:
            print("Debes ingresar un número entre 1 y 100. Intenta de nuevo.")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    jugar()