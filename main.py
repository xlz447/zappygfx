import pygame, sys
from pygame.locals import *
from grid import *
from key_events import KeyEvents

class LINK:
    def __init__(self):
        self.SPRITE_POS = pygame.image.load('./sprites/link/link_f6.png')
        self.PLAYER_POS = [0, 0]
        self.PLAYER_INV = []
        self.HEALTH = 100
        self.MANA = 200
        self.DIRECTION = False

PLAYER = LINK()
key_events = KeyEvents(PLAYER)
GAME_OVER = False

while not GAME_OVER:
	for event in pygame.event.get():

		keys = pygame.key.get_pressed()
        key_events.global_events()

        if event.type == pygame.QUIT:
			GAME_OVER = True

        # MOVE RIGHT
        if (keys[K_RIGHT]):
           key_events.key_right(PLAYER.PLAYER_POS[0], MAPWIDTH)

        # MOVE LEFT
        if (keys[K_LEFT]):
           key_events.key_left(PLAYER.PLAYER_POS[0], MAPWIDTH)

        # MOVE UP
        if (keys[K_UP]):
            key_events.key_up(PLAYER.PLAYER_POS[1], MAPHEIGHT)

        # MOVE DOWN
        if (keys[K_DOWN]):
            key_events.key_down(PLAYER.PLAYER_POS[1], MAPHEIGHT)
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))
			for i in range(0, len(ITEMGRID[row][column])):
				it_i = ITEMGRID[row][column][i]
				DISPLAYSURFACE.blit(ITEMS[it_i], (column * TILESIZE + (it_i % 2) * 50, row * TILESIZE + (it_i / 2) * 15))
	DISPLAYSURFACE.blit(PLAYER.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))

	pygame.display.update()
