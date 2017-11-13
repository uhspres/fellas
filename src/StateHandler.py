import pygame

class StateHandler:
    #TODO: add a list of states like world, titlescreen etc so that when the class
    # is pass by reference, it can just be called easily
    def configStates(self, titleScreen, battleScreen):
        self.title = titleScreen
        self.battle = battleScreen
        self.state = self.title
    def changeState(self, newState): # base function
        self.state = newState

    def update(self):
        self.state.update()
        
    def goToTitleScreen(self):
        self.changeState(self.title)

    def goToBattle(self):
        self.changeState(self.battle)
