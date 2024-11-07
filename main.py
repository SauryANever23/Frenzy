import pygame
import sys 

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Killing Game")

background_color = (106, 137, 167)

screen.fill(background_color)

main_character = 0

pygame.display.update()

game_state = True
while game_state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    