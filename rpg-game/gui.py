#!/usr/bin/env python

try:
    import os
    import sys
    import pygame
    import resources
except ImportError, err:
    print "cannot load module(s)"
    sys.exit(2)

class Gui:

    def __init__(self):
        self.elements = []

    def draw(self):
        for element in self.elements:
            element.draw()

class Menu:

    def __init__(self, entries, position, (width, height)):
        self.entries = entries
        self.position = position
        self.width, self.height = (width, height)
        self.font_size = 15
        self.menu_surface = pygame.Surface((self.width, self.height)).convert_alpha()
        self.menu_surface.fill((0, 0, 0))
        self.menu_surface.set_alpha(20)
        self.menu_items = []
        for i, entry in enumerate(self.entries):
            label_position = (self.position[0], self.position[1] + (i * (self.font_size + 2)))
            label = Label(entry, label_position, self.font_size)
            self.menu_items.append(label)
            self.menu_surface.blit(label.get_surface(), label.get_position())
        self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def draw(self):
        self.activate()
        screen = pygame.display.get_surface()
        screen.blit(self.menu_surface, self.position)

class Label(pygame.font.Font):

    def __init__(self, text, position, font_size):
        self.font_size = font_size
        self.font = pygame.font.Font(None, self.font_size)
        self.text = text
        self.position = position
        self.surface = self.font.render(self.text, 1, (255, 255, 255))
        
    def get_text(self):
        return self.text

    def get_position(self):
        return self.position

    def get_surface(self):
        return self.surface
