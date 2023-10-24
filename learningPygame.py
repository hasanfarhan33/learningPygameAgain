import pygame
from sys import exit

pygame.init() 

pygame.display.set_caption("Learning Pygame Again")
screen = pygame.display.set_mode((800, 400))

# Used to control the frame rate 
clock = pygame.time.Clock() 

# Font 
mainFont = pygame.font.Font("font\Pixeltype.ttf", 50)

groundSurface = pygame.image.load("graphics\ground.png")
skySurface = pygame.image.load("graphics\Sky.png")
textSurface = mainFont.render("Learning Pygame", False, "black")

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit() 
    
    # draw all elements 
    '''
    Surface 

    There are two types of surfaces - display surface and regular surface 

    Display surface - The game window. 
    
    Regular surface - Essentially a single image, needs to be put on display 
    surface to be visible.
    
    Pygame draws the surfaces in order. Ground is drawn on top of the Sky. 
    '''

    '''
    Adding text in Pygame 

    Every time you want to create text, you create an image of the text 
    and then add it to the surface. 

    THREE important steps 
    1. Font 
    2. Write text on surface 
    3. Blit the surface 
    '''

    # Drawing the sky 
    screen.blit(skySurface, (0, 0)) # blit stands for block image transfer

    # Drawing the ground 
    screen.blit(groundSurface, (0, 300))

    # Adding the text 
    screen.blit(textSurface, (300, 50))

    # update everything 
    pygame.display.update() 
    clock.tick(60)