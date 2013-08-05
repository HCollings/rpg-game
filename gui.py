#!/usr/bin/env python

try:
    import os
    import pygame    
    from resources import *
    from main import *
except ImportError, err:
    print "cannot load module(s)"
    sys.exit(2)  

# gui

class Menu_item(pygame.font.Font):
    def __init__(self, text, position, font_size = 15, antialias = 1, color = (255,255,255)):
        pygame.font.Font.__init__(self, None, font_size)
        self.text = text
        self.text_surface = self.render(self.text, antialias, color)
        self.position = self.text_surface.get_rect(centerx = position[0], centery = position[1])
    def get_position(self):
        return self.position
    def get_text(self):
        return self.text
    def get_surface(self):
        return self.text_surface

class Menu:
    def __init__(self, menu_items):
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.menu_surface = pygame.Surface(screen.get_size()).convert()
        print self.menu_surface
        self.active = False
        font_size = 15
        font_space = 4
        center_x = self.area.width / 2
        menu_height = (font_size + font_space) * len(menu_items)
        start_y = (self.area.height / 2) - (menu_height / 2)
        self.menu_list = list()
        for menu_item in menu_items:
            center_y = start_y + font_size + font_space
            item = Menu_item(menu_item, (center_x, center_y))
            self.menu_list.append(item)
            self.menu_surface.blit(item.get_surface(), item.get_position())
            start_y = start_y + font_size + font_space
            
    def draw(self):
        self.active = True            
        screen = pygame.display.get_surface()
        screen.blit(self.menu_surface, (100, 100))      

    def is_active(self):
        return self.active
    def activate(self):
        self.active = True
    def deactivate(self):
        self.active = False
