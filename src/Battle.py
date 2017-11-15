import pygame
from GameState import GameState
from Player import Player
from Enemy import Enemy
import time

class Battle(GameState):
    def __init__(self, stateHandler):
        self.stateHandler = stateHandler
        self.PERFECT_COLOR = (255,0,128)
        self.screen = pygame.display.set_mode((800,600))
        # sprite list
        self.sprites = pygame.sprite.Group()
        self.test = ["ryan.png", "ryankick.png"]
        self.cIndex = 0
        # testing stuff
        self.testCharacter = Player(self.test[self.cIndex])
        self.testEnemy = Enemy("mm_phil.png", 100, 100, self.testCharacter)
        self.background = pygame.image.load("../res/img/world.png")
        self.background = pygame.transform.scale(self.background, (800, 600))
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
                # test code just to test statehandler
            if keys[pygame.K_x]:
                self.cIndex = 1
                self.testCharacter.kill()
                self.testCharacter = Player(self.test[self.cIndex])
                self.sprites.add(self.testCharacter)
                self.testCharacter.update()
            if keys[pygame.K_y]:   
                self.cIndex = 0
                self.testCharacter.kill()
                self.testCharacter = Player(self.test[self.cIndex])
                self.sprites.add(self.testCharacter)
                self.testCharacter.update()
        
            # update sprites
            self.testCharacter.update()
            self.testEnemy.update()
            

            #self.screen.fill(self.PERFECT_COLOR)
            self.screen.blit(self.background, (0,0))
            self.sprites.draw(self.screen)
            self.hitbox()
            pygame.display.flip() # flip the buffers

    def hitbox(self):
        enemyHit = pygame.draw.rect(self.screen, (155, 155, 155), (self.testEnemy.rect.x + 20, self.testEnemy.rect.y, 60, 100), 2)
        if self.cIndex == 1:
            kickHit = pygame.draw.rect(self.screen, (155, 155, 155), (self.testCharacter.rect.x + 20, self.testCharacter.rect.y + 120, 30, 30), 2)
            if(kickHit.colliderect(enemyHit)):
                print("hit")
        else:
            normalHit = pygame.draw.rect(self.screen, (155, 155, 155), (self.testCharacter.rect.x + 20, self.testCharacter.rect.y, 110, 225), 2)






