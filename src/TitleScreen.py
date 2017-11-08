import pygame
from GameState import GameState

class TitleScreen(GameState):
    def __init__(self, stateHandler):
        self.stateHandler = stateHandler
    def update(self):
        print("TitleScreen")
