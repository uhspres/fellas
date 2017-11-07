# Fellas... the game
import pygame
from Player import Player

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

sprites.add(testCharacter)

# variables for the game loop
running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get(): # loop through the events
        if event.type == pygame.QUIT: # user quit?
            running = False # set the exit flag


            
    screen.fill(PERFECT_COLOR)

    sprites.draw(screen)

    testCharacter.move()
    
    pygame.display.flip() # flip the buffers
    clock.tick(60)

pygame.quit()
