#!/usr/bin/env python

try:
    import os
    import sys
    import math
    import random
    import pygame    
    from pygame.locals import *
    from level import *
    from player import *
    from resources import *
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

        #set program stuff
        self.screen_size = (1280, 720)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.name = "RPG"
        self.keys_down = []        

    def load(self):
        #set program stuff
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption(self.name)

        #initialise objects
        level = Level("level.map", "key.txt")
        level.load_tiles("tiles.png")
        level.load_map()
        self.background, self.background_rect = level.create()
        player = Player()        
        self.entities = pygame.sprite.Group(player)

        self.play(level, player)

    def get_time(self):
        #returns time passed in seconds
        return float(pygame.time.get_ticks()) / 1000.0

    def handle_collisions(self, player):
        screen_rect = self.screen.get_rect()
        level_offset_top = - self.background_rect.top
        level_offset_right = self.background_rect.width - (-self.background_rect.left + screen_rect.width)
        level_offset_bottom = self.background_rect.height - (-self.background_rect.top + screen_rect.height)
        level_offset_left = - self.background_rect.left
        player_screen_offset_top = player.rect.top
        player_screen_offset_right = screen_rect.width - (player.rect.left + player.rect.width)
        player_screen_offset_bottom = screen_rect.height - (player.rect.top + player.rect.height)
        player_screen_offset_left = player.rect.left
        if (level_offset_top > 0 and player_screen_offset_top < 200):
            self.background_rect.top += 8
        if (level_offset_right > 0 and player_screen_offset_right < 200):
            self.background_rect.left -= 8
        if (level_offset_bottom > 0 and player_screen_offset_bottom < 200):
            self.background_rect.top -= 8
        if (level_offset_left > 0 and player_screen_offset_left < 200):
            self.background_rect.left += 8

        player.location[0] = player.position[0] - self.background_rect.left
        player.location[1] = player.position[1] - self.background_rect.top
        if player.location[1] < 0:
            player.position[1] = 0
        if player.location[0] + player.rect.width > self.background_rect.width:
            player.position[0] = screen_rect.width - player.rect.width
        if player.location[1] + player.rect.height > self.background_rect.height:
            player.position[1] = screen_rect.height - player.rect.height
        if player.location[0] < 0:
            player.position[0] = 0        

    def scroll_screen(self, direction):
        if direction == "up":
            self.background_rect.top += 32
        if direction == "right":
            self.background_rect.left -= 32
        if direction == "down":
            self.background_rect.top -= 32
        if direction == "left":
            self.background_rect.left += 32        

    def handle_events(self, player):
        dt = self.__dt
        player.movement_cooldown += dt
        self.keys_down = pygame.key.get_pressed()
        print player.movement_cooldown, player.movement_limit
        if player.movement_cooldown >= player.movement_limit:
            if self.keys_down[K_w]:       
                player.move("up", dt)
            if self.keys_down[K_d]:
                player.move("right", dt)
            if self.keys_down[K_s]:
                player.move("down", dt)
            if self.keys_down[K_a]:
                player.move("left", dt)
            player.movement_cooldown = 0.0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()                

    def update(self):
        #call update method for all entities
        self.entities.update()

    def render(self):
        self.screen.blit(self.background, self.background_rect)
        self.entities.draw(self.screen)

    def play(self, level, player):
        dt = self.__dt
        while True:
            time_new = self.get_time()
            time_frame = time_new - self.time_current
            if time_frame > 0.25:
                time_frame = 0.25
            self.accumulator += time_frame
            self.time_current = time_new        
            # update
            while self.accumulator >= dt:
                self.update()
                self.handle_collisions(player)
                self.accumulator -= dt           
                self.handle_events(player)
            # render
            self.render()
            pygame.display.update()       
    
def main():
    pygame.init()
    game = Game()
    game.load()

if __name__ == "__main__":
    main()
