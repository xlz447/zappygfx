import pygame

# TILES
BRICK = 0
BRICKMOSS = 1
GRASS = 2
GRASSFLOWER = 3
GRASSSTONE = 4
PLASTER = 5
SOIL = 6

DERAUMERE = 0
LINEMATE = 1
MENDIANE = 2
PHIRAS = 3
SIBUR = 4
THYSTAME = 5

TEXTURES = {
    BRICK: pygame.image.load('./textures/floor/brick.jpg'),
    BRICKMOSS: pygame.image.load('./textures/floor/brickmoss.jpg'),
    GRASS: pygame.image.load('./textures/floor/grass.jpg'),
    GRASSFLOWER: pygame.image.load('./textures/floor/grassflower.jpg'),
    GRASSSTONE: pygame.image.load('./textures/floor/grassstone.jpg'),
    PLASTER: pygame.image.load('./textures/floor/plaster.jpg'),
	SOIL: pygame.image.load('./textures/floor/soil.jpg')
}

ITEMS = {
	DERAUMERE:
	pygame.image.load('./textures/item/deraumere54.png'),
	LINEMATE:
	pygame.image.load('./textures/item/linemate54.png'),
	MENDIANE:
	pygame.image.load('./textures/item/mendiane54.png'),
	PHIRAS:
	pygame.image.load('./textures/item/phiras54.png'),
	SIBUR:
	pygame.image.load('./textures/item/sibur54.png'),
	THYSTAME:
	pygame.image.load('./textures/item/thystame54.png')
}

GRID = [
    [GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE],
	[GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE],
	[GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE],
	[GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE],
	[GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE]
]

ITEMGRID = [
    [[0, 1, 2, 5], [], [1, 3, 4, 5], [], [0, 1, 2, 3, 4, 5]],
	[[], [2, 3, 4, 5], [], [0, 3, 4, 5], []],
	[[0, 1, 3, 5], [], [0, 2, 3, 5], [], [0, 1, 2, 3, 4, 5]],
	[[], [1, 3, 4, 5], [], [2, 3, 4, 5], []],
	[[3, 4, 5], [], [0, 1, 2], [], [0, 1, 2, 4]]
]
# GAME DIMENSIONS, CONFIG
TILESIZE = 100
MAPWIDTH = 5
MAPHEIGHT = 5
pygame.init()
pygame.display.set_caption('testing')

DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
