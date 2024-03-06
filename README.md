 ### Reglas del Juego:

- El juego se juega con dos participantes: uno selecciona una palabra y el otro adivina las letras.
- La palabra seleccionada debe estar oculta para el adivinador, representada inicialmente por guiones bajos o guiones.
- El adivinador intenta adivinar las letras de la palabra una por una.
- Se permite un cierto número de intentos incorrectos antes de que termine el juego.

### Interfaz de Usuario:

- Mostrar el estado actual de la palabra, mostrando las letras adivinadas y guiones para las letras restantes.
- Mostrar el número de intentos incorrectos permitidos y el número de intentos incorrectos realizados hasta el momento.
- Proporcionar una forma para que el usuario ingrese sus intentos (típicamente una letra a la vez).
  
### Ingreso de Palabra:

- Implementar un mecanismo que permita que uno de los participantes ingrese una palabra para que sea adivinada por el otro.
- Validar la entrada para asegurarse de que la palabra ingresada sea válida (por ejemplo, solo letras y sin espacios).
- Proporcionar la opción de que la palabra sea seleccionada aleatoriamente de una lista predefinida si no se ingresa manualmente.

### Progreso del Juego:

- Seguir el progreso del juego, incluyendo las letras adivinadas y los intentos incorrectos.
- Actualizar la pantalla después de cada intento para reflejar los cambios en la palabra y el número de intentos incorrectos.

### Condiciones de Fin del Juego:

- Definir las condiciones para ganar y perder el juego.
- El juego se gana si el adivinador adivina correctamente todas las letras de la palabra antes de exceder los intentos incorrectos permitidos.
- El juego se pierde si el adivinador excede los intentos incorrectos permitidos.

### Retroalimentación:

- Proporcionar retroalimentación al usuario después de cada intento, indicando si la suposición fue correcta o incorrecta.
- Mostrar un mensaje cuando se gana o pierde el juego.

### Rejugabilidad:

- Permitir que el usuario juegue el juego varias veces sin reiniciar el programa.
- Después de que termine un juego, preguntar al usuario si desea jugar de nuevo.

### Puntuación (Opcional):

- Si se desea, implementar un sistema de puntuación basado en el número de suposiciones correctas y el tiempo necesario para completar el juego.

### Manejo de Errores:

- Implementar manejo de errores para entradas inválidas (por ejemplo, caracteres no alfabéticos, suposiciones repetidas).
