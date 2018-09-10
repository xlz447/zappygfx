import socket, pygame
from grid_test import *
from player_test import *

# TILES
BRICKMOSS = 0
GRASS = 1
BRICK = 2
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
FOOD = 6

TEXTURES = {
    GRASS: pygame.image.load('./textures/floor/grass2.jpg'),
    GRASSFLOWER: pygame.image.load('./textures/floor/grassflower2.jpg'),
    GRASSSTONE: pygame.image.load('./textures/floor/grassstone2.jpg'),
	SOIL: pygame.image.load('./textures/floor/soil2.jpg')
}

ITEMS = {
	DERAUMERE:
	pygame.image.load('./textures/item/deraumere20.png'),
	LINEMATE:
	pygame.image.load('./textures/item/linemate20.png'),
	MENDIANE:
	pygame.image.load('./textures/item/mendiane20.png'),
	PHIRAS:
	pygame.image.load('./textures/item/phiras20.png'),
	SIBUR:
	pygame.image.load('./textures/item/sibur20.png'),
	THYSTAME:
	pygame.image.load('./textures/item/thystame20.png'),
	FOOD:
	pygame.image.load('./textures/item/food20.png')
}

# setup pygame, default max win is 500 * 500 <---we need to change this
TILESIZE = 100
ITEMSIZE = 20
pygame.init()
pygame.display.set_caption('testing')
DISPLAYSURFACE = pygame.display.set_mode((10 * TILESIZE, 10 * TILESIZE))


TCP_IP = '127.0.0.1'
TCP_PORT = 4242
BUFFER_SIZE = 2048 #map

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

	# setup items
	# for row in range(0, ALL_ITEM):
	# 	GRIDS.append([])
	# 	COL_ITEM = ROW_ITEM[row].split(",")
	# 	if len(COL_ITEM) != NUM_COL:
	# 		raise ValueError("Inconsistent column length at row " + str(row))
	# 	for col in range(0, NUM_COL):
	# 		new_grid = Grid()
	# 		new_grid.setup(TEXTURES[GRASSSTONE], int(COL_ITEM[col]), [])
	# 		GRIDS[row].append(new_grid)

GAMEOVER = False
while GAMEOVER != True:
	GRIDS = []
	ALL_PLAYER = {}
	data = ""
	GET_FULL_DATA = False
	sep = "@"
	# to make sure we have the full data to run
	while not GET_FULL_DATA:
		data += s.recv(BUFFER_SIZE)
		GET_FULL_DATA = sep in data.split("\n")
#	while (data == "" or data[len(data) - 2] == '#'): 
#		data += s.recv(BUFFER_SIZE) + "\n" # temporary version due to flawed input
	print (data)
##################################
	data_split = data.split("\n")
	ALL_ITEM = data_split[0].split(",")
	print (data_split)
	NUM_ROW = int(ALL_ITEM.pop(0))
	NUM_COL = int(ALL_ITEM.pop(0))

	for i in TEXTURES:
		pygame.transform.scale(TEXTURES[i], (TILESIZE, TILESIZE))

	# setting up grids
	for r in range (NUM_ROW):
		GRIDS.append([])
		for c in range (NUM_COL):
			if "#" not in ALL_ITEM[0]:
				new_grid = Grid()
				new_grid.setup(TEXTURES[GRASSFLOWER], int(ALL_ITEM.pop(0)), [])
				GRIDS[r].append(new_grid)

	# setting up players
	for i in range(1, len(data_split)):
		if not (data_split[i] == '' or data_split[i] == '@'):
			new_player = Player()
			new_player.setup(data_split[i])
			if not(new_player.id < 0 or new_player.id in ALL_PLAYER):
				ALL_PLAYER[new_player.id] = new_player
#				print("Player " + str(new_player.id) + " created")

	
	for event in pygame.event.get():
		keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
			GAMEOVER = True

	for row in range(NUM_ROW):
		for column in range(NUM_COL):
			DISPLAYSURFACE.blit(GRIDS[row][column].background, (column*TILESIZE, row*TILESIZE))
			for i in range(7):
				if GRIDS[row][column].items[i][2] is 1:
					DISPLAYSURFACE.blit(ITEMS[i], (column*TILESIZE + (TILESIZE - ITEMSIZE) * GRIDS[row][column].items[i][0], row*TILESIZE + (TILESIZE - ITEMSIZE) * GRIDS[row][column].items[i][1]))
					
	for players in ALL_PLAYER:
		print("display player " + str(ALL_PLAYER[players].id))
	pygame.display.update()
