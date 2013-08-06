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
        self.top = self.rect.top
        self.right = self.rect.left + self.rect.width
        self.bottom = self.rect.top + self.rect.height
        self.left = self.rect.left
        
    def update(self):
        #movement
        x, y = self.get_position()
        self.rect.top = y
        self.rect.left = x
        #collisions
        self.handle_collisions()

    def handle_collisions(self):
        screen_width = pygame.display.get_surface().get_rect().width
        screen_height = pygame.display.get_surface().get_rect().height
        if self.top < 0:
            self.location[1] = 0
        if self.right > screen_width:
            self.location[0] = screen_width
        if self.bottom > screen_height:
            self.location[1] = screen_height
        if self.left < 0:
            self.location[0] = 0        

    def get_position(self):
        x = int(self.location[0])
        y = int(self.location[1])
        return x, y

    def get_coordinates(self):
        x = int(self.location[0]) / 32
        y = int(self.location[1]) / 32
        return x, y

    def move(self, direction, dt, progress):
        if progress == 0:
            if direction == "up":
                self.location[1] -= self.speed * dt
            if direction == "right":
                self.location[0] += self.speed * dt
            if direction == "down":
                self.location[1] += self.speed * dt
            if direction == "left":
                self.location[0] -= self.speed * dt
        elif progress == 1:
            if direction == "up":
                s = int(self.location[1]) % 32
                self.location[1] -= s
            if direction == "right":
                s = 32 - (int(self.location[0]) % 32)
                self.location[0] += s
            if direction == "down":
                s = 32 - (int(self.location[1]) % 32)
                self.location[1] += s
            if direction == "left":
                s = int(self.location[0]) % 32
                self.location[0] -= s
