import pygame
import sys
from View import View


def main():
    pygame.init()
    pygame.display.set_caption("Testing the Game Over Screen")
    screen_WIDTH = 800
    screen_Height = 600
    screen = pygame.display.set_mode((screen_WIDTH,screen_Height))
    pygame.mouse.set_visible(True)
    background = pygame.image.load("c:/Users/yueya/OneDrive/Desktop/Flappy/assets/background.png").convert_alpha()
    screen.blit(background,(0,0))
    run_game_over_loop(screen)
    

def run_game_over_loop(screen):
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        
        img = pygame.font.SysFont("arialblack",40).render("Game Over",True,(255,255,255))
        screen.blit(img,(10,0)) 
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if keys_pressed[pygame.K_SPACE]:

            return True

        
        pygame.display.update()


if __name__ == "__main__":
    main()