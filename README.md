# Solución del juego del gato por medio del algoritmo MiniMax

El juego del gato, también conocido como "Tres en línea" o "Tic-Tac-Toe", es un juego de suma cero en el que ambos jugadores, si juegan de manera óptima, terminarán en empate, el siguente programa utiliza el algoritmo MiniMax, programación orientada a objetos y la biblioteca Pygame para crear una interfaz gráfica que representa este juego.

## Instrucciones de uso.

- Clona este repositorio en tu máquina local.
- Asegure que el respositorio se haya descargado correctamente.
- Abre el programa que deseas ejecutar en tu entorno de desarrollo que soporte Python 3.11.2 64-bit.

## Funcionamiento.

El juego del gato, también conocido como "Tres en línea" o "Tic-Tac-Toe", es un juego perfecto de suma cero, lo que significa que, si ambos jugadores juegan de manera óptima, el juego terminará en empate. El objetivo del juego es conseguir que tres de tus fichas estén en línea horizontal, vertical o diagonal antes que tu oponente como se muestra en la `Imagen 1`.

<img src="/img/Imagen1.jpg" alt="objetivoComunJuegoGatoGanar" title="Posibles formas de terminar el juego." width="500px"/>

> _**Imagen 1.- Posibles formas de terminar el juego.**_

<br/>

Para lograr esto se debe de realizar árbol de juego donde cada nodo representa un estado del juego y las aristas son las posibles jugadas, el objetivo es determinar la mejor jugada para el jugador maximizador, ver `Imagen 2` e `Imagen 3`.

<img src="/img/Imagen2.jpg" alt="arbolJuegoJugada" title="Árbol de juego para esta jugada." width="650px"/>

> _**Imagen 2.- Árbol de juego para esta jugada.**_

<br/>

<img src="/img/Imagen3.jpg" alt="arbolJuegoJugadaLibreta" title="Árbol de juego para esta jugada." width="650px"/>

> _**Imagen 3.- Árbol de juego para esta jugada.**_

Restricciones (ver Imagen 4):
  - Inicialmente el tablero está vacío.
  - MAX gana si obtiene una línea de 3 X.
  - MIN gana si obtiene una línea de 3 O.
  - Existe la posibilidad de empate.
  - MIN empieza en la primera ronda y se alternan los movimientos.
  - Cuando MAX gane, MIN empieza primero en la siguiente ronda y se alternan los movimientos.
  - Cuando MIN gane, MAX empieza primero en la siguiente ronda y se alternan los movimientos.
  - Cuando la ronda quede en empate, MIN o MAX empieza primero la siguiente ronda.

<img src="/img/Imagen5.jpg" alt="programaMinMaxAccion" title="" width="650px"/>

> _**Imagen 4.- Aplicación del árbol de juego.**_

Como el algoritmo MiniMax se centra en encontrar la mejor estrategia para un jugador en un juego competitivo, asumiendo que ambos jugadores juegan de manera óptima, funciona construyendo un árbol de búsqueda que representa todas las posibles secuencias de movimientos y asigna valores a los nodos para determinar cuán favorable es un estado del juego para un jugador en particular, y sus valores asignados representan la puntuación esperada para un jugador si ambos jugadores juegan de manera óptima `Imagen 3`.

## Ejecución.

<img src="/img/Imagen5.jpg" alt="ejecucionPrograma" title="Ejecución del programa." width="650px"/>

> _**Imagen 5.- Ejecución del programa**_

## Notas.

- Cuando a la IA le toca colocar primero su ficha, este tarda entre 5 a 10 segundos en colocarlo.
- Este código no tiene dependencias externas y debería funcionar con cualquier entorno Python 3.x.

Si deseas contribuir a este proyecto, puedes enviar solicitudes de extracción (pull requests) con mejoras o características adicionales y si tienes alguna pregunta o problema, puedes contactarme a través de mi perfil de GitHub MrMike92. :turtle:
