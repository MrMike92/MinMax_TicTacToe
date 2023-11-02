"""MIT License
Copyright (c) 2023 MrMike92
Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software"), para tratar el Software sin restricciones, incluyendo, sin limitación, los derechos de uso, copia, modificación, fusión, publicación, distribución, sublicencia y/o venta de copias del Software, y para permitir a las personas a las que se les proporcione el Software a hacerlo, sujeto a las siguientes condiciones:
El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o porciones sustanciales del Software.
EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD, ADECUACIÓN PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES POR CUALQUIER RECLAMO, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, DERIVADA DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL SOFTWARE."""

import pygame
import sys
import random

class JuegoDelGato:
    def __init__(self):
        pygame.init()
        # Configuración de la ventana
        self.width, self.high = 800, 700
        self.window = pygame.display.set_mode((self.width, self.high))
        pygame.display.set_caption("Juego del Gato")
        self.recuadro = (255, 255, 255)
        self.linea = (0, 0, 0)
        # Inicializar el tablero
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        # Variable para indicar si el juego ha terminado
        self.juego_terminado = False
        # Mensajes
        self.mensajes = []
        # Ancho de la columna de mensajes
        self.mensaje_width = 220

    def dibujar_tablero(self):
        self.window.fill(self.recuadro)
        for fila in range(3):
            for col in range(3):
                pygame.draw.rect(self.window, self.linea, (col * (self.width - self.mensaje_width) / 3, fila * (self.high - 60) / 3, (self.width - self.mensaje_width) / 3, (self.high - 60) / 3), 1)
                if self.tablero[fila][col] == "X":
                    pygame.draw.line(self.window, self.linea, (col * (self.width - self.mensaje_width) / 3, fila * (self.high - 60) / 3),
                                     ((col + 1) * (self.width - self.mensaje_width) / 3, (fila + 1) * (self.high - 60) / 3), 2)
                    pygame.draw.line(self.window, self.linea, (col * (self.width - self.mensaje_width) / 3, (fila + 1) * (self.high - 60) / 3),
                                     ((col + 1) * (self.width - self.mensaje_width) / 3, fila * (self.high - 60) / 3), 2)
                
                elif self.tablero[fila][col] == "O":
                    pygame.draw.circle(self.window, self.linea, (col * (self.width - self.mensaje_width) / 3 + (self.width - self.mensaje_width) / 6, fila * (self.high - 60) / 3 + (self.high - 60) / 6),
                                       (self.width - self.mensaje_width) / 6, 2)

    def verificar_ganador(self, jugador):
        for i in range(3):
            if all(self.tablero[i][j] == jugador for j in range(3)):
                return True
            
            if all(self.tablero[j][i] == jugador for j in range(3)):
                return True
            
        if all(self.tablero[i][i] == jugador for i in range(3)) or all(self.tablero[i][2 - i] == jugador for i in range(3)):
            return True
        
        return False

    def reiniciar_juego(self):
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        self.juego_terminado = False

    def dibujar_boton_reinicio(self):
        pygame.draw.rect(self.window, self.linea, (10, self.high - 40, 130, 33), 2)
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render("Reiniciar", True, self.linea)
        self.window.blit(texto, (20, self.high - 35))

    def dibujar_boton_cerrar(self):
        pygame.draw.rect(self.window, self.linea, (200, self.high - 40, 100, 33), 2)
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render("Cerrar", True, self.linea)
        self.window.blit(texto, (210, self.high - 35))

    def mostrar_mensajes(self):
        pygame.draw.rect(self.window, self.recuadro, (self.width - self.mensaje_width, 0, self.mensaje_width, self.high))
        fuente = pygame.font.Font(None, 24)
        y_offset = 20
        for mensaje in self.mensajes:
            texto = fuente.render(mensaje, True, self.linea)
            self.window.blit(texto, (self.width - self.mensaje_width + 20, y_offset))
            y_offset += 30

    def minimax(self, profundidad, es_maximizador):
        if self.verificar_ganador("O"):
            return 1
        
        if self.verificar_ganador("X"):
            return -1
        
        if not any("" in row for row in self.tablero):
            return 0

        if es_maximizador:
            mejor_valor = float("-inf")
            for fila in range(3):
                for col in range(3):
                    if self.tablero[fila][col] == "":
                        self.tablero[fila][col] = "O"
                        valor = self.minimax(profundidad + 1, False)
                        self.tablero[fila][col] = ""
                        mejor_valor = max(mejor_valor, valor)
            return mejor_valor
        else:
            mejor_valor = float("inf")
            for fila in range(3):
                for col in range(3):
                    if self.tablero[fila][col] == "":
                        self.tablero[fila][col] = "X"
                        valor = self.minimax(profundidad + 1, True)
                        self.tablero[fila][col] = ""
                        mejor_valor = min(mejor_valor, valor)
            return mejor_valor

    def movimiento_optimo(self):
        mejor_valor = float("-inf")
        mejor_movimiento = None
        for fila in range(3):
            for col in range(3):
                if self.tablero[fila][col] == "":
                    self.tablero[fila][col] = "O"
                    valor = self.minimax(0, False)
                    self.tablero[fila][col] = ""
                    if valor > mejor_valor:
                        mejor_valor = valor
                        mejor_movimiento = (fila, col)

        return mejor_movimiento

    def juego_del_gato(self):
        jugador_actual = "X"
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if not self.juego_terminado:
                    if jugador_actual == "X":
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            x, y = event.pos
                            fila = int(y // (self.high / 3))
                            col = int(x // ((self.width - self.mensaje_width) / 3))
                            if 0 <= fila < 3 and 0 <= col < 3:
                                if self.tablero[fila][col] == "":
                                    self.tablero[fila][col] = jugador_actual
                                    if self.verificar_ganador(jugador_actual):
                                        mensaje = f"¡El jugador {jugador_actual} ha ganado!"
                                        self.mensajes.append(mensaje)
                                        self.juego_terminado = True
                                        
                                    elif all(self.tablero[i][j] != "" for i in range(3) for j in range(3)):
                                        mensaje = "¡Empate!"
                                        self.mensajes.append(mensaje)
                                        self.juego_terminado = True

                                jugador_actual = "O"

                    elif jugador_actual == "O":
                        if not self.verificar_ganador("O") and not self.verificar_ganador("X") and not all(self.tablero[i][j] != "" for i in range(3) for j in range(3)):
                            if all(self.tablero[i][j] == "" for i in range(3) for j in range(3)):
                                # En el primer turno de la IA, elige una casilla aleatoria
                                fila, col = random.choice([(0, 0), (0, 2), (2, 0), (2, 2)])
                            else:
                                fila, col = self.movimiento_optimo()
                            self.tablero[fila][col] = "O"
                            if self.verificar_ganador("O"):
                                mensaje = f"¡El jugador {jugador_actual} ha ganado!"
                                self.mensajes.append(mensaje)
                                self.juego_terminado = True
                            elif all(self.tablero[i][j] != "" for i in range(3) for j in range(3)):
                                mensaje = "¡Empate!"
                                self.mensajes.append(mensaje)
                                self.juego_terminado = True

                        jugador_actual = "X"

                # Verificar si se hizo clic en el botón de reinicio
                if event.type == pygame.MOUSEBUTTONDOWN and 10 <= event.pos[0] <= 140 and self.high - 40 <= event.pos[1] <= self.high - 10:
                    self.reiniciar_juego()

                # Verificar si se hizo clic en el botón de cerrar
                if event.type == pygame.MOUSEBUTTONDOWN and 200 <= event.pos[0] <= 300 and self.high - 40 <= event.pos[1] <= self.high - 10:
                    pygame.quit()
                    sys.exit()

            self.dibujar_tablero()
            self.dibujar_boton_reinicio()
            self.dibujar_boton_cerrar()
            self.mostrar_mensajes()
            pygame.display.update()

if __name__ == "__main__":
    juego = JuegoDelGato()
    juego.juego_del_gato()