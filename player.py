#!/usr/bin/env python

try:
    import os
    import pygame
    from resources import *
except ImportError, err:
    print "cannot load module(s)"
    sys.exit(2)  

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("player.png")
        self.speed = 0.02
        self.displacement = [0, 0]
        self.rect.top = 320
        self.rect.left = 320
        self.state = "idle"
        
    def update(self):
        if self.state == "idle":
            self.displacement = self.displacement
        else:            
            if self.state == "moving_up":
                self.displacement[1] = self.displacement[1] - self.speed
            if self.state == "moving_right":
                self.displacement[0] = self.displacement[0] + self.speed  
            if self.state == "moving_down":
                self.displacement[1] = self.displacement[1] + self.speed    
            if self.state == "moving_left":
                self.displacement[0] = self.displacement[0] - self.speed
            if self.state == "stopping_up":
                s = self.rect.top % 32
                self.displacement[1] = self.displacement[1] - s
                self.state = "idle"
            if self.state == "stopping_right":
                s = (pygame.display.get_surface().get_rect().width - (self.rect.left + self.rect.width)) % 32
                self.displacement[0] = self.displacement[0] + s
                self.state = "idle"
            if self.state == "stopping_down":
                s = (pygame.display.get_surface().get_rect().height - (self.rect.top + self.rect.width)) % 32
                self.displacement[1] = self.displacement[0] - s
                self.state = "idle"
            if self.state == "stopping_left":
                s = self.rect.left % 32
                self.displacement[0] = self.displacement[0] - s
                self.state = "idle"
            new_position = self.rect.move(self.displacement)
            self.rect = new_position
