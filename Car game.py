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
Car_y = 525
#Starting cords for Player Bot1
Bot1_x = 75
Bot1_y = 200
#Starting cords for Player Bot2
Bot2_x = 325
Bot2_y = 200
#Starting cords for Player Bot3
Bot3_x = 575
Bot3_y = 200
#Starting cords for Player Bot4
Bot4_x = 825
Bot4_y = 200
#Defining game loop
def game_loop():
    global Car_x, Car_x_change
    quit_game= False

    Car_x_change = 0

    #Car code
    while not quit_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Car_x_change = -20
                elif event.key == pygame.K_RIGHT:
                    Car_x_change = 20
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    Car_x_change = 0
                elif event.key == pygame.K_RIGHT:
                    Car_x_change = 0

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
        #Bot1 Code
        Bot1_Bot1 = pygame.Rect(Bot1_x, Bot1_y, 20, 20)
        Bot1 = pygame.image.load( 'car_3.png' ).convert_alpha()
        resized_Bot1 = pygame.transform.smoothscale(Bot1, [ 100,170 ])
        screen.blit(resized_Bot1, Bot1_Bot1)
        #Bot2 Code
        Bot2_Bot2 = pygame.Rect(Bot2_x, Bot2_y, 20, 20)
        Bot2 = pygame.image.load( 'car_4.png' ).convert_alpha()
        resized_Bot2 = pygame.transform.smoothscale(Bot2, [ 100,170 ])
        screen.blit(resized_Bot2, Bot2_Bot2)
        #Bot3 Code
        Bot3_Bot3 = pygame.Rect(Bot3_x, Bot3_y, 20, 20)
        Bot3 = pygame.image.load( 'car_6.png' ).convert_alpha()
        resized_Bot3 = pygame.transform.smoothscale(Bot3, [ 100,170 ])
        screen.blit(resized_Bot3, Bot3_Bot3)
        #Bot4 Code
        Bot4_Bot4 = pygame.Rect(Bot4_x, Bot4_y, 20, 20)
        Bot4 = pygame.image.load( 'car_2.png' ).convert_alpha()
        resized_Bot4 = pygame.transform.smoothscale(Bot4, [ 100,170 ])
        screen.blit(resized_Bot4, Bot4_Bot4)
        Car_x += Car_x_change
        if Car_x >= 885 or Car_x <10:
            Car_x_change = 0

        #Bot1 Code
        while not quit_game:
            for event in pygame.event.get():
                Bot1_y_change = -20
          
        
            #Update Screen
        pygame.display.update()
        clock.tick(25)

game_loop()
