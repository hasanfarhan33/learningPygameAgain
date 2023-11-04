import random
import pygame
from sys import exit
from random import randint, choice

from pygame.sprite import AbstractGroup

startTime = 0
score = 0

# Pygame doesn't load sprites automatically
# Have to create sprite -> place in group or group single -> draw/update sprites in that group

# Sprite has two main functions
# Drawing all the sprites
# Update all the sprites
# Sprites have their own collision mechanics


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        playerWalk1Surface = pygame.image.load(
            "graphics\player\player_walk_1.png").convert_alpha()

        playerWalk2Surface = pygame.image.load(
            "graphics\player\player_walk_2.png").convert_alpha()

        # For animating the player
        self.playerWalk = [playerWalk1Surface, playerWalk2Surface]
        self.playerIndex = 0
        self.playerSurface = self.playerWalk[self.playerIndex]
        self.playerJump = pygame.image.load(
            "graphics/player/jump.png").convert_alpha()

        self.image = self.playerWalk[self.playerIndex]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0
        self.jumpSound = pygame.mixer.Sound("audio/jump.mp3")
        self.jumpSound.set_volume(0.5)

    # Player input
    def playerInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -22
            self.jumpSound.play()

    def applyGravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animatePlayer(self):
        if self.rect.bottom < 300:
            self.image = self.playerJump
        else:
            self.playerIndex += 0.1
            if self.playerIndex >= len(self.playerWalk):
                self.playerIndex = 0
            self.image = self.playerWalk[int(self.playerIndex)]

    def update(self):
        self.playerInput()
        self.applyGravity()
        self.animatePlayer()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'fly':
            fly_1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
            fly_2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load(
                "graphics/snail/snail1.png").convert_alpha()
            snail_2 = pygame.image.load(
                "graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animationIndex = 0
        self.image = self.frames[self.animationIndex]
        self.rect = self.image.get_rect(
            midbottom=(random.randint(900, 1100), y_pos))

    def animateObstacle(self):
        self.animationIndex += 0.1
        if self.animationIndex >= len(self.frames):
            self.animationIndex = 0
        self.image = self.frames[int(self.animationIndex)]

    def update(self):
        self.animateObstacle()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


def collisionSprite():
    # spritecollide(sprite, group, dokill)
    if pygame.sprite.spritecollide(player.sprite, obstacleGroup, False):
        obstacleGroup.empty()
        return False
    else:
        return True


def display_score():
    # mainFont = pygame.font.Font("font\Pixeltype.ttf", 50)
    curTime = (pygame.time.get_ticks()) // 1000 - startTime
    scoreSurface = mainFont.render(
        "SCORE: " + str(curTime), False, (64, 64, 64))
    scoreRectangle = scoreSurface.get_rect(center=(screen.get_width()//2, 50))
    screen.blit(scoreSurface, scoreRectangle)
    return curTime


def obstacle_movement(obstacleList):
    if obstacleList:
        for obstacleRect in obstacleList:
            obstacleRect.x -= 3

            if obstacleRect.bottom == 300:
                screen.blit(snailSurface, obstacleRect)
            elif obstacleRect.bottom == 200:
                screen.blit(flySurface, obstacleRect)

        obstacleList = [
            obstacle for obstacle in obstacleList if obstacle.x > -100]

        return obstacleList
    else:
        return []


def player_animation():
    global playerSurface, playerIndex
    if playerRectangle.bottom < 300:
        playerSurface = playerJumpSurface
    else:
        playerIndex += 0.1
        if playerIndex >= len(playerWalk):
            playerIndex = 0
        playerSurface = playerWalk[int(playerIndex)]

    # Play walking animation if the player is on the floor

    # Play the jump animation if the player is in the air


def collision(player, obstacleList):
    if obstacleList:
        for obstacleRect in obstacleList:
            if player.colliderect(obstacleRect):
                return False
    return True


pygame.init()

# Music
backgroundMusic = pygame.mixer.Sound("audio/music.wav")
backgroundMusic.set_volume(0.5)
backgroundMusic.play(loops=-1)

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

# PLAYER
player = pygame.sprite.GroupSingle()
player.add(Player())

# OBSTACLES
obstacleGroup = pygame.sprite.Group()

# ENEMIES
# Snail
snailFrame1 = pygame.image.load("graphics\snail\snail1.png").convert_alpha()
snailFrame2 = pygame.image.load("graphics\snail\snail2.png").convert_alpha()
snailFrames = [snailFrame1, snailFrame2]
snailIndex = 0
snailSurface = snailFrames[snailIndex]

# Fly
flyFrame1 = pygame.image.load("graphics\Fly\Fly1.png").convert_alpha()
flyFrame2 = pygame.image.load("graphics\Fly\Fly2.png").convert_alpha()
flyFrames = [flyFrame1, flyFrame2]
flyIndex = 0
flySurface = flyFrames[flyIndex]

obstacleRectList = []

playerWalk1Surface = pygame.image.load(
    "graphics\player\player_walk_1.png").convert_alpha()
# playerRectangle = playerWalk1Surface.get_rect(midbottom=(80, 300))

playerWalk2Surface = pygame.image.load(
    "graphics\player\player_walk_2.png").convert_alpha()

# For animating the player
playerWalk = [playerWalk1Surface, playerWalk2Surface]
playerIndex = 0
playerSurface = playerWalk[playerIndex]

playerJumpSurface = pygame.image.load("graphics\player\jump.png")

playerRectangle = playerWalk1Surface.get_rect(midbottom=(80, 300))


# Intro Screen
playerStandSurface = pygame.image.load(
    "graphics\player\player_stand.png").convert_alpha()
playerStandSurface = pygame.transform.rotozoom(playerStandSurface, 0, 2)
playerStandRectangle = playerStandSurface.get_rect(
    center=(screen.get_width() // 2, screen.get_height() // 2))


playerGravity = 0  # Implementing Gravity


# Game Title
gameTitleSurface = mainFont.render(
    "Jumpy Boi", False, (111, 196, 169)).convert_alpha()
# gameTitleSurface = pygame.transform.rotozoom(gameTitleSurface, 0, 1.5)
gameTitleRectangle = gameTitleSurface.get_rect(
    center=(screen.get_width() // 2, 50))

# Press Space to Start
spaceToStartSurface = mainFont.render(
    "PRESS SPACE TO START", False, (111, 196, 169)).convert_alpha()
# spaceToStartSurface = pygame.transform.rotozoom(spaceToStartSurface, 0, 1.5)
spaceToStartSurfaceRectangle = spaceToStartSurface.get_rect(
    center=(screen.get_width() // 2, 350))


# Game States
gameActive = False


# Timer - MUST add +1 to each event
obstacleTimer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacleTimer, 1500)

snailAnimationTimer = pygame.USEREVENT + 2
pygame.time.set_timer(snailAnimationTimer, 500)

flyAnimationTimer = pygame.USEREVENT + 3
pygame.time.set_timer = (flyAnimationTimer, 200)

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
                if (playerRectangle.collidepoint(event.pos)):
                    playerGravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameActive = True
                startTime = (pygame.time.get_ticks()) // 1000

        if gameActive:
            if event.type == obstacleTimer:
                obstacleGroup.add(
                    Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

                '''
                if randint(0, 2):
                    obstacleRectList.append(snailSurface.get_rect(
                        bottomright=(randint(900, 1100), 300)))
                else:
                    obstacleRectList.append(flySurface.get_rect(
                        bottomright=(randint(900, 1100), 200)))'''

            if event.type == snailAnimationTimer:
                if snailIndex == 0:
                    snailIndex = 1
                else:
                    snailIndex = 0

                snailSurface = snailFrames[snailIndex]

            if event.type == flyAnimationTimer:
                if flyIndex == 0:
                    flyIndex = 1
                else:
                    flyIndex = 0

                flySurface = flyFrames[flyIndex]

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
        screen.blit(skySurface, (0, 0))  # blit stands for block image transfer

        # Drawing the ground
        screen.blit(groundSurface, (0, 300))

        # Adding the text
        # pygame.draw.rect(screen, "#c0e8ec", scoreRectangle, 10) # Draws border around text
        # pygame.draw.rect(screen, "#c0e8ec", scoreRectangle) # Fills the border
        # screen.blit(scoreSurface, scoreRectangle)
        score = display_score()

        # SNAIL
        # snailRectangle.x -= 4
        # if snailRectangle.right < 0 - snailSurface.get_width() - 5:
        #     # snailRectangle.left = screen.get_width() + snailSurface.get_width() + 5
        #     snailRectangle.left = screen.get_width()

        # screen.blit(snailSurface, snailRectangle)

        # PLAYER
        # playerGravity += 1
        # playerRectangle.y += playerGravity
        # # Making sure that the player doesn't go through the floor
        # if (playerRectangle.bottom > 300):
        #     playerRectangle.bottom = 300
        # player_animation()
        # screen.blit(playerSurface, playerRectangle)

        player.draw(screen)
        player.update()

        obstacleGroup.draw(screen)
        obstacleGroup.update()

        # Obstacle Movement
        # obstacleRectList = obstacle_movement(obstacleRectList)

        # Collision
        gameActive = collisionSprite()
        # gameActive = collision(playerRectangle, obstacleRectList)

    else:
        obstacleRectList.clear()
        playerRectangle.midbottom = (80, 300)
        playerGravity = 0
        screen.fill((94, 129, 162))

        # Player
        screen.blit(playerStandSurface, playerStandRectangle)

        # Game Title
        # pygame.draw.rect(screen, "#c0e8ec", gameTitleRectangle, 10)
        # pygame.draw.rect(screen, "#c0e8ec", gameTitleRectangle)
        screen.blit(gameTitleSurface, gameTitleRectangle)

        # Space to Start
        # pygame.draw.rect(screen, (64, 64, 64), spaceToStartSurfaceRectangle, 10)
        # pygame.draw.rect(screen, (64, 64, 64), spaceToStartSurfaceRectangle)
        if score != 0:
            scoreMessageSurface = mainFont.render(
                "Your score: " + str(score), False, (111, 196, 169))
            scoreMessageRectangle = scoreMessageSurface.get_rect(
                center=(screen.get_width() // 2, 350))
            screen.blit(scoreMessageSurface, scoreMessageRectangle)
        else:
            screen.blit(spaceToStartSurface, spaceToStartSurfaceRectangle)

    # update everything
    pygame.display.update()
    clock.tick(60)
