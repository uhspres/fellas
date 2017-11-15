import pygame
from GameState import GameState
from Player import Player
from Enemy import Enemy

'''
Cutscenes are formated as COMMAND [character] [args (optional)]
Ex: MOVE 1 4 5
would move characters[1] by the vector movement (4,5)
'''

class Cutscene(GameState):
    def __init__(self, stateHandler, background, scene, exitState):
        self.background = pygame.transform.scale(
            pygame.image.load("../res/img/" + background),
            (800,800))
        
        self.stateHandler = stateHandler
        self.scene = scene
        self.exitState = exitState
        

    def update(self):
        index = 0
        for event in self.scene:
            index += 1
            if event == "MOVE": # MOVE <character> <amount x>
                # move characters
                # this.characters[this.scene[index+1]].move(this.scene[index+2])
            elif event == "JUMP": # MOVE <character> <# of times>
                # TODO: jump
                #for x in range(0,this.scene[index+2]):
                    #this.characters[this.scene[index+1]].jump()
            else: # this is arguments
                continue
            
        self.stateHandler.changeState(self.exitState)

