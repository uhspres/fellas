# Fellas... the game
import pygame
import sys
from Player import Player
from Enemy import Enemy

# game state imports
from StateHandler import StateHandler
from TitleScreen import TitleScreen
from DeathScreen import DeathScreen
from WinScreen import WinScreen
from FinalWin import FinalWin
from Battle import Battle
from Cutscene import Cutscene

#sound
from SoundPlayer import SoundPlayer

pygame.init() # initialize pygame



# configure the display
winSize = (800,600) # window size
screen = pygame.display.set_mode(winSize)
pygame.display.set_caption("Fellas... the game")

# variables for the game loop
running = True
clock = pygame.time.Clock()

# main state handler
stateHandler = StateHandler()

# initial states
firstState = TitleScreen(stateHandler)
battleState = Battle(stateHandler)
deathState = DeathScreen(stateHandler)
winState = WinScreen(stateHandler)
finalWin = FinalWin(stateHandler)
soundPlayer = SoundPlayer()

if sys.argv[1] == "hmmmmm":
    soundPlayer.play("dope.ogg")
else:
    soundPlayer.play("mountain_king.ogg")


stateHandler.configStates(firstState, battleState, deathState, winState, finalWin) # configure the statehandler

while running:

    for event in pygame.event.get(): # loop through the events
        if event.type == pygame.QUIT: # user quit?
            running = False # set the exit flag

    keys = pygame.key.get_pressed()

    stateHandler.update()
    

    clock.tick(60)

pygame.quit()
