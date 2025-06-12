# Un programa que genere un numero aleatorio entre 1 y 100, y el usuario debe adivinarlo.
import random
def adivinar_numero():
    numero_aleatorio = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Bienvenido, elige un numero entre el 1 y 100 para comenzar.")

    while not adivinado:
        try:
            numero_usuario = int(input("Introduce tu número: "))
            intentos += 1

            if numero_usuario < 1 or numero_usuario > 100:
                print("Por favor, elige un número entre 1 y 100.")
                continue

            if numero_usuario < numero_aleatorio:
                print("Uuuuuyyyy muy abajo. Inténtalo de nuevo.")
            elif numero_usuario > numero_aleatorio:
                print("Ufffff te fuiste muy arriba. Inténtalo de nuevo.")
            else:
                adivinado = True
                print(f"Has adivinado el número {numero_aleatorio} en {intentos} intentos.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

if __name__ == "__main__":
    adivinar_numero()