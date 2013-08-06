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
        
    def update(self):
        #movement
        x, y = self.get_position()
        print self.position
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

    def move(self, direction, dt, progress):
        if progress == 0:
            if direction == "up":
                self.position[1] -= self.speed * dt
            if direction == "right":
                self.position[0] += self.speed * dt
            if direction == "down":
                self.position[1] += self.speed * dt
            if direction == "left":
                self.position[0] -= self.speed * dt
        elif progress == 1:
            if direction == "up":
                s = int(self.location[1]) % 32
                self.position[1] -= s
            if direction == "right":
                s = 32 - (int(self.location[0]) % 32)
                t = s / self.speed
                self.move(direction, t, 0)
            if direction == "down":
                s = 32 - (int(self.location[1]) % 32)
                self.position[1] += s
            if direction == "left":
                s = int(self.location[0]) % 32
                self.position[0] -= s
