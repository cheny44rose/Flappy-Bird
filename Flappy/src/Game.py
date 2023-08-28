import pygame
from Bird import Bird
from Walls import Wall
from View import View
import Gameover
import Startscreen
import random



class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.background = pygame.image.load("c:/Users/yueya/OneDrive/Desktop/Flappy/assets/background.png").convert_alpha()
        self.Bird = Bird(self.screen,self.screen.get_width()/8,self.screen.get_height()/2-50)
        # self.view = View(self.screen)
        self.walls = []
        self.score = 0

        self.timer = 0
        self.spawnRate = 50

        self.velocity = 0
        self.pressed = False
        
        
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.White = (255,255,255)
        
        self.bullet = pygame.Surface((10,10))
        self.bullet.fill((255,0,0))
        self.bullet_mask = pygame.mask.from_surface(self.bullet)

        self.pipeOffset = 250

        self.font = pygame.font.SysFont("arialblack",40)
        

        self.game_start = True
        self.game_paused = False






    def draw_game(self):
        self.screen.blit(self.background,(0,0))

        self.Bird.draw()
        for top in self.walls:
            top.draw()
        self.draw_text(str(self.score),self.font,self.White,10,0)
    
    def draw_text(self, text,font,text_col,x,y):
        img = font.render(text,True,text_col)
        self.screen.blit(img,(x,y))   



    def run_one_cycle(self):
        if self.game_start:
            self.game_start = Startscreen.main()
            self.Bird = Bird(self.screen,self.screen.get_width()/8,self.screen.get_height()/2-50)
            self.view = View(self.screen)
            self.walls = []
            self.score = 0

        #Gravity
        self.velocity +=0.5
        if self.velocity > 8:
            self.velocity = 8
        if self.Bird.y+self.Bird.Bird.get_height()<600:
            self.Bird.y+=int(self.velocity)
        if self.Bird.y<0:
            self.Bird.y = 0
        # jumping
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE] and self.pressed == False:
            self.pressed = True
            self.velocity = -7
        if not keys_pressed[pygame.K_SPACE]:
            self.pressed = False
        # rotating bird
        # self.Bird.Bird = pygame.transform.rotate(self.Bird.Bird,self.velocity*-2)


        pos = pygame.mouse.get_pos()
        if self.Bird.Bird_mask.overlap(self.bullet_mask, (pos[0]-self.Bird.x, pos[1]-self.Bird.y)):
            col = self.RED
        else:
            col = self.GREEN

        self.bullet.fill(col)
        self.screen.blit(self.bullet, pos)

        for k in range(len(self.walls) - 1, -1, -1):
            self.walls[k].move()
            if self.walls[k].x<-100:

                del self.walls[k]
            
            if (self.Bird.x+self.Bird.Bird.get_width()/2) == (self.walls[k].x +self.walls[k].pipe.get_width()/2):
                self.score+=1
            if self.walls[k].pipe_mask.overlap(self.Bird.Bird_mask, (self.Bird.x-self.walls[k].x, self.Bird.y-self.walls[k].y)) or self.Bird.y+self.Bird.Bird.get_height()==600:
                Gameover.main()
                self.game_start = True



        lowestPoint = 0 - self.pipeOffset
        highestPoint = 0
        if self.timer<self.spawnRate:
            self.timer = self.timer + 1
        else:
            pipe = Wall(self.screen,self.screen.get_width(),random.randrange(lowestPoint,highestPoint),"bot")
            self.walls.append(pipe)
            self.timer = 0




        
        

        # Checks if the player goes too high or low

