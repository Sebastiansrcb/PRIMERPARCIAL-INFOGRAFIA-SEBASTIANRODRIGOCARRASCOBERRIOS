import math
import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


class Player(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x=center_x, center_y=center_y,)
        self.radius =  8
        self.speed = 0
        self.change_x = 0
        self.change_y = 0
    
    def collides_with_circle(self, center_x, center_y, radius):
        dx = self.center_x - center_x
        dy = self.center_y - center_y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance <= radius + self.radius:
            return True
        else:
            return False

    def update(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

class Disc(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x = center_x, center_y = center_y)
        self.change_x = 5
        self.change_y = 5
        self.radius = 16

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Comprobar si el disco ha chocado con los bordes de la ventana
        if self.left < 0 or self.right > SCREEN_WIDTH - 10 :
            self.change_x *= -1
        if self.bottom < 0 or self.top > SCREEN_HEIGHT - 10:
            self.change_y *= -1
