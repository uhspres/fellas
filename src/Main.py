# Fellas... the game
import pygame
from Player import Player
from Enemy import Enemy

pygame.init() # initialize pygame

PERFECT_COLOR = (255,0,128)

# configure the display
winSize = (800,600) # window size
screen = pygame.display.set_mode(winSize)
pygame.display.set_caption("Fellas... the game")

# sprite list
sprites = pygame.sprite.Group()

# testing stuff
testCharacter = Player("ryan.png")
testEnemy = Enemy("mm_phil.png", 100, 100, testCharacter)

sprites.add(testCharacter)
sprites.add(testEnemy)

# variables for the game loop
running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get(): # loop through the events
        if event.type == pygame.QUIT: # user quit?
            running = False # set the exit flag


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        testCharacter.move(-3,0)
    elif keys[pygame.K_d]:
        testCharacter.move(3,0)
    if keys[pygame.K_SPACE]:
        testCharacter.jump()

    # attack
    if keys[pygame.K_j]:
        testCharacter.punch()
        
    # update sprites
    testCharacter.update()
    testEnemy.update()
    
    screen.fill(PERFECT_COLOR)

    sprites.draw(screen)
    
    
    pygame.display.flip() # flip the buffers
    clock.tick(60)

pygame.quit()
