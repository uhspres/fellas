import pygame

class StateHandler:
    def __init__(self, state):
        self.state = state

    def changeState(self, newState):
        self.state = newState

    def update(self):
        self.state.update()
