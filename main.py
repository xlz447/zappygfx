import pygame
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
GAME_OVER = False

for row in range(MAPHEIGHT):
	for column in range(MAPWIDTH):
		DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))

while not GAME_OVER:
	for event in pygame.event.get():

		keys = pygame.key.get_pressed()
        key_events.global_events()

        if event.type == pygame.QUIT:
			GAME_OVER = True

        # MOVE RIGHT
        if (keys[K_RIGHT]) and PLAYER.PLAYER_POS[0] < MAPWIDTH - 1:
           key_events.key_right()

        # MOVE LEFT
        if (keys[K_LEFT]) and PLAYER.PLAYER_POS[0] > 0:
           key_events.key_left()

        # MOVE UP
        if (keys[K_UP]) and PLAYER.PLAYER_POS[1] > 0:
            key_events.key_up()

        # MOVE DOWN
        if (keys[K_DOWN]) and PLAYER.PLAYER_POS[1] < MAPHEIGHT - 1:
            key_events.key_down()

	pygame.display.update()

	DISPLAYSURFACE.blit(PLAYER.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))
