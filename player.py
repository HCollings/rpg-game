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
        #player position relative to screen
        self.position = [0, 0]
        #player position relative to map
        self.location = [0, 0]
        self.state = "idle"
        self.top = self.rect.top
        self.right = self.rect.left + self.rect.width
        self.bottom = self.rect.top + self.rect.height
        self.left = self.rect.left
        self.movement_cooldown = 0.0
        self.movement_limit = 0.16
        
    def update(self):
        #movement
        x, y = self.get_position()
        self.rect.top = y
        self.rect.left = x
        #collisions

    def get_position(self):
        x = int(self.position[0])
        y = int(self.position[1])
        return x, y

    def get_coordinates(self):
        x = int(self.position[0]) / 32
        y = int(self.position[1]) / 32
        return x, y

    def move(self, direction, dt):
        if direction == "up":
            self.position[1] -= self.speed * self.movement_limit
        if direction == "right":
            self.position[0] += self.speed * self.movement_limit
        if direction == "down":
            self.position[1] += self.speed * self.movement_limit
        if direction == "left":
            self.position[0] -= self.speed * self.movement_limit
