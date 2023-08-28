import pygame
import math

pygame.init()

#define screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Masks")

#define colours
BG = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#hide mouse cursor
pygame.mouse.set_visible(False)

#create soldier
soldier = pygame.image.load("C:/Users/yueya/OneDrive/Documents/Cs projects/Flappy/assets/bird.png").convert_alpha()
soldier_rect = soldier.get_rect()
soldier_mask = pygame.mask.from_surface(soldier)
mask_image = soldier_mask.to_surface()

#create bullet and mask
bullet = pygame.Surface((10, 10))
bullet.fill(RED)
bullet_mask = pygame.mask.from_surface(bullet)

soldier_rect.topleft  = (350,250)
velocityX = 0
velocityY = 0


#game loop
run = True
while run:

  #get mouse coordinates
  pos = pygame.mouse.get_pos()

  #update background
  screen.fill(BG)
  distanceFromCursor = math.sqrt(math.pow((soldier_rect.x+soldier.get_width()/2)-pos[0],2)+math.pow((soldier_rect.y+soldier.get_height()/2)-pos[1],2))
  #check mask overlap
  if soldier_mask.overlap(bullet_mask, (pos[0]- soldier_rect.x, pos[1]-soldier_rect.y)):
    col = RED
  else:
    col = GREEN


  #draw mask image
  screen.blit(mask_image,(0,0))
  screen.blit(soldier,soldier_rect)

  #draw rectangle
  bullet.fill(col)
  screen.blit(bullet, pos)

  # moves away from the cursor
  if  distanceFromCursor<200:
    if pos[0]< soldier_rect.x:
      velocityX = (1/distanceFromCursor) * 50
    elif pos[0] > soldier_rect.x+soldier.get_width()/2:
      velocityX = (1/distanceFromCursor) * -50
    if pos[1]< soldier_rect.y:
      velocityY = (1/distanceFromCursor) * 50
    elif pos[1] > soldier_rect.y+soldier.get_height()/2:
      velocityY = (1/distanceFromCursor) * -50

  soldier_rect.x = soldier_rect.x + velocityX
  soldier_rect.y = soldier_rect.y + velocityY



  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  #update display
  pygame.display.flip()

pygame.quit()