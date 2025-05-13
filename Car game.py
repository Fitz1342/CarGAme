#Imports
import pygame
import time
import random
    
#Screen
pygame.init()
screen = pygame.display.set_mode((1000,720),pygame.RESIZABLE)

#Game icon/Game name
game_icon = pygame.image.load('game_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Car game")

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

#Starting cords for Player car
Car_x = 325
Car_y = 300
   
#Defining game loop
def game_loop():
    global Car_x, Car_y
    quit_game= False
    
    #background colour
    screen.fill(grey)

    #Lines on background
    pygame.draw.rect(screen,white,[250,0,4,1000])

    pygame.draw.rect(screen,white,[500,0,4,1000])

    pygame.draw.rect(screen,white,[750,0,4,1000])

    pygame.draw.rect(screen,yellow,[1,0,4,1000])

    pygame.draw.rect(screen,yellow,[995,0,4,1000])

    #Player Car Code
    Car_Car = pygame.Rect(Car_x, Car_y, 20, 20)
    Car = pygame.image.load( 'car_1.png' ).convert_alpha()
    resized_Car = pygame.transform.smoothscale(Car, [ 100,170 ])
    screen.blit(resized_Car, Car_Car)


    #Update Screen
    pygame.display.update()

    
     
game_loop()
