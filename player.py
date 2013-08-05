#!/usr/bin/env python

try:
    import os
    import sys
    import pygame
    import math
    from resources import *
except ImportError, err:
    print "cannot load module(s)"
    sys.exit(2)  

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("player.png")
        self.speed = 200.0
        self.location = [0, 0]
        self.state = "idle"
        
    def update(self):
        x, y = self.get_position(self.location)
        print x, y
        self.rect.top = y
        self.rect.left = x

    def get_position(self, location):
        x = int(location[0])
        y = int(location[1])
        return x, y   

    def move(self, direction, dt):
        if direction == "up":
            self.location[1] -= self.speed * dt
        if direction == "right":
            self.location[0] += self.speed * dt
        if direction == "down":
            self.location[1] += self.speed * dt
        if direction == "left":
            self.location[0] -= self.speed * dt

