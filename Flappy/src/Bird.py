import pygame

class Bird:
    def __init__(self,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        self.jump_height = 20
        self.y_velocity = self.jump_height
        self.jumped = False

        
        self.Bird = pygame.image.load("c:/Users/yueya/OneDrive/Desktop/Flappy/assets/bird.png").convert_alpha()
        self.Bird_rect = self.Bird.get_rect()
        self.Bird_mask = pygame.mask.from_surface(self.Bird)
        self.mask_image = self.Bird_mask.to_surface(setcolor=(0, 255, 0, 255), unsetcolor=(0, 0, 0, 0))




     
        
    
    def draw(self):
        self.screen.blit(self.Bird,(self.x,self.y))
        # self.screen.blit(self.Bird,(self.x-int(self.Bird.get_width()/2),self.y-int(self.Bird.get_height()/2)))
        # pygame.draw.circle(self.screen, (255, 0, 0), (self.x+self.bat.get_width()/2,self.y), 2)
        # self.screen.blit(self.mask_image, (self.x,self.y))
        # self.hitbox = pygame.Rect(self.x+2,
        #                           self.y+2,
        #                           self.bat.get_width(),
        #                           self.bat.get_height()-10)
        # pygame.draw.rect(self.screen,(0,0,0),self.hitbox,1)
    
    def jump(self):
        self.y -=self.y_velocity
        if(self.y_velocity<-self.jump_height):
            self.jumped = False
            self.y_velocity = self.jump_height

