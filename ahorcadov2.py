import random
import string

class Ahorcado:
    def __init__(self):
        self.lista_de_palabra = ["programador", "aprendiendo", "juego", "phyton", "react", "javascript"]
        self.palabra_secreta = ""
        self.letras_adivinadas = []
        self.intentos_restantes = 5

    def elegir_palabra(self):
        while True:
            respuesta = input("¿Desea elegir una palabra para que su rival adivine? (Si/No): ").lower()
            if respuesta == "si":
                self.palabra_secreta = input("Ingrese la palabra: ").lower()
                break
            elif respuesta == "no":
                self.palabra_secreta = random.choice(self.lista_de_palabra)
                break
            else:
                print("Respuesta no válida. Por favor, responda 'Si' o 'No'.")

    def mostrar_progreso(self):
        palabra_mostrada = ""
        for letra in self.palabra_secreta:
            if letra.lower() in self.letras_adivinadas:
                palabra_mostrada += letra.lower()
            else:
                palabra_mostrada += "-"
        print("Palabra:", palabra_mostrada)
        print(f"Intentos restantes: {self.intentos_restantes}")

    def ayuda_al_usuario(self):
        while True:
            ayuda = input("¿Necesitas ayuda? (Si/No): ").lower()
            if ayuda == "si":
                pista = input("Darle pista al usuario: ")
                return pista
            elif ayuda == "no":
                return None
            else:
                print("Respuesta no válida. Por favor, responde 'Si' o 'No'.")

    def adivinar_letra(self):
        letra = input("Introduzca una letra: ").lower()
        if letra in self.letras_adivinadas:
            print("Ya has introducido esta letra. Por favor, prueba otra.")
            self.adivinar_letra()
        elif letra not in string.ascii_lowercase:
            print("Entrada inválida. Por favor, introduzca una letra del alfabeto.")
            self.adivinar_letra()
        else:
            self.letras_adivinadas.append(letra)
            if letra in self.palabra_secreta:
                print("¡Correcto! Has adivinado una letra.")
            else:
                self.intentos_restantes -= 1
                print(f"Incorrecto. Te quedan {self.intentos_restantes} intentos.")

    def jugar(self):
        print("Bienvenido al juego del ahorcado")
        self.elegir_palabra()
        while self.intentos_restantes > 0:
            self.mostrar_progreso()
            self.ayuda_al_usuario()
            self.adivinar_letra()
            if set(self.letras_adivinadas) == set(self.palabra_secreta):
                print("¡Felicidades! Has adivinado la palabra correctamente.")
                seguir_jugando()
                break
        else:
            print(f"Lo siento, has agotado todos tus intentos. La palabra secreta era '{self.palabra_secreta}'.")

def seguir_jugando():
    while True:
        continuar_juego = input("¿Quieres seguir jugando? (Si/No): ").lower()
        if continuar_juego == "si":
           juego = Ahorcado()
           juego.jugar()
        elif continuar_juego == "no":
            print("Gracias por jugar al juego del ahorcado")
            break
        else:
            print("Respuesta no válida. Por favor, responde 'Si' o 'No'.")

juego = Ahorcado()
juego.jugar()

