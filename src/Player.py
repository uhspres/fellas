import pygame
import time
from Character import Character

class Player(Character):
    def __init__(self, image):
        super().__init__(140, 225, image)
        parab = 0;
        self.frames = [self.image,
                       pygame.transform.scale(
                           pygame.image.load("../res/img/ryankick.png"), (140,225)),
                                pygame.transform.scale(
                                    pygame.image.load("../res/img/ryanpunch.png"), (140,225))]
        self.animating = False
        self.startTime = 0
        self.animationDuration = 0
        self.cooldown = 0
    def update(self):
        if self.animating:
            if self.startTime + self.animationDuration < time.time():
                self.animating = False
                self.image = self.frames[0]
        elif self.cooldown > 0:
            self.cooldown -= 1

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



    
    def animate(self, animationIndex, duration):
        if self.animating == False and self.cooldown == 0:
            self.animating = True
            self.startTime = round(time.time())
            self.animationDuration = duration/500
            self.image = self.frames[animationIndex]
            self.cooldown = 2

    
    def punch(self):
        self.animate(1, 1)
        self.soundPlayer.play("woosh.ogg")

    def kick(self):
        self.animate(2, 1)
        self.soundPlayer.play("woosh.ogg")
