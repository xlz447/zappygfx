import pygame
from grid import *

GAME_OVER = False

while not GAME_OVER:
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))
	pygame.display.update()
