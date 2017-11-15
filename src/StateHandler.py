import pygame
from Battle import Battle

class StateHandler:
    def __init__(self):
        self.stage = 0 # the current game stage is 0
    #TODO: add a list of states like world, titlescreen etc so that when the class
    # is pass by reference, it can just be called easily
    def configStates(self, titleScreen, battleScreen, deathScreen, winScreen):
        self.title = titleScreen
        self.battle = battleScreen
        self.death = deathScreen
        self.win = winScreen
        self.state = self.title

    def changeState(self, newState): # base function
        self.state = newState

    def update(self):
        self.state.update()
        
    def goToTitleScreen(self):
        self.changeState(self.title)

    def goToBattle(self):
        self.changeState(self.battle)

    def goToDeathScreen(self):
        self.stage = 0
        self.changeState(self.death)

    def goToWinScreen(self):
        self.changeState(self.win)
        self.stage += 1

    def newGame(self):
        self.battle = Battle(self)
