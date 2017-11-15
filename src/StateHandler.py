import pygame
from Battle import Battle

class StateHandler:
    #TODO: add a list of states like world, titlescreen etc so that when the class
    # is pass by reference, it can just be called easily
    def configStates(self, titleScreen, battleScreen, deathScreen):
        self.title = titleScreen
        self.battle = battleScreen
        self.death = deathScreen
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
        self.changeState(self.death)

    def newGame(self):
        self.battle = Battle(self)
