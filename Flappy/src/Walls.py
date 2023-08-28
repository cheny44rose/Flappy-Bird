import pygame
import random

class Wall:
    def __init__(self,screen,x,y,pos):
        self.screen = screen
        self.x = x
        self.y = y
        self.pos = pos
        self.pipe = pygame.image.load("c:/Users/yueya/OneDrive/Desktop/Flappy/assets/pipe.png").convert_alpha()
        self.pipe_rect = self.pipe.get_rect()
        self.pipe_mask = pygame.mask.from_surface(self.pipe)
        self.mask_image = self.pipe_mask.to_surface(setcolor=(0, 255, 0, 255), unsetcolor=(0, 0, 0, 0))
        
        
        # self.top = pygame.image.load("c:/Users/yueya/OneDrive/Desktop/Flappy/assets/pipe up.png").convert_alpha()
        # self.top_rect = self.top.get_rect()
        # self.top_mask = pygame.mask.from_surface(self.top)
        # self.tmask_image = self.top_mask.to_surface(setcolor=(0, 255, 0, 255), unsetcolor=(0, 0, 0, 0))




    
    def draw(self):
        # if self.pos == "top":
        self.screen.blit(self.pipe,(self.x,self.y))
        # pygame.draw.circle(self.screen, (255, 0, 0), (self.x+self.pipe.get_width()/2,self.x+300), 5)
        # self.screen.blit(self.mask_image, (self.x,self.y))
        # elif self.pos == "bot":
        #     self.screen.blit(self.bot,(self.x,self.y))
        #     self.screen.blit(self.bmask_image, (self.x,self.y))
    
    def move(self):
        self.x-=5
