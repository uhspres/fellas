import pygame
from GameState import GameState
from Player import Player
from Enemy import Enemy
from SoundPlayer import SoundPlayer
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

        self.testCharacter = Player(self.test[self.cIndex])
        self.testEnemy = Enemy("mm_phil.png", 100, 100, self.testCharacter)
        self.background = pygame.image.load("../res/img/world.png")
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.sprites.add(self.testCharacter)
        self.sprites.add(self.testEnemy)

        self.font = pygame.font.SysFont("monospace", 25)
    def update(self):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                self.testCharacter.move(-5,0)
            elif keys[pygame.K_d]:
                self.testCharacter.move(5,0)
            if keys[pygame.K_SPACE]:
                self.testCharacter.jump()

            # attack
            if keys[pygame.K_j]:
                self.testCharacter.punch()
            if keys[pygame.K_k]:
                self.testCharacter.kick()
            if keys[pygame.K_y]:  # DEBUG KILL ENEMY
                self.testEnemy.health -= 10
        
            # update sprites
            self.testCharacter.update()
            self.testEnemy.update()
            if self.testCharacter.health < 0:
                self.stateHandler.goToDeathScreen()
                
                pygame.display.flip()
                print("lose")
            elif self.testEnemy.health < 0:
                print("Win")
                self.stateHandler.goToWinScreen()
                
                pygame.display.flip()

            #self.screen.fill(self.PERFECT_COLOR)
            self.screen.blit(self.background, (0,0))
            self.sprites.draw(self.screen)
            self.hitbox()
            self.drawHealthBars()
            self.drawStage()
            pygame.display.flip() # flip the buffers


    def hitbox(self):
        enemyHit = pygame.draw.rect(self.screen, (155, 155, 155), (self.testEnemy.rect.x + 20, self.testEnemy.rect.y, 60, 100), 2)
        if self.testCharacter.animating:
            kickHit = pygame.draw.rect(self.screen, (155, 155, 155), (self.testCharacter.rect.x + 20, self.testCharacter.rect.y + 120, 30, 30), 2)
            if(kickHit.colliderect(enemyHit)):
                self.testCharacter.soundPlayer.play("hit.ogg")
                self.testEnemy.health -= 5
                self.testEnemy.rect.x -= 200
        else:
            normalHit = pygame.draw.rect(self.screen, (155, 155, 155), (self.testCharacter.rect.x + 20, self.testCharacter.rect.y, 110, 225), 2)
            if(normalHit.colliderect(enemyHit)):
                self.testCharacter.health -= 5
                self.testCharacter.rect.x += 100


    def drawHealthBars(self):
        # player health
        pygame.draw.rect(self.screen, (0,255,0), (75,30,self.testCharacter.health*2,40))
        # enemy health
        pygame.draw.rect(self.screen, (0,255,0), (530,30,self.testEnemy.health*2,40))

        self.screen.blit(self.font.render("Player", 1, (0,0,128)), (40,3))
        self.screen.blit(self.font.render("Enemy", 1, (0,0,128)), (685,3))

    def drawStage(self):
        self.screen.blit(self.font.render("Stage " + str(self.stateHandler.stage), 1, (0,0,128)), (250, 30))
