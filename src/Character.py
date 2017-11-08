import pygame

# Character class inherits from the pygame sprite class
class Character(pygame.sprite.Sprite):
    def __init__(self, width, height, image):
        super().__init__() # call the super constructor

        # -- sprite configuration -- 
        # configure the image
        self.image = pygame.image.load("../res/img/" + image)
        self.image = pygame.transform.scale(self.image, (width, height))
        #self.image.set_colorkey(key)

        # return the rect
        self.rect = self.image.get_rect()

        self.rect.x = 30
        self.rect.y = 30

        # -- physics configuration --
        self.jumping = False # jump when true
        self.velocity = 5 # character's velocity
        self.mass = 1 # character's mass
        
        
    def move(self, deltaX, deltaY): # move character
        self.rect.x += deltaX
        self.rect.y += deltaY

    def jump(self): # set jumping flag
        self.jumping = True
        # actual jumping stuff is implemented by the sublclasses
            
        
        

        
