import pygame
from sys import exit

startTime = 0

def display_score(): 
    # mainFont = pygame.font.Font("font\Pixeltype.ttf", 50)
    curTime = (pygame.time.get_ticks()) // 1000 - startTime
    scoreSurface = mainFont.render("SCORE: " + str(curTime), False, (64, 64, 64))
    scoreRectangle = scoreSurface.get_rect(center=(screen.get_width()//2, 50))
    screen.blit(scoreSurface, scoreRectangle)

pygame.init() 

# Font 
mainFont = pygame.font.Font("font\Pixeltype.ttf", 50)

pygame.display.set_caption("Learning Pygame Again")
screen = pygame.display.set_mode((800, 400))

# Used to control the frame rate 
clock = pygame.time.Clock() 



groundSurface = pygame.image.load("graphics\ground.png").convert()
skySurface = pygame.image.load("graphics\Sky.png").convert()

# scoreSurface = mainFont.render("SCORE: ", False, (64, 64, 64))
# scoreRectangle = scoreSurface.get_rect(center = (screen.get_width() // 2, 50))

snailSurface = pygame.image.load("graphics\snail\snail1.png").convert_alpha()
snailRectangle = snailSurface.get_rect(midbottom = (600, 300))


playerSurface = pygame.image.load("graphics\player\player_stand.png").convert_alpha()
playerRectangle = playerSurface.get_rect(midbottom = (80, 300)) 
playerGravity = 0 # Implementing Gravity

# Game States 
gameActive = True 



while True: 
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

        if gameActive: 
            # KEYBOARD INPUTS
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE and playerRectangle.bottom >= 300: 
                    # print("Space")
                    playerGravity = -20
            
            # if event.type == pygame.KEYUP: 
            #     print("Key up")

            
            
            # Checking if I clicked on the player 
            if event.type == pygame.MOUSEBUTTONDOWN and playerRectangle.bottom >= 300: 
                if(playerRectangle.collidepoint(event.pos)): 
                    playerGravity = -20
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameActive = True
                snailRectangle.left = screen.get_width() + 5
                startTime = (pygame.time.get_ticks()) // 1000   
    
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

    if gameActive: 
        # Drawing the sky 
        screen.blit(skySurface, (0, 0)) # blit stands for block image transfer

        # Drawing the ground 
        screen.blit(groundSurface, (0, 300))

        # Adding the text 
        # pygame.draw.rect(screen, "#c0e8ec", scoreRectangle, 10) # Draws border around text 
        # pygame.draw.rect(screen, "#c0e8ec", scoreRectangle) # Fills the border 
        # screen.blit(scoreSurface, scoreRectangle)
        display_score()

        # SNAIL 
        snailRectangle.x -= 4 
        if snailRectangle.right < 0 - snailSurface.get_width() - 5: 
            # snailRectangle.left = screen.get_width() + snailSurface.get_width() + 5 
            snailRectangle.left = screen.get_width()
        
        screen.blit(snailSurface, snailRectangle)

        # PLAYER 
        playerGravity += 1
        playerRectangle.y += playerGravity
        # Making sure that the player doesn't go through the floor
        if(playerRectangle.bottom > 300):
            playerRectangle.bottom = 300
        screen.blit(playerSurface, playerRectangle)

        # Collision between player and snail 
        if playerRectangle.colliderect(snailRectangle): 
            gameActive = False
    else:
        screen.fill("yellow")

    # update everything 
    pygame.display.update() 
    clock.tick(60)