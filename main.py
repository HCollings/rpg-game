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

def get_time():
    return float(pygame.time.get_ticks()) / 1000.0

def update(all_sprites, dt):
    all_sprites.update(dt)

def render(all_sprites, background, background_rect):
    screen = pygame.display.get_surface()
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

def draw_hud(graphics_FPS):
    font = pygame.font.SysFont("monospace", 15)
    text = "FPS: " + str(graphics_FPS)
    label = font.render(text, 1, (255,255,255))
    screen = pygame.display.get_surface()
    screen.blit(label, (10, 10))

def scrolling(level, background_rect, player):
    screen = pygame.display.get_surface()
    screen_rect = screen.get_rect()
    level_offset_top = - background_rect.top
    level_offset_right = level.actual_width - background_rect.left + screen_rect.width
    level_offset_bottom = level.actual_height - background_rect.top + screen_rect.height
    level_offset_left = - background_rect.left
    player_screen_offset_top = player.rect.top
    player_screen_offset_right = screen_rect.width - (player.rect.left + player.rect.width)
    player_screen_offset_bottom = screen_rect.height - (player.rect.top + player.rect.height)
    player_screen_offset_left = player.rect.left
    if (level_offset_top > 0 and player_screen_offset_top < 200):
        background_rect.top += 2
    if (level_offset_right > 0 and player_screen_offset_right < 200):
        background_rect.left -= 2
    if (level_offset_bottom > 0 and player_screen_offset_bottom < 200):
        background_rect.top -= 2
    if (level_offset_left > 0 and player_screen_offset_left < 200):
        background_rect.left += 2
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    screen.fill((0, 0, 0))
    
    pygame.display.set_caption("test")

    level = Level()
    player = Player()

    level.load_tiles("tiles.png")
    level.load_map("level.map", "key.txt")
    background, background_rect = level.render()
    all_sprites = pygame.sprite.Group(player)

    clock = pygame.time.Clock()
    physics_FPS = 60.0
    dt = 1.0 / physics_FPS
    time_current = get_time()
    accumulator = 0.0    

    # game loop
    while True:
        time_new = get_time()
        time_frame = time_new - time_current
        if time_frame > 0.25:
            time_frame = 0.25
        accumulator += time_frame
        time_current = time_new        
        # update
        while accumulator >= dt:
            update(all_sprites, dt)
            scrolling(level, background_rect, player)
            accumulator -= dt
        # events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    player.moving_up = True
                if event.key == K_d:
                    player.moving_right = True                    
                if event.key == K_s:
                    player.moving_down = True
                if event.key == K_a:
                    player.moving_left = True
            elif event.type == KEYUP:
                if event.key == K_w:
                    player.moving_up = False
                if event.key == K_d:
                    player.moving_right = False                    
                if event.key == K_s:
                    player.moving_down = False
                if event.key == K_a:
                    player.moving_left = False        
        # render
        render(all_sprites, background, background_rect)
        graphics_FPS = math.floor(1.0 / (clock.tick() / 1000.0))
        draw_hud(graphics_FPS)
        pygame.display.update()

if __name__ == "__main__":
    main()


