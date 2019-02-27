import pygame, sys
from random import randint
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((500, 400), 0, 32)

img = pygame.image.load('skull.png')
imgsz=img.get_rect().size
pygame.display.set_caption('Hello skull! '+str(imgsz))

running=True
while running:
	for event in pygame.event.get():
		if event.type==QUIT:running=False
	mouseX,mouseY=mouse=pygame.mouse.get_pos()
	clr=(randint(0,255),randint(0,255),randint(0,255))
	if pygame.mouse.get_pressed()[0]:
		pygame.draw.circle(screen, clr, mouse, 20, 0)
		
	screen.blit(img,(0,0))
	pygame.display.update()
arr=[]
for y in range(imgsz[1]):
	for x in range(imgsz[0]):
		clr=screen.get_at((x, y))
		arr.append([x,y,clr[0]])

with open('data.scad','w') as f:
	f.write('data=[')
	for p in arr:
		f.write(str(p)+',\n')
	f.write('];')
pygame.quit()
sys.exit()