import pygame
from Character import Character

class Player(Character):
    def __init__(self, image):
        super().__init__(140, 225, image)
        parab = 0;

    def update(self):
        if self.jumping:

            # calculate force for jump
            if self.velocity > 0:
                self.force = (0.5 * self.mass * pow(self.velocity, 2)) # positive force for going up
            else:
                self.force = -(0.5 * self.mass * pow(self.velocity, 2)) # negative force for going down

            self.rect.y -= self.force # add force to the y position
            parab = abs(80/(self.rect.y + .001))

            self.velocity -= 2 * pow(parab, 2) + parab + .01; # reduce the velocity so that you fall eventually
            # reset physics
            if self.rect.y > 350: # check if player is on the ground
                self.rect.y = 350
                self.jumping = False
                self.velocity = 8
        
    def punch(self):
        print("Punch!")
