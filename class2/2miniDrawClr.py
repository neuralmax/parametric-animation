# load modules
import pygame, sys
from random import randint
from pygame.locals import *
# start game engine
pygame.init()
# open window
screen=pygame.display.set_mode((500, 400), 0, 32)
# rename window
pygame.display.set_caption('Hello world!')
# paint window black color=(red,green,blue) values:0-255
screen.fill((0,0,0))
# all drawing operations are made in memory, next command displays changes
pygame.display.update()
# status of main loop
running=True
# start main loop
while running:
	# read events: user intaction with window, keyboard, mouse.
	for event in pygame.event.get():
		# check if user tried to close window
		if event.type==QUIT:
			# exit main loop 
			running=False 
	# get mouse coordinates
	mouseX,mouseY=mouse=pygame.mouse.get_pos()
	
	
	# set paint color to random
	clr=(randint(0,255),randint(0,255),randint(0,255))
	# check if mouse is pressed
	if pygame.mouse.get_pressed()[0]:
		# draw circle on mouse coordinates
		pygame.draw.circle(screen, clr, mouse, 20, 0)
		
		
	pygame.display.update()
	# all drawing operations are made in memory, next command displays changes
pygame.quit()
# stop game engine
sys.exit()
# stop program