import pygame, sys
from random import randint
from pygame.locals import *

from math import sin,cos,radians

pygame.init()
size=500,400
screen=pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption('Hello agent!')
screen.fill((0,0,0))
pygame.display.update()
agent=[0,0]#[ position x, position y ]

speed=[45,0.01]#[ direction , speed ]
running=True
while running:
	for event in pygame.event.get():
		if event.type==QUIT:running=False

	keys=pygame.key.get_pressed()
	if keys[K_LEFT]:
		speed[0]+=0.01
	if keys[K_RIGHT]:
		speed[0]-=0.01
	speedX=sin(radians(speed[0]))*speed[1]
	speedY=cos(radians(speed[0]))*speed[1]
	agent[0]+=sin(radians(speed[0]))*speed[1]
	agent[1]+=cos(radians(speed[0]))*speed[1]
	if agent[0]<0:
		speed[0]+=90
	if agent[1]<0:
		speed[0]+=90
	if agent[0]>size[0]:
		speed[0]+=90
	if agent[1]>size[1]:
		speed[0]+=90
	agentInt=(int(agent[0]),int(agent[1]))
	clr=(randint(0,255),randint(0,255),randint(0,255))	
	pygame.draw.circle(screen, clr, agentInt, 20, 0)
	
	pygame.display.update()
pygame.quit()
sys.exit()