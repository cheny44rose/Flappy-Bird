import pygame


class View:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.background_color = pygame.Color(
            "black")  # TODO: Choose your own color
        
    
