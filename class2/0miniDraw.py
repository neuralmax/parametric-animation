import pygame,sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((500, 400), 0, 32)
running=True
while running:
	for event in pygame.event.get():
		if event.type==QUIT:
			running=False
	mouseX,mouseY=mouse=pygame.mouse.get_pos()
	if pygame.mouse.get_pressed()[0]:
		pygame.draw.circle(screen,(255,255,255), mouse, 20, 0)
	pygame.display.update()
pygame.quit()
sys.exit()