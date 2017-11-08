import pygame
from abc import ABCMeta, abstractmethod

# abstract class for all gamestates
class GameState:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def update(self): pass
