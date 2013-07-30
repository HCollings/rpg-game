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
        self.tile_size = 32
        self.tiles = []
        for i in range (0, image_width / self.tile_size):
            rect = (i * self.tile_size, 0, self.tile_size, self.tile_size)
            self.tiles.append(level.subsurface(rect))
    
    def load_map(self, level_name, level_key):

        self.map = []        
        level_path = os.path.join("levels", level_name)
        level_file = open(level_path, "r")
        self.map = level_file.read().split("\n")
        level_file.close()
        
        self.key = {}
        key_path = os.path.join("levels", level_key)
        parser = ConfigParser.ConfigParser()
        parser.read(key_path)
        for section in parser.sections():
            tile_desc = dict(parser.items(section))
            self.key[section] = tile_desc
        self.width = len(self.map[0])
        self.height = len(self.map)

        self.actual_width = self.width * self.tile_size
        self.actual_height = self.height * self.tile_size
        
    def render(self):
        image = pygame.Surface((self.actual_width, self.actual_height)) 
        for y, line in enumerate(self.map):
            for x, tile in enumerate(line):
                tile = self.key[tile]
                try:
                    tile_id = int(tile["id"])
                except (ValueError, KeyError):
                    tile_id = int(0)
                tile_image = self.tiles[tile_id]
                image.blit(tile_image, (x * self.tile_size, y * self.tile_size))
        return image, image.get_rect()
                    

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("player.png")

        self.v = 10.0
        self.pos = [0, 0]
        self.rect.top = 400
        self.rect.left = 400
        self.moving_up = False
        self.moving_right = False
        self.moving_down = False
        self.moving_left = False

    def update(self, dt):
        if self.moving_up:
            self.pos[1] = self.pos[1] - (self.v * dt)
        if self.moving_right:
            self.pos[0] = self.pos[0] + (self.v * dt)   
        if self.moving_down:
            self.pos[1] = self.pos[1] + (self.v * dt)    
        if self.moving_left:
            self.pos[0] = self.pos[0] - (self.v * dt)
        new_pos = self.rect.move(self.pos)
        self.rect = new_pos
