import pygame, sys
from pygame.locals import DOUBLEBUF
from pygame.locals import QUIT

pygame.init()

'''
Globals
'''
fps = 15
fpsClock = pygame.time.Clock()
flags = DOUBLEBUF
DISPLAYSURF = pygame.display.set_mode((1280, 750), flags, 16)
font = pygame.font.SysFont('Arial', 40)
objects = [] #objects in display

class node:
    def __init__(self,name,pos):
        self.name = name
        self.pos = pos
    def __str__(self):
        return f"{self.name}({self.pos})"
    

while 1:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	for object in objects:
		object.process()
	pygame.display.update()
	fpsClock.tick(fps)