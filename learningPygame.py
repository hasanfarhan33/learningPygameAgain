import pygame
from sys import exit

pygame.init() 

pygame.display.set_caption("Learning Pygame Again")
screen = pygame.display.set_mode((800, 400))

# Used to control the frame rate 
clock = pygame.time.Clock() 

# Font 
mainFont = pygame.font.Font("font\Pixeltype.ttf", 50)

groundSurface = pygame.image.load("graphics\ground.png").convert()
skySurface = pygame.image.load("graphics\Sky.png").convert()

scoreSurface = mainFont.render("SCORE: ", False, (64, 64, 64))
scoreRectangle = scoreSurface.get_rect(center = (screen.get_width() // 2, 50))

snailSurface = pygame.image.load("graphics\snail\snail1.png").convert_alpha()
snailRectangle = snailSurface.get_rect(midbottom = (600, 300))


playerSurface = pygame.image.load("graphics\player\player_stand.png").convert_alpha()
playerRectangle = playerSurface.get_rect(midbottom = (80, 300)) 


while True: 
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
        
        # Checking if the mouse is over the player rectangle 
        # if event.type == pygame.MOUSEMOTION: 
        #     if(playerRectangle.collidepoint(event.pos)): 
        #         print("Hovering over player")
    
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
    pygame.draw.rect(screen, "#c0e8ec", scoreRectangle, 10) # Draws border around text 
    pygame.draw.rect(screen, "#c0e8ec", scoreRectangle) # Fills the border 
    screen.blit(scoreSurface, scoreRectangle)

    # Drawing a line from top left to bottom right 
    # pygame.draw.line(screen, "Blue", (0, 0), (screen.get_width(), screen.get_height()), 3)

    # Drawing a circle that follows the mouse 
    # pygame.draw.circle(screen, "black", pygame.mouse.get_pos(), 5)

    # Adding the snail 
    # if(snailXPos < 0 - snailSurface.get_width() - 5):
    #     snailXPos = screen.get_width() + snailSurface.get_width()
    # else: 
    #     snailXPos -= 4

    # Better way to animate 
    snailRectangle.x -= 4 
    if snailRectangle.right < 0 - snailSurface.get_width() - 5: 
        # snailRectangle.left = screen.get_width() + snailSurface.get_width() + 5 
        snailRectangle.left = screen.get_width()
    
    # Checking collision between snail and player 
    # if snailRectangle.colliderect(playerRectangle): 
    #     print("Collision has occured")

    # Mouse Functions
    # if(playerRectangle.collidepoint((pygame.mouse.get_pos()))): 
    #     # print("Mouse in player")
    #     leftClick, midClick, rightClick = pygame.mouse.get_pressed()
    #     if leftClick: 
    #         print("Clicked on the player")

    screen.blit(snailSurface, snailRectangle)

    screen.blit(playerSurface, playerRectangle)

    # update everything 
    pygame.display.update() 
    clock.tick(60)