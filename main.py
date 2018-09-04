import pygame
from grid import *

GAME_OVER = False

for row in range(MAPHEIGHT):
	for column in range(MAPWIDTH):
		DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))
while not GAME_OVER:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			GAME_OVER = True
	pygame.display.flip() # flip updates the whole screen