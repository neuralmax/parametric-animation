import pygame, sys
from random import randint
from pygame.locals import *
pygame.init()
size=500,400
screen=pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption('Hello agent!')
screen.fill((0,0,0))
pygame.display.update()
agent=[0,0]#[ position x, position y ]
speed=[1,1]#[ speed x, speed y ]
running=True
while running:
	for event in pygame.event.get():
		if event.type==QUIT:running=False
	mouseX,mouseY=mouse=pygame.mouse.get_pos()
	clr=(randint(0,255),randint(0,255),randint(0,255))
	agent[0]+=speed[0]
	agent[1]+=speed[1]
	
	if agent[0]<0:
		speed[0]*=-1
	if agent[1]<0:
		speed[1]*=-1
	if agent[0]>size[0]:
		speed[0]*=-1
	if agent[1]>size[1]:
		speed[1]*=-1
	
	pygame.draw.circle(screen, clr, agent, 20, 0)
	pygame.display.update()
pygame.quit()
sys.exit()