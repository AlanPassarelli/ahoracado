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

#----------------------------------------------------------
# V2 - Implementar el uso de objetos y hacer uso de ellos. 


import random
import string

#Seleccion de palabra

def eleccion_de_palabra (lista_de_palabra):
    
    #Restringir el lo que ingresa el usuario a solamente Si o No... ya que puede confundirse e ingresar cualquier otro texto como si fuera la palabra a ingresar.
    respuesta = input ("Desea elegir palabra para que su rival adivine ? (Si/No): ") 

    if respuesta.lower() == "si":
        palabra_elegida = input ("Escribi la palabra: ")
        return palabra_elegida
    
    palabra_elegida = random.choice(lista_de_palabra)
    return palabra_elegida

#Ayuda al usuario
def ayuda_al_usuario ():
    #Restringir el lo que ingresa el usuario a solamente Si o No...
    ayuda = input ("necesitas ayuda? (Si/no)")
    if ayuda.lower() == "si":
        #Este input no devuelve nada, y luego vuelve a pedir la palabra supuesta.
        # Luego del segundo input la ayuda no hace nada. 
        input ("comentame tu suposición")
        return input ("tu suposición es: ")


#Tablero de juego
        
def adivinar_palabra (palabra_secreta, letras_adivinadas, intentos_restantes):

    palabra=""
    for letra in palabra_secreta:

        if letra in letras_adivinadas:
            palabra+= letra

        else:
            palabra += "-"
    print (palabra)
    print (f"intentos restantes: {intentos_restantes}")
    print ("intentos permitidos: 5")
    ayuda_al_usuario ()

#Continuar jugando    
def seguir_jugando ():
    continuar_juego = input ("queres seguir jugando: (si/no)")
    if continuar_juego.lower() == "si":
        jugar_ahorcado ()
    else:
        #Esta bien que por default si no pone "si" avise que sale del juego pero deberia avisar que seleccion el No por default.
        print("gracias por jugar al juego del ahorcado")
    return

#logica de juego
    
def jugar_ahorcado ():

    lista_de_palabra = ["programador", "aprendiendo", "juego", "phyton", "react", "javascript"]
    palabra_secreta = eleccion_de_palabra(lista_de_palabra)
    letra_adivinadas = []
    intentos_restantes = 5

    print("Bienvenido al juego del ahorcado")
    print("La palabra a adivinar es: ") 

    while intentos_restantes>0:
        adivinar_palabra(palabra_secreta, letra_adivinadas, intentos_restantes)
        letra=input ("introduce una letra: ").lower ()

        if letra in letra_adivinadas:
            print ("ya has introducido la letra. Prueba con Otra")
            continue

        if letra not in string.ascii_lowercase:
            print("Entrada inválida. Por favor, introduce una letra del alfabeto.")
            continue

        #Si la palabra ingresa tiene alguna mayuscula y el usuario no la ingresa en mayuscula no la reconoce. 
        if letra in palabra_secreta:
            letra_adivinadas.append(letra)
            if set (letra_adivinadas) == set (palabra_secreta):
                print ("has acertado la palabra")
                break
        else:
            intentos_restantes-=1
            print (f"Letra incorrecta. te quedan {intentos_restantes}")

    if intentos_restantes == 0:
        print (f"Has perdido. la palabra secreta era: {palabra_secreta}")
        seguir_jugando ()
    else:
        seguir_jugando ()    

jugar_ahorcado ()
