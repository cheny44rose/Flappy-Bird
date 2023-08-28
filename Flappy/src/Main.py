import pygame
from Game import Game
from Controller import Controller
from View import View
import sys
pygame.init()

screen_WIDTH = 800
screen_Height = 600
screen = pygame.display.set_mode((screen_WIDTH,screen_Height))

framerate = 60
clock = pygame.time.Clock()

game = Game(screen)
controller = Controller(game)
viewer = View(screen)

GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.mouse.set_visible(False)



run = True
while run:
    
    clock.tick(framerate)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
    # controller.get_and_handle_events(game)
    # viewer.draw_everything()
    game.draw_game()
    game.run_one_cycle()

    
    pygame.display.update()
pygame.quit()