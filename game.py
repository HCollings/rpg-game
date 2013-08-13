#!/usr/bin/env python

try:
    import os
    import sys
    import math
    import random
    import pygame
    from pygame.locals import *
    import level as l
    import player as p
    import gui
    import item
    import item_list
    import resources
except ImportError, err:
    print "cannot load module(s)"
    sys.exit(2)

class Game:
    
    def __init__(self):
        #set physics variables
        self.clock = pygame.time.Clock()
        self.__physics_FPS = 100.0
        self.__dt = 1.0 / self.__physics_FPS
        self.time_current = self.get_time()
        self.accumulator = 0.0
        #set program variables
        self.screen_size = (1280, 720)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.tile_size = 64
        self.name = "RPG"
        self.font = pygame.font.SysFont("monospace", 15)
        #game variables
       
    def load(self):
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption(self.name)
        #initialise objects
        level = l.Level("level.map", "key.txt", self.tile_size)
        level.load_tiles("tiles.png")
        level.load_map()
        self.background, self.background_rect = level.create()
        player = p.Player()
        self.entities = pygame.sprite.Group(player)
        self.set_player_center(player)
        self.set_level_offset(level, player)

        self.gui = gui.Gui()
        
        self.play(level, player)

    def get_time(self):
        #returns time passed in seconds
        return float(pygame.time.get_ticks()) / 1000.0

    def set_player_center(self, player):
        #set player in screen center
        (screen_width, screen_height) = self.screen_size
        player.position[1] = (screen_height / 2) - (player.rect.height / 2)
        player.position[0] = (screen_width / 2) - (player.rect.width / 2)

    def set_level_offset(self, level, player):
        top_offset = player.location[1] - player.position[1]
        left_offset = player.location[0] - player.position[0]
        self.background_rect.top = - top_offset
        self.background_rect.left = - left_offset

    def handle_events(self, player):
        dt = self.__dt
        player.movement_cooldown += dt
        self.keys_down = pygame.key.get_pressed()
        if player.movement_cooldown >= player.movement_limit:
            if self.keys_down[K_w]:       
                player.set_movement_points("up")
            if self.keys_down[K_d]:
                player.set_movement_points("right")
            if self.keys_down[K_s]:
                player.set_movement_points("down")
            if self.keys_down[K_a]:
                player.set_movement_points("left")
            player.movement_cooldown = 0.0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def handle_movement(self, player):
        s = self.tile_size / (player.movement_limit * 100)
        if player.movement_points[0] > 0:
            self.background_rect.top += s
            player.movement_points[0] -= s
        if player.movement_points[1] > 0:
            self.background_rect.left -= s
            player.movement_points[1] -= s
        if player.movement_points[2] > 0:
            self.background_rect.top -= s
            player.movement_points[2] -= s
        if player.movement_points[3] > 0:
            self.background_rect.left += s
            player.movement_points[3] -= s
    
    def is_player_blocked(self, level, player):
        x, y = player.get_coordinates()
        player.directions_blocked["up"] = level.is_wall(x, y - 1)
        player.directions_blocked["right"] = level.is_wall(x + 1, y)
        player.directions_blocked["down"] = level.is_wall(x, y + 1)
        player.directions_blocked["left"] = level.is_wall(x - 1, y)    

    def update(self, level, player):
        self.handle_events(player)
        self.handle_movement(player)
        #call update method for all entities
        self.entities.update()  
        for entity in self.entities:
            #update player location relative to map
            entity.location[0] = entity.position[0] - self.background_rect.left
            entity.location[1] = entity.position[1] - self.background_rect.top
        self.is_player_blocked(level, player)
        
    def render(self):
        self.screen.blit(self.background, self.background_rect)
        dirty_rects = self.entities.draw(self.screen)
        self.gui.draw()
        pygame.display.update()

    def play(self, level, player):
        dt = self.__dt
        while True:
            time_new = self.get_time()
            time_frame = time_new - self.time_current
            if time_frame > 0.25:
                time_frame = 0.25
            self.accumulator += time_frame
            self.time_current = time_new        
            #update
            while self.accumulator >= dt:
                self.update(level, player)
                self.accumulator -= dt
            #render
            self.render()      
    
def main():
    pygame.init()
    game = Game()
    game.load()

if __name__ == "__main__":
    main()
