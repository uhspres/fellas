# Fellas... the game
import pygame
from Player import Player
from Enemy import Enemy

from StateHandler import StateHandler
from TitleScreen import TitleScreen
from Battle import Battle

pygame.init() # initialize pygame



# configure the display
winSize = (800,600) # window size
screen = pygame.display.set_mode(winSize)
pygame.display.set_caption("Fellas... the game")

#sprites.add(testCharacter)
#sprites.add(testEnemy)

# variables for the game loop
running = True
clock = pygame.time.Clock()
firstState = TitleScreen()
stateHandler = StateHandler(firstState)

while running:

    for event in pygame.event.get(): # loop through the events
        if event.type == pygame.QUIT: # user quit?
            running = False # set the exit flag

    keys = pygame.key.get_pressed()
    if keys[pygame.K_v]:
        newState = Battle()
        stateHandler.changeState(newState)
    stateHandler.update()
    

    clock.tick(60)

pygame.quit()
