import pygame
from Character import Character

class Enemy(Character):
    def __init__(self, image, w, h, target):
        super().__init__(w,h,image)
        self.height = h
        self.target = target
        self.jumpCooldown = 0
        self.jumpRate = 30

    def update(self):
        # move towards the player
        if self.target.rect.x  > self.rect.x:
            self.move(2.5, 0)
        elif self.target.rect.x < self.rect.y:
            self.move(-2.5, 0)
        
        # random jumping code, just jump constantly
        if not self.jumping and self.jumpCooldown < 0:
            self.jump()
            self.jumpCooldown = self.jumpRate
        else:
            self.jumpCooldown -= 1
        
        # jumping code
        if self.jumping:

            # calculate force for jump
            if self.velocity > 0:
                self.force = (0.5 * self.mass * pow(self.velocity, 2)) # positive force for going up
            else:
                self.force = -(0.5 * self.mass * pow(self.velocity, 2)) # negative force for going down

            self.rect.y -= self.force # add force to the y position
            self.velocity -= 1 # reduce the velocity so that you fall eventually

            # reset physics
            if self.rect.y > 500 - (self.height / 2): # check if player is on the ground
                self.rect.y = 450
                self.jumping = False
                self.velocity = 8
        
