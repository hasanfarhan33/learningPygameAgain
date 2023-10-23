import pygame
from sys import exit

pygame.init() 

pygame.display.set_caption("Learning Pygame Again")
screen = pygame.display.set_mode((800, 400))

# Used to control the frame rate 
clock = pygame.time.Clock() 

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit() 
    
    # draw all elements 
    # update everything 
    pygame.display.update() 
    clock.tick(60)