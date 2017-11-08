import pygame
from GameState import GameState
from Player import Player
from Enemy import Enemy

class Battle(GameState):
    def __init__(self):
        self.PERFECT_COLOR = (255,0,128)
        self.screen = pygame.display.set_mode((800,600))
        # sprite list
        self.sprites = pygame.sprite.Group()

        # testing stuff
        self.testCharacter = Player("ryan.png")
        self.testEnemy = Enemy("mm_phil.png", 100, 100, self.testCharacter)
        self.sprites.add(self.testCharacter)
        self.sprites.add(self.testEnemy)
    
    def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.testCharacter.move(-3,0)
            elif keys[pygame.K_d]:
                self.testCharacter.move(3,0)
            if keys[pygame.K_SPACE]:
                self.testCharacter.jump()

            # attack
            if keys[pygame.K_j]:
                self.testCharacter.punch()
        
            # update sprites
            self.testCharacter.update()
            self.testEnemy.update()
            
            self.screen.fill(self.PERFECT_COLOR)

            self.sprites.draw(self.screen)
    
    
            pygame.display.flip() # flip the buffers
