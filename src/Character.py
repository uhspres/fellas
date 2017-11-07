import pygame

# Character class inherits from the pygame sprite class
class Character(pygame.sprite.Sprite):

    def __init__(self, width, height, image):
        super().__init__() # call the super constructor

        # configure the image
        self.image = pygame.image.load("../res/img/" + image)
        #self.image.set_colorkey(key)

        # return the rect
        self.rect = self.image.get_rect()

        self.rect.x = 30
        self.rect.y = 30
        
    def move(self, deltaX, deltaY):
        self.rect.x += deltaX
        self.rect.y += deltaY
            
        
        

        
