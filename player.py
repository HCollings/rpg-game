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
        self.speed = 400.0
        #player position relative to screen
        self.position = [0, 0]
        #player position relative to map
        self.location = [0, 0]
        self.movement_cooldown = 0.0
        self.movement_limit = 0.16
        self.directions_blocked = {}
        self.health = 100.0
        self.mana = 0.0
        self.state = "idle"
        
    def update(self):
        #movement
        x, y = self.get_position()
        self.rect.top = y
        self.rect.left = x
        if self.health == 0.0:
            self.die()

    def get_position(self):
        x = int(self.position[0])
        y = int(self.position[1])
        return x, y

    def get_coordinates(self):
        x = int(self.location[0]) / 64
        y = int(self.location[1]) / 64
        return x, y

    def move(self, direction):
        if not self.directions_blocked["up"]:
            if direction == "up":
                self.state = "moving_up"
                self.position[1] -= self.speed * self.movement_limit
                self.state = "idle"
        if not self.directions_blocked["right"]:
            if direction == "right":
                self.state = "moving_right"
                self.position[0] += self.speed * self.movement_limit
                self.state = "idle"
        if not self.directions_blocked["down"]:
            if direction == "down":
                self.state = "moving_down"
                self.position[1] += self.speed * self.movement_limit
                self.state = "idle"
        if not self.directions_blocked["left"]:
            if direction == "left":
                self.state = "moving_left"
                self.position[0] -= self.speed * self.movement_limit
                self.state = "idle"

    def modify_health(self, modifier):
        self.health += modifier
        if self.health < 0.0:
            self.health = 0.0
        if self.health > 100.0:
            self.health = 100.0        

    def modify_mana(self, modifier):
        self.mana += modifier
        if self.mana < 0.0:
            self.mana = 0.0
        if self.mana > 100.0:
            self.mana = 100.0

    def die(self):
        self.kill()
