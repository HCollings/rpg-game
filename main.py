#!/usr/bin/env python

try:
    import os
    import sys
    import math
    import random
    from socket import *
    import pygame    
    from pygame.locals import *
    from objects import *
    from resources import *
except ImportError, err:
    print "cannot load module(s)"
    sys.exit(2)  

def main():
    
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    background = pygame.Surface(screen.get_size())
    background.convert()
    background.fill((0, 0, 0))
    pygame.display.set_caption("test")

    level = Level()
    hero = Hero()

    level.load_tiles("tiles.png")
    level.load_map("level.txt")

    
    allsprites = pygame.sprite.RenderPlain(hero)

    clock = pygame.time.Clock()

    # game loop
    
    while True:
        
        clock.tick(60)

        # events

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_w:
                    hero.move_up()
                if event.key == K_s:
                    hero.move_down()
                if event.key == K_a:
                    hero.move_left()
                if event.key == K_d:
                    hero.move_right()
            elif event.type == KEYUP:
                if event.key == K_w or event.key == K_s:
                    hero.movepos[1] = 0
                    hero.state = "still"
                if event.key == K_a or event.key == K_d:
                    hero.movepos[0] = 0
                    hero.state = "still"

        allsprites.update()
        screen.blit(background, (0, 0))
        screen.blit(hero.image, hero.rect)
        allsprites.draw(screen)        
        pygame.display.update()

if __name__ == "__main__":
    main()


