#!/usr/bin/env python

try:
    import os
    import pygame    
    import ConfigParser
    from resources import *
except ImportError, err:
    print "cannot load module(s)"
    sys.exit(2)  

# objects

class Level(object):

    def load_tiles(self, name):
        level, level_rect = load_image(name)
        image_width = level.get_width()
        self.tile_size = 24
        self.tiles = []
        for i in range (0, image_width / self.tile_size):
            rect = (i * self.tile_size, 0, self.tile_size, self.tile_size)
            self.tiles.append(level.subsurface(rect))
    
    def load_map(self, name):
        self.map = []
        self.key = {}
        fullname = os.path.join("levels", name)
        parser = ConfigParser.ConfigParser()
        parser.read(fullname)
        self.map = parser.get("level", "map").split("\n")
        self.key = parser._sections
        print self.key
        self.width = len(self.map[0])
        self.height = len(self.map)        
                
    def get_tile(self, x, y):
        try:
            char = self.map[y][x]
        except IndexError:
            return {}
        try:
            return self.key[char]
        except KeyError:
            return {}
        
    def render(self):
        image = pygame.Surface((self.width*self.tile_size, self.height*self.tile_size))

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("ball.png")
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.speed = 10
        self.movepos = [0, 0]
        self.state = "still"

    def update(self):
        newpos = self.rect.move(self.movepos)
        self.rect = newpos

    def move_up(self):
        self.movepos[1] = self.movepos[1] - (self.speed)
        self.state = "moving"

    def move_down(self):
        self.movepos[1] = self.movepos[1] + (self.speed)
        self.state = "moving"

    def move_left(self):
        self.movepos[0] = self.movepos[0] - (self.speed)
        self.state = "moving"

    def move_right(self):
        self.movepos[0] = self.movepos[0] + (self.speed)
        self.state = "moving"
