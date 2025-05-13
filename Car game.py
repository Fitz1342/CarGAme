#Imports
import pygame
import time
import random
    
#Screen
pygame.init()
screen = pygame.display.set_mode((1000,720),pygame.RESIZABLE)

#Game icon/Game name


#Colors
blue = (0,0, 255)
black = (0, 0, 0)
green = (188, 227, 199)
red = (255, 0, 0)
grey = (45, 45, 45)
white = (255, 255 , 255)
yellow = (255, 255, 0)
#Clock/Time
clock = pygame.time.Clock()

#Fonts
exit_font = pygame.font.Font("freesansbold.ttf", 30)
score_font = pygame.font.SysFont("arialblack", 20)
high_score_font = pygame.font.SysFont("arialblack", 20)
font = pygame.font.Font("freesansbold.ttf", 50)

   
#Defining game loop
def game_loop():
    global car_x, car_y
    quit_game= False
    
    #background colour
    screen.fill(grey)

   
    
    pygame.draw.rect(screen,white,[250,0,4,1000])

    pygame.draw.rect(screen,white,[500,0,4,1000])

    pygame.draw.rect(screen,white,[750,0,4,1000])

    pygame.draw.rect(screen,yellow,[1,0,4,1000])

    pygame.draw.rect(screen,yellow,[995,0,4,1000])

                                                   
    
    #Update Screen
    pygame.display.update()

    
     
game_loop()
