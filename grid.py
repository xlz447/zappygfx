import pygame

# TILES
BRICK = 0
BRICKMOSS = 1
GRASS = 2
GRASSFLOWER = 3
GRASSSTONE = 4
PLASTER = 5
SOIL = 6

TEXTURES = {
    BRICK: pygame.image.load('./textures/floor/brick.jpg'),
    BRICKMOSS: pygame.image.load('./textures/floor/brickmoss.jpg'),
    GRASS: pygame.image.load('./textures/floor/grass.jpg'),
    GRASSFLOWER: pygame.image.load('./textures/floor/grassflower.jpg'),
    GRASSSTONE: pygame.image.load('./textures/floor/grassstone.jpg'),
    PLASTER: pygame.image.load('./textures/floor/plaster.jpg'),
	SOIL: pygame.image.load('./textures/floor/soil.jpg')
}

GRID = [
    [GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE],
	[GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE],
	[GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE],
	[GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE],
	[GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE, GRASSSTONE]
]

# GAME DIMENSIONS, CONFIG
TILESIZE = 100
MAPWIDTH = 5
MAPHEIGHT = 5
pygame.init()
pygame.display.set_caption('testing')

DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
