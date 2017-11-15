import pygame
from GameState import GameState
from Battle import Battle

class WinScreen(GameState):
    def __init__(self, stateHandler):
        self.stateHandler = stateHandler
        self.screen = pygame.display.set_mode((800,600))
    def update(self):
        
        x = 250;

        playagainButton = pygame.image.load("../res/img/playagain.png")
        playagainButtonHover = pygame.image.load("../res/img/playagainhover.png")
        self.background = pygame.image.load("../res/img/winscreen.png")
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.screen.blit(self.background, (0,0))
        self.screen.blit(playagainButton, (x, 150))
        mosx, mosy = pygame.mouse.get_pos();
        if mosx > 260 and mosx < 500 and mosy > 190 and mosy < 306:
            self.screen.blit(playagainButtonHover, (x, 150))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                self.stateHandler.newGame()
                self.stateHandler.goToBattle()
                self.stateHandler.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.stateHandler.newGame()
            self.stateHandler.goToBattle()
            self.stateHandler.update()
            
        pygame.display.flip()
