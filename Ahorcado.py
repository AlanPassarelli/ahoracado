# Reglas del Juego:
# El juego se juega con dos participantes: uno selecciona una palabra y el otro adivina las letras.ok
# La palabra seleccionada debe estar oculta para el adivinador, representada inicialmente por guiones bajos o guiones. ok
# El adivinador intenta adivinar las letras de la palabra una por una.ok
# Se permite un cierto número de intentos incorrectos antes de que termine el juego.ok
# Interfaz de Usuario:
# Mostrar el estado actual de la palabra, mostrando las letras adivinadas y guiones para las letras restantes.ok
# Mostrar el número de intentos incorrectos permitidos y el número de intentos incorrectos realizados hasta el momento.ok
# Proporcionar una forma para que el usuario ingrese sus intentos (típicamente una letra a la vez).ok
# Ingreso de Palabra:
# Implementar un mecanismo que permita que uno de los participantes ingrese una palabra para que sea adivinada por el otro.ok
# Validar la entrada para asegurarse de que la palabra ingresada sea válida (por ejemplo, solo letras y sin espacios).ok
# Proporcionar la opción de que la palabra sea seleccionada aleatoriamente de una lista predefinida si no se ingresa manualmente.ok
# Progreso del Juego:
# Seguir el progreso del juego, incluyendo las letras adivinadas y los intentos incorrectos.ok
# Actualizar la pantalla después de cada intento para reflejar los cambios en la palabra y el número de intentos incorrectos.ok
# Condiciones de Fin del Juego:
# Definir las condiciones para ganar y perder el juego.ok
# El juego se gana si el adivinador adivina correctamente todas las letras de la palabra antes de exceder los intentos incorrectos permitidos.ok
# El juego se pierde si el adivinador excede los intentos incorrectos permitidos.ok
# Retroalimentación:
# Proporcionar retroalimentación al usuario después de cada intento, indicando si la suposición fue correcta o incorrecta.ok
# Mostrar un mensaje cuando se gana o pierde el juego.ok
# Rejugabilidad:
# Permitir que el usuario juegue el juego varias veces sin reiniciar el programa.preguntar.ok
# Después de que termine un juego, preguntar al usuario si desea jugar de nuevo.ok
# Manejo de Errores:
# Implementar manejo de errores para entradas inválidas (por ejemplo, caracteres no alfabéticos, suposiciones repetidas).ok
import random
import string


import random
import string

# Selección de palabra
def eleccion_de_palabra(lista_de_palabra):
    while True:
        respuesta = input("¿Desea elegir una palabra para que su rival adivine? (Si/No): ")

        if respuesta.lower() == "si":
            palabra_elegida = input("Escribe la palabra: ")
            return palabra_elegida.lower()  # Convertir la palabra a minúsculas
        elif respuesta.lower() == "no":
            return random.choice(lista_de_palabra)
        else:
            print("Respuesta no válida. Por favor, responde 'Si' o 'No'.")

# Ayuda al usuario
def ayuda_al_usuario():
    while True:
        ayuda = input("¿Necesitas ayuda? (Si/No): ")
        if ayuda.lower() == "si":
            pista = input("Darle pista al usuario: ")
            return pista
        elif ayuda.lower() == "no":
            return None
        else:
            print("Respuesta no válida. Por favor, responde 'Si' o 'No'.")

# Tablero de juego
def adivinar_palabra(palabra_secreta, letras_adivinadas, intentos_restantes):
    palabra = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:  # Convertir la letra a minúsculas
            palabra += letra
        else:
            palabra += "-"
    print(palabra)
    print(f"Intentos restantes: {intentos_restantes}")
    print("Intentos permitidos: 5")
    ayuda_al_usuario()

# Continuar jugando
def seguir_jugando():
    continuar_juego = input("¿Quieres seguir jugando? (Si/No): ")
    if continuar_juego.lower() == "si":
        jugar_ahorcado()
    elif continuar_juego.lower() == "no":
        print("Gracias por jugar al juego del ahorcado")
    else:
        print("Respuesta no válida. Por favor, responde 'Si' o 'No'.")

# Lógica de juego
def jugar_ahorcado():
    lista_de_palabra = ["programador", "aprendiendo", "juego", "python", "react", "javascript"]
    palabra_secreta = eleccion_de_palabra(lista_de_palabra)
    if palabra_secreta is None:
        return

    letra_adivinadas = []
    intentos_restantes = 5

    print("Bienvenido al juego del ahorcado")
    print("La palabra a adivinar es: ")

    while intentos_restantes > 0:
        adivinar_palabra(palabra_secreta, letra_adivinadas, intentos_restantes)
        letra = input("Introduce una letra: ").lower()

        if letra in letra_adivinadas:
            print("Ya has introducido la letra. Prueba con otra.")
            continue

        if letra not in string.ascii_lowercase:
            print("Entrada inválida. Por favor, introduce una letra del alfabeto.")
            continue

        if letra in palabra_secreta.lower():
            letra_adivinadas.append(letra)
            if set(letra_adivinadas) == set(palabra_secreta.lower()):
                print("¡Has acertado la palabra!")
                break
        else:
            intentos_restantes -= 1
            print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")

    if intentos_restantes == 0:
        print(f"Has perdido. La palabra secreta era: {palabra_secreta}")

    seguir_jugando()

jugar_ahorcado()