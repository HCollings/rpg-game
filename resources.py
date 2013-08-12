#!/usr/bin/env python

try:
    import os
    import sys
    import pygame    
except ImportError, err:
    print "cannot load module(s)"
    sys.exit(2)  

def load_image(name):
    #load an image and get its rect
    fullname = os.path.join("images", name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()        
    except pygame.error, message:
        print "cannot load image:", name
        raise SystemExit, message
    return image, image.get_rect()         

def load_sound(name):
    #load a sound
    fullname = os.path.join("sounds", name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print "Cannot load sound:", wav
        raise SystemExit, message
    return sound
