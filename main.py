import math
import random
import pygame

import definition as d
import videomaker as v
import Ball as b

# Instanciation des variables
balls = []

# Initialisation de pygame
pygame.init()
screen = pygame.display.set_mode((d.SCREEN_DIMENSIONS["x"], d.SCREEN_DIMENSIONS["y"]))
pygame.display.set_caption("TikTok bounce")
clock = pygame.time.Clock()
running = True

# Boucle principale
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                balls.append(b.Ball(20))

    screen.fill("black")
    for i in balls:
        i.update()
        i.draw(screen)
    pygame.display.flip()

    """
    pygame.image.save(screen, f"frames/frame_{d.frame_id:04d}.png")
    d.frame_id += 1
    """

    clock.tick(60)

pygame.quit()

"""
v.makeVideo()
v.cleanFrames()
"""