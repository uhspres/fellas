import pygame
from Character import Character

class Player(Character):

    def __init__(self, image):
        super().__init__(50, 30, image)
