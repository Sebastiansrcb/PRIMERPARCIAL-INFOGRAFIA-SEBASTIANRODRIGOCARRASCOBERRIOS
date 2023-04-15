# PRIMER PARCIAL INFOGRAFIA
# SEBASTIAN RODRIGO CARRASCO BERRIOS
# HOCKEY DE AIRE

Este código es un juego de hockey de aire que utiliza la biblioteca arcade para Python. El juego se ejecuta en una ventana y los jugadores pueden mover sus discos para tratar de golpear un disco central hacia la meta del oponente. Cada jugador tiene un disco y los discos rebotan en las paredes de la ventana.

La clase Player es una subclase de arcade.Sprite que representa a cada jugador y su disco en el juego. La clase Disc es una subclase de arcade.Sprite que representa el disco central. Ambas clases tienen un método update() que se llama en cada frame para actualizar su posición en la ventana. La clase Player también tiene un método collides_with_circle() que comprueba si el disco del jugador ha chocado con el disco central.

La clase App es una subclase de arcade.Window que maneja la ventana y el bucle del juego. El método on_key_press() maneja la entrada del teclado del jugador y actualiza la velocidad y dirección del disco del jugador en consecuencia. El método on_key_release() se llama cuando se suelta una tecla y detiene el movimiento del disco del jugador en esa dirección.

En el método __init__() se crean los objetos del juego, incluyendo los jugadores, el disco central y los arcos. También se crean variables para mantener el puntaje de cada jugador, las rachas de cada jugador y si el juego ha terminado o no.

En este código, los personajes y el disco se mueven por medio de la función update(), que se llama automáticamente en cada cuadro del juego. Cada cuadro se llama aproximadamente 60 veces por segundo en este juego.

Los personajes se mueven en respuesta a las teclas presionadas por el jugador. Las teclas que mueven los personajes hacia arriba, abajo, izquierda y derecha cambian las propiedades change_x y change_y del objeto de jugador correspondiente. La velocidad del jugador se establece en la propiedad speed. La función update() actualiza la posición del jugador multiplicando change_x y change_y por speed y agregando los resultados a las propiedades center_x y center_y del objeto de jugador correspondiente.

El disco se mueve por sí solo a lo largo de la pantalla. Su movimiento se controla en la función update() mediante las propiedades change_x y change_y. Si el disco choca con uno de los bordes de la pantalla, se invierte la dirección de la velocidad en la dirección correspondiente para que el disco rebote en la pantalla.

La función collides_with_circle() se utiliza para detectar si el disco ha colisionado con un jugador. Esta función calcula la distancia entre el centro del disco y el centro del jugador, y si esa distancia es menor que la suma de los radios del disco y el jugador, se considera que el disco ha colisionado con el jugador.

## COMO JUGAR

El Player 1 se maneja con las teclas arriba abajo izquierda y derecha el Player 2 con las teclas WASD ahora que sucede
Ambos jugadores tienen un movimiento limitado en la mitad de su propia cancha no pueden pasarse a la cancha del otro jugador para hacer el juego más interesante
Otra cosa a tomar en cuenta es que el juego se maneja con rachas de manera que si un jugador lleva una racha de 3 goles seguidos esto le quitara un punto al contrincante 
Pero recuerda esto solo ocurre con 3 goles seguidos si marcas 2 seguidos y el oponente marca 1 tu racha vuelve a 0

## COMO GANAR

En este HOCKEY gana el jugador que llegue primero a los 10 pts pero como tambien estamos manejando el sistema de rachas para hacer el juego más interesante si algun jugador llega a un score de -3 puntos pierde automaticamente 

Ahora que conoces el juego diviertete :D