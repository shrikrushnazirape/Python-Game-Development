import pygame, sys, os
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.dispay.set_mode((400,300),0,32)
pygame.display.set_caption('Drawing')

black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]

DISPLAYSURF.fill(white)
pygame.draw.polygon(DISPLAYSURF, green ((146,0),(291,106),(236,236)))

pixobj = pygame.PixelArray(DISPLAYSURF)
pixobj[380][280] = black
pixobj[382][282] = black
pixobj[384][284]= black

del pixobj

while True:
    for event in pygame.events.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()