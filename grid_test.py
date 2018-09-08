import random, pygame

class Grid:
	def __init__(self):
		self.background = None
		self.items = [] #[{x0, y0, 0}, {x1, y1,1}, ...., {x6, y6,1}] # will always be length 7
		self.players = [] #[{x0, y0, image}, {x1, y1, image},......] # might be empty
		for i in range(0, 6):
			self.items.append([random.random(), random.random(), 0]) # set up the random xy coordinates and start with no item


	"""
	Funciton to setup a grid
	Args:
    	img: the background image used for this grid(preloaded using pygames.image.load)
    	items: an int ranging from 0 to 127 representing the items that will apppear in this grid
		player: data type TBD, (tuple?) contains information of the team and the orientation of all players on the grid

	Returns:
    	None

	Raises:
    	Nothing for now
	"""
	def setup(self, img, items, players):
		self.background = img
		for i in range(5, -1, -1):
			self.items[i][2] = items % 2
			items = items / 2
		# test items
#		for j in range(0, 7):
#			print("Item " + str(j) + " is " + str(self.items[j][1]))

		# set up players
		self.players = []




# this is just for testing
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

TEXTURES = {
    BRICKMOSS: pygame.image.load('./textures/floor/brickmoss.jpg'),
    GRASS: pygame.image.load('./textures/floor/grass.jpg'),
	BRICK: pygame.image.load('./textures/floor/brick.jpg'),
    GRASSFLOWER: pygame.image.load('./textures/floor/grassflower.jpg'),
    GRASSSTONE: pygame.image.load('./textures/floor/grassstone2.jpg'),
    PLASTER: pygame.image.load('./textures/floor/plaster.jpg'),
	SOIL: pygame.image.load('./textures/floor/soil.jpg')
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
	pygame.image.load('./textures/item/thystame20.png')
}

GRIDS = []

################################## this part will change to input from server
f1 = open("testinput.txt", 'r')
test_input = f1.read()
f1.close()
##################################
ALL_ITEM = test_input.split(",")
NUM_ROW = int(ALL_ITEM.pop(0))
NUM_COL = int(ALL_ITEM.pop(0))

# setup pygame, default max win is 500 * 500 <---we need to change this
TILESIZE = min([500/NUM_ROW, 1000/NUM_COL])
ITEMSIZE = 20
pygame.init()
pygame.display.set_caption('testing')
DISPLAYSURFACE = pygame.display.set_mode((NUM_COL * TILESIZE, NUM_ROW * TILESIZE))

for i in TEXTURES:
	pygame.transform.scale(TEXTURES[i], (TILESIZE, TILESIZE))

for r in range (NUM_ROW):
	GRIDS.append([])
	for c in range (NUM_COL):
		if "#" not in ALL_ITEM[0]:
			new_grid = Grid()
			new_grid.setup(TEXTURES[GRASSSTONE], int(ALL_ITEM.pop(0)), [])
			GRIDS[r].append(new_grid)


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
	for event in pygame.event.get():
		keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
			GAMEOVER = True

	for row in range(NUM_ROW):
		for column in range(NUM_COL):
			DISPLAYSURFACE.blit(GRIDS[row][column].background, (column*TILESIZE, row*TILESIZE))
			for i in range(6):
				if GRIDS[row][column].items[i][2] is 1:
					DISPLAYSURFACE.blit(ITEMS[i], (column*TILESIZE + (TILESIZE - ITEMSIZE) * GRIDS[row][column].items[i][0], row*TILESIZE + (TILESIZE - ITEMSIZE) * GRIDS[row][column].items[i][1]))
	pygame.display.update()
