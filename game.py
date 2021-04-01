import pygame
import time
import random
from graphTool import returnDirection, score
#start lib
pygame.init()

#define constants
GREEN   = ( 0, 255, 0)
BLACK = ( 0, 0, 0)
RED = (255, 0, 0)
width = 1600
height = 900
font_style = pygame.font.SysFont(None, 50)
block_size = 10

#set display and title 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

#set clock
clock = pygame.time.Clock()

#functions
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    text_width, text_height = font_style.size(msg)
    screen.blit(mesg, [(width - text_width)/2, (height - text_height)/2])

def game_loop():
    active = True
    snake = []
    snake.append([(width/20)*10,(height/20)*10])

    xDirection = 0
    yDirection = 0

    eaten = False

    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while active:
        #user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    xDirection = 10
                    yDirection = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    xDirection = -10
                    yDirection = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    xDirection = 0
                    yDirection = -10
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    xDirection = 0
                    yDirection = 10
        #get direction from graph         
        xDirection, yDirection = returnDirection(yDirection, width, height, foodx, foody, snake)
        print("snake=(",snake[0][0], "|", snake[0][1], "),score=",score(snake[0][0], snake[0][1], width, height) ,", apple=(", foodx, "|", foody,") =>", xDirection, "|", yDirection, sep="")   
        #game logic
        #loose game
        if(snake[0][0] < 0 or snake[0][0] >= width or snake[0][1] < 0 or snake[0][1] >= height):
            active = False
            break
        if(len(snake) > 1):
            for index in range(1, len(snake), +1):
                if (snake[0][0] == snake[index][0] and snake[0][1] == snake[index][1]):
                    active = False
                    break
        #eat apple
        if(snake[0][0] == foodx and snake[0][1] == foody):
            foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            snake.append([0,0])

        if(len(snake) > 1):
            for index in range(len(snake)-1,-1,-1):
                if(index > 0):
                    snake[index][0] = snake[index-1][0]
                    snake[index][1] = snake[index-1][1]
                else:
                    snake[0][0] += xDirection
                    snake[0][1] += yDirection
        else:
            snake[0][0] += xDirection
            snake[0][1] += yDirection
        #reset screen 
        screen.fill(BLACK)
        #draw screen
        for row in snake:
            pygame.draw.rect(screen,GREEN,[row[0],row[1],10,10])
        pygame.draw.rect(screen, RED, [foodx, foody, 10, 10])
        #reset window
        pygame.display.flip()
        #refresh time
        clock.tick(120)

    message("You lost, press Q to quit and any other key to try again",RED)
    pygame.display.flip()
    while not active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                else:
                    game_loop()

#start game
game_loop()