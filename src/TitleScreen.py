import pygame
from GameState import GameState

class TitleScreen(GameState):
	def __init__(self, stateHandler):
		self.stateHandler = stateHandler
	def update(self):
		logo = pygame.image.load("/Users/Goose/Documents/GitHub/fellas/res/img/Fellas1.png")
		white = (255, 255, 255)
		self.screen.fill(white)
		self.screen.blit(logo, (200, 25))
		pygame.draw.rect(self.screen, (100, 100, 200), (250, 200, 300, 90))
		pygame.draw.rect(self.screen, (100, 100, 200), (250, 350, 300, 90))
		pygame.draw.rect(self.screen, (100, 100, 200), (250, 500, 300, 90))
		pygame.display.flip()