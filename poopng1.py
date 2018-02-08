# First code stub for testing use of pygame for DigitalTwin displays
# Move a png around the screen with a full screen toggle
# NOTE: requires a png file name poo.png in the same folder as the py script

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
#DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
#modes = pygame.display.list_modes(16)

#DISPLAYSURF = pygame.display.set_mode((0, 0), FULLSCREEN, 32)
scr_size = ( 320 , 240 )
DISPLAYSURF = pygame.display.set_mode ( scr_size )
pygame.display.set_caption('poo.png')

WHITE = (255, 255, 255)
pooImg = pygame.image.load('poo.png')
poox = 10
pooy = 10
direction = 'right'

running = True
while running: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        poox += 5
        if poox == 280:
            direction = 'down'
    elif direction == 'down':
        pooy += 5
        if pooy == 220:
            direction = 'left'
    elif direction == 'left':
        poox -= 5
        if poox == 10:
            direction = 'up'
    elif direction == 'up':
        pooy -= 5
        if pooy == 10:
            direction = 'right'

    DISPLAYSURF.blit(pooImg, (poox, pooy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            running = False  # be interpreter friendly
            sys.exit()
        # fullscreen toggle code
        elif (event.type is KEYDOWN and event.key == K_ESCAPE):
            if DISPLAYSURF.get_flags() & FULLSCREEN:
                pygame.display.set_mode(scr_size)
            else:
                pygame.display.set_mode(scr_size, FULLSCREEN)

    pygame.display.update()
    fpsClock.tick(FPS)
