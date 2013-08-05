#!/usr/bin/env python

try:
    import os
    import pygame    
    import ConfigParser
    from resources import *
except ImportError, err:
    print "cannot load module(s)"
    sys.exit(2)  

class Level:

    def __init__(self, level_name = "", level_key = ""):
        #map is stored in a 2d array
        self.map = []
        #the key finds the corresponding tile according to map character
        self.key = {}
        #os independant file paths
        self.level_path = os.path.join("src", level_name)
        self.key_path = os.path.join("src", level_key)

    def load_tiles(self, name):
        #load the tileset
        level, level_rect = load_image(name)
        image_width = level.get_width()
        self.tile_size = 32
        self.tiles = []
        #cut each tile from the tileset and append to an array for later use
        for i in range (0, image_width / self.tile_size):
            rect = (i * self.tile_size, 0, self.tile_size, self.tile_size)
            self.tiles.append(level.subsurface(rect))
    
    def load_map(self):
        #reads the map from file
        level_file = open(self.level_path, "r")
        self.map = level_file.read().split("\n")
        level_file.close()

        #reads the key from file
        parser = ConfigParser.ConfigParser()
        parser.read(self.key_path)
        for section in parser.sections():
            tile_description = dict(parser.items(section))
            self.key[section] = tile_description

        #set some variables for later use
        self.width = len(self.map[0])
        self.height = len(self.map)
        self.actual_width = self.width * self.tile_size
        self.actual_height = self.height * self.tile_size
        
    def create(self):
        #build the level image, also return its rect
        image = pygame.Surface((self.actual_width, self.actual_height)).convert()
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
                    
