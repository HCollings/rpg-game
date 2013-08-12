#!/usr/bin/env python

try:
    import os
    import sys
    import pygame
    import math
    import resources
except ImportError, err:
    print "cannot load module(s)"
    sys.exit(2)  

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = resources.load_image("player.png")
        self.speed = 400.0
        #player position relative to screen
        self.position = [0, 0]
        #player position relative to map
        self.location = [128, 128]
        self.movement_cooldown = 0.0
        self.movement_limit = 0.16
        self.movement_points = [0, 0, 0, 0] #up, right, down, left
        self.directions_blocked = {}
        self.health = 100.0
        self.mana = 0.0
        self.state = "idle"
        
    def update(self):
        #set rect according to position
        #for other entities the position will be their location relative to map
        x, y = self.get_position()
        self.rect.top = y
        self.rect.left = x
        print self.state
        if self.state != "idle":
            self.animate()
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

    def set_movement_points(self, direction):
        if not self.directions_blocked["up"] and direction == "up":
            self.movement_points[0] = 64
        if not self.directions_blocked["right"] and direction == "right":
            self.movement_points[1] = 64
        if not self.directions_blocked["down"] and direction == "down":
            self.movement_points[2] = 64
        if not self.directions_blocked["left"] and direction == "left":
            self.movement_points[3] = 64

    def animate(self):
        print "Lol"

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
