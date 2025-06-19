import math
import random
import pygame

import definition as d

class Ball():
    def __init__(self, radius):
        self.x = d.SCREEN_DIMENSIONS["x"]/2
        self.y = d.SCREEN_DIMENSIONS["y"]/2
        self.r = radius
        self.color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
        self.V_x = random.uniform(-3,3)
        self.V_y = 0

    def update(self):
        # Déplacement
        self.x += self.V_x
        self.V_y += d.gravity
        self.y += self.V_y
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.r)
        pass

    pass