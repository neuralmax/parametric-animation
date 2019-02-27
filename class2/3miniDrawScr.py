import pygame, sys
from random import randint
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world!')
screen.fill((0,0,0))
pygame.display.update()

counter=0

running=True
while running:
	for event in pygame.event.get():
		if event.type==QUIT:
			running=False 
	mouseX,mouseY=mouse=pygame.mouse.get_pos()
	clr=(randint(0,255),randint(0,255),randint(0,255))
	if pygame.mouse.get_pressed()[0]:
		pygame.draw.circle(screen, clr, mouse, 20, 0)
	pygame.display.update()
	
	counter+=1
	pygame.image.save(screen,'screenshot'+str(counter)+'.jpg')
	
pygame.quit()
sys.exit()
