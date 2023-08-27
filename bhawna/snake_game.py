# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 14:09:54 2022

@author: bhawana
"""

import pygame
import random
import os


pygame.mixer.init()


pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


# Creating window
screen_width = 600
screen_height = 500
gamewindow = pygame.display.set_mode((screen_width, screen_height))

#background image

    
bgimg = pygame.image.load("snakeimage.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width,screen_height)).convert_alpha()

bg = pygame.image.load("wlcmimage.jpg")
bg = pygame.transform.scale(bg, (screen_width,screen_height))

# Game Title

pygame.display.set_caption("Snakegame")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)
    

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])


def plot_snake(gamewindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])
        
def welcome():
    exit_game=False
    while not exit_game:
        #gamewindow.fill((233,210,229))
    
        gamewindow.blit(bg,(0,0))
        
        text_screen("Welcomes to snakes",black,150,180)
        text_screen("press space bar to play", black,142,230)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("snakegames.mp3")
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(30)    
                

# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    #check if hi_score file exists
    if(not os.path.exists("hi_score.py")):
        with open("hi_score.py","w") as f:
            f.write("0")
            
            
    with open("hi_score.py","r") as f:
        hi_score=f.read()

    food_x = random.randint(40, screen_width / 2)
    food_y = random.randint(40, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 10
    fps = 30
    while not exit_game:
        if game_over:
            with open("hi_score.py","w") as f:
                f.write(str(hi_score))
            gamewindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 10, 230)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
                        

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    

                if event.type == pygame.KEYDOWN:
                    pygame.mixer.music.load("snakegames.mp3")
                    pygame.mixer.music.play()
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score +=1000
                food_x = random.randint(40, screen_width / 2)
                food_y = random.randint(40, screen_height / 2)
                snk_length +=5
                if score>int(hi_score):
                    hi_score = score
            

            gamewindow.fill(white)
            gamewindow.blit(bgimg,(0,0))
            text_screen("Score: " + str(score) + " Hi_score :" + str(hi_score), red, 5, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("gameover.wav")
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("gameover.wav")
                pygame.mixer.music.play()
            plot_snake(gamewindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
 
    pygame.quit()
    quit()
welcome()    
