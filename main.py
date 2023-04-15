import math
import random
import arcade

from game_object import Player
from game_object import Disc

# definicion de constantes
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Hockey de Aire"
SCALING = 0.03
SCALINGD = 0.1

SPEED = 8
BULLET_SPEED = 15


class App(arcade.Window):
    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)
        self.sprites = arcade.SpriteList()
        self.player1 = Player("img/puck1.png", SCALING, SCREEN_WIDTH // 2 + 400, SCREEN_HEIGHT / 2 )
        self.player2 = Player("img/puck2.png", SCALING, SCREEN_WIDTH // 2 - 400, SCREEN_HEIGHT / 2)
        self.disc = Disc("img/disc.png", SCALINGD,SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
        #Arcos
        self.arc1 = arcade.SpriteSolidColor(16, 121, arcade.color.BEAU_BLUE)
        self.arc1.center_x = 7
        self.arc1.center_y = SCREEN_HEIGHT // 2 
        self.arc2 = arcade.SpriteSolidColor(16, 121, arcade.color.BEAU_BLUE)
        self.arc2.center_x = SCREEN_WIDTH - 7
        self.arc2.center_y = SCREEN_HEIGHT // 2

        self.sprites.append(self.arc1)
        self.sprites.append(self.arc2)
        self.sprites.append(self.player1)
        self.sprites.append(self.player2)
        self.sprites.append(self.disc)
        
        # Creamos los puntajes de cada jugador
        self.score_player1 = 0
        self.score_player2 = 0
        # Creamos rachas
        self.player1_streak = 0
        self.player2_streak = 0
        # Variable para ver si el juego termino
        self.gameover = 0
        self.winner = "nadie"
        self.puntajeganador = 0
        self.loser = "nadie"
        self.puntajeperdedor = 0

    def on_key_press(self, symbol: int, modifiers: int):
        # PLayer 1 movimiento azul
        if symbol == arcade.key.UP:
            self.player1.change_y = 1
            self.player1.speed = SPEED
        elif symbol == arcade.key.DOWN:
            self.player1.change_y = -1
            self.player1.speed = SPEED
        elif symbol == arcade.key.LEFT:
            self.player1.change_x = -1
            self.player1.speed = SPEED
            self.player1.change_y = 0
        elif symbol == arcade.key.RIGHT:
            self.player1.change_x += 1
            self.player1.speed = SPEED
            self.player1.change_y = 0
        # player 2 movimiento naranja      
        if symbol == arcade.key.W:
            self.player2.change_y = 1
            self.player2.speed = SPEED
        elif symbol == arcade.key.S:
            self.player2.change_y = -1
            self.player2.speed = SPEED
        elif symbol == arcade.key.A:
            self.player2.change_x = -1
            self.player2.speed = SPEED
            self.player2.change_y = 0
        elif symbol == arcade.key.D:
            self.player2.change_x += 1
            self.player2.speed = SPEED
            self.player2.change_y = 0

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP, arcade.key.DOWN):
            self.player1.change_y = 0
        elif symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player1.change_x = 0
        if symbol in (arcade.key.W, arcade.key.S):
            self.player2.change_y = 0
        if symbol in (arcade.key.A, arcade.key.D):
            self.player2.change_x = 0

    def on_update(self, delta_time: float):

         # Actualizar los sprites
        self.disc.update()
        self.player1.update()
        self.player2.update()

        # Comprobar si el disco ha chocado con alguno de los jugadores
        if self.player1.collides_with_circle(self.disc.center_x, self.disc.center_y, (self.disc.radius + self.player1.radius)):
           self.disc.change_y += random.uniform(-1,1)
           self.disc.change_x *= -1
        elif self.player2.collides_with_circle(self.disc.center_x, self.disc.center_y, (self.disc.radius+self.player2.radius) ):
           self.disc.change_y += random.uniform(-1,1)
           self.disc.change_x *= -1
       
        # Limitamos la posición de los jugadores dentro de la pantalla
        # Limites Player1
        if self.player1.left < SCREEN_WIDTH / 2:
            self.player1.left = SCREEN_WIDTH / 2
        elif self.player1.right > SCREEN_WIDTH:
            self.player1.right = SCREEN_WIDTH
        if self.player1.top > SCREEN_HEIGHT:
            self.player1.top = SCREEN_HEIGHT 
        elif self.player1.bottom < 0:
            self.player1.bottom = 0
        # Limites de Player2
        if self.player2.right > SCREEN_WIDTH / 2:
            self.player2.right = SCREEN_WIDTH / 2
        elif self.player2.left < 0:
            self.player2.left = 0
        if self.player2.top > SCREEN_HEIGHT:
            self.player2.top = SCREEN_HEIGHT 
        elif self.player2.bottom < 0:
            self.player2.bottom = 0

        # Comprobar si el disco colisiona con cualquiera de los arcos
        #Con Arco 1
        if arcade.check_for_collision(self.disc, self.arc1):
            self.score_player1 += 1
            self.disc.change_x *= -1
            self.player1_streak += 1
            self.player2_streak = 0
            
            if self.player1_streak == 3:
                self.score_player2 -= 1
                self.player1_streak = 0
                #self.player2_streak = 0
                #self.reset_positions()

        # Reiniciar la posición del disco
            self.disc.center_x = SCREEN_WIDTH // 2
            self.disc.center_y = SCREEN_HEIGHT // 2
        # Reiniciar la posición de los jugadores
            self.player1.center_x = SCREEN_WIDTH - 100
            self.player1.center_y = SCREEN_HEIGHT // 2
            self.player2.center_x = 100
            self.player2.center_y = SCREEN_HEIGHT // 2
        
        #Con arco 2
        elif arcade.check_for_collision(self.disc, self.arc2):
            self.score_player2 += 1
            self.disc.change_x *= -1
            self.player2_streak += 1
            self.player1_streak = 0
            if self.player2_streak == 3:
                self.score_player1 -= 1
                self.player2_streak = 0
                #self.player1_streak = 0
                #self.reset_positions()
            #else:
                #self.player2_streak = 0
        
        # Reiniciar la posición del disco
            self.disc.center_x = SCREEN_WIDTH // 2
            self.disc.center_y = SCREEN_HEIGHT // 2
        # Reiniciar la posición de los jugadores
            self.player1.center_x = SCREEN_WIDTH - 100
            self.player1.center_y = SCREEN_HEIGHT // 2
            self.player2.center_x = 100
            self.player2.center_y = SCREEN_HEIGHT // 2

        # Verificamos si algun jugador llego a un score de -3 o 10
        if self.score_player1 in (-3, 10) or self.score_player2 in (-3, 10):
            self.gameover = 1
            if self.score_player1 > self.score_player2:
                self.winner = "PLAYER 1 WINS"
                self.puntajeganador = self.score_player1
                self.loser = "PLAYER 2 LOSE"
                self.puntajeperdedor = self.score_player2
            else :
                self.winner = "PLAYER 2 WINS"
                self.puntajeganador = self.score_player2
                self.loser = "PLAYER 1 LOSE"
                self.puntajeperdedor = self.score_player1





    def on_draw(self):
        arcade.start_render()
        if self.gameover != 1 :
            # Bordes de la pantalla
            arcade.draw_rectangle_outline(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.BLUE, 30)

            # Elementos de la cancha
            arcade.draw_line(SCREEN_WIDTH // 2, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT, arcade.color.BLUE, 4)
            arcade.draw_circle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 40, arcade.color.WHITE)        
            arcade.draw_circle_outline(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, arcade.color.RED, 4)        
            arcade.draw_circle_outline(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 40, arcade.color.BLUE, 4)
            # arcade.draw_lrtb_rectangle_filled(0, 15, SCREEN_HEIGHT // 2 + 60, SCREEN_HEIGHT // 2 - 60, arcade.color.RED)
            # arcade.draw_lrtb_rectangle_filled(SCREEN_WIDTH - 14, SCREEN_WIDTH, SCREEN_HEIGHT // 2 + 60, SCREEN_HEIGHT // 2 - 60, arcade.color.RED)
        
            self.sprites.draw()
            arcade.draw_text(f"{self.score_player1} (Racha de: {self.player1_streak} )", SCREEN_WIDTH - 200, SCREEN_HEIGHT - 50, arcade.color.BLACK, font_size=15, anchor_x="center")
            arcade.draw_text(f"{self.score_player2} (Racha de: {self.player2_streak} )", 200, SCREEN_HEIGHT - 50, arcade.color.BLACK, font_size=15, anchor_x="center")
        else:
            # Elementos de la cancha
            arcade.draw_rectangle_filled(SCREEN_WIDTH//2,SCREEN_HEIGHT//2,SCREEN_WIDTH,SCREEN_HEIGHT,arcade.color.BLACK)
            arcade.draw_rectangle_outline(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.RED_DEVIL, 30)
            arcade.draw_line(SCREEN_WIDTH // 2, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT, arcade.color.RED_DEVIL, 4)
            arcade.draw_circle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 40, arcade.color.BLACK)        
            arcade.draw_circle_outline(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, arcade.color.BLUE, 4)        
            arcade.draw_circle_outline(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 40, arcade.color.RED_DEVIL, 4)
            arcade.draw_text(f"{self.winner}", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100, arcade.color.WHITE, font_size=40, anchor_x="center",font_name='Arial')
            arcade.draw_text(f"{self.puntajeganador}", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50, arcade.color.YELLOW_ROSE, font_size=30, anchor_x="center",font_name='Arial')
            arcade.draw_text(f"{self.loser}", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.WHITE_SMOKE, font_size=40, anchor_x="center",font_name='Arial')
            arcade.draw_text(f"{self.puntajeperdedor}", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 -50, arcade.color.YELLOW_ROSE, font_size=30, anchor_x="center",font_name='Arial')
            self.sprites.draw()
            self.disc.center_x = SCREEN_WIDTH/2 -5
            self.disc.center_y = SCREEN_HEIGHT/2 - 200

            
        


if __name__ == "__main__":
    app = App()
    arcade.run()
