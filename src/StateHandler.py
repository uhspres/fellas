import pygame

class StateHandler:
    #TODO: add a list of states like world, titlescreen etc so that when the class
    # is pass by reference, it can just be called easily
    def changeState(self, newState):
        self.state = newState

    def update(self):
        self.state.update()
