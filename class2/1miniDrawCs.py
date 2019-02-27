# load modules
import pygame,sys
from pygame.locals import *
# start game engine
pygame.init()
# open window
screen=pygame.display.set_mode((500, 400), 0, 32)
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
	# check if mouse is pressed
	if pygame.mouse.get_pressed()[0]:
		# draw circle on mouse coordinates
		pygame.draw.circle(screen,(255,255,255), mouse, 20, 0)
	# all drawing operations are made in memory, next command displays changes
	pygame.display.update()
# stop game engine	
pygame.quit()
# stop program
sys.exit()
