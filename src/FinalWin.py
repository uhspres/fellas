import pygame
from GameState import GameState

class FinalWin(GameState):
    def __init__(self, stateHandler):
        self.stateHandler = stateHandler
        self.screen = pygame.display.set_mode((800,600))
        self.background = pygame.transform.scale(pygame.image.load("../res/img/winscreen.png"), (800, 600))

    def update(self):
        self.screen.blit(self.background, (0,0))

        pygame.display.flip()
