import pygame
from GameState import GameState
from Battle import Battle

class TitleScreen(GameState):
    def __init__(self, stateHandler):
        self.stateHandler = stateHandler
        self.screen = pygame.display.set_mode((800,600))
    def update(self):
        x = 250;
        logo = pygame.image.load("../res/img/Fellas1.png")
        logo = pygame.transform.scale(logo, (350, 130))
        playButton = pygame.image.load("../res/img/playButton.png")
        playButtonHover = pygame.image.load("../res/img/playButtonHover.png")
        exitButton = pygame.image.load("../res/img/exitButton.png")
        exitButtonHover = pygame.image.load("../res/img/exitButtonHover.png")
        white = (255, 255, 255)
        self.screen.fill(white)
        self.screen.blit(logo, (225, 25))
        self.screen.blit(playButton, (x, 100))
        self.screen.blit(exitButton, (x, 200))
        mosx, mosy = pygame.mouse.get_pos();
        if mosx > 260 and mosx < 500 and mosy > 190 and mosy < 266:
            self.screen.blit(playButtonHover, (x, 100))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                print("haha")
                exit()
        if mosx > 260 and mosx < 500 and mosy > 290 and mosy < 366:
            self.screen.blit(exitButtonHover, (x, 200))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                exit()
        pygame.display.flip()