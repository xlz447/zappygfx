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

TILESIZE = 120
ITEMSIZE = 20
PLAYERSIZE = 80

TEXTURES = {
    GRASS:
	pygame.transform.scale(pygame.image.load('./textures/floor/grass2.jpg'), (TILESIZE, TILESIZE)),
    GRASSFLOWER:
	pygame.transform.scale(pygame.image.load('./textures/floor/grassflower2.jpg'), (TILESIZE, TILESIZE)),
    GRASSSTONE:
	pygame.transform.scale(pygame.image.load('./textures/floor/grassstone2.jpg'), (TILESIZE, TILESIZE)),
	SOIL:
	pygame.transform.scale(pygame.image.load('./textures/floor/soil2.jpg'), (TILESIZE, TILESIZE))
}

ITEMS = {
	DERAUMERE:
	pygame.transform.scale(pygame.image.load('./textures/item/deraumere54.png'), (ITEMSIZE, ITEMSIZE)),
	LINEMATE:
	pygame.transform.scale(pygame.image.load('./textures/item/linemate54.png'), (ITEMSIZE, ITEMSIZE)),
	MENDIANE:
	pygame.transform.scale(pygame.image.load('./textures/item/mendiane54.png'), (ITEMSIZE, ITEMSIZE)),
	PHIRAS:
	pygame.transform.scale(pygame.image.load('./textures/item/phiras54.png'), (ITEMSIZE, ITEMSIZE)),
	SIBUR:
	pygame.transform.scale(pygame.image.load('./textures/item/sibur54.png'), (ITEMSIZE, ITEMSIZE)),
	THYSTAME:
	pygame.transform.scale(pygame.image.load('./textures/item/thystame54.png'), (ITEMSIZE, ITEMSIZE)),
	FOOD:
	pygame.transform.scale(pygame.image.load('./textures/item/food.png'), (ITEMSIZE, ITEMSIZE))

}

def blitz_grid(NUM_ROW, NUM_COL, DISPLAYSURFACE, GRIDS):
	for row in range(NUM_ROW):
		for column in range(NUM_COL):
			DISPLAYSURFACE.blit(GRIDS[row][column].background, (column*TILESIZE, row*TILESIZE))
			for i in range(7):
				if GRIDS[row][column].items[i][2] is 1:
					DISPLAYSURFACE.blit(ITEMS[i], (column*TILESIZE + (TILESIZE - ITEMSIZE) * GRIDS[row][column].items[i][0], row*TILESIZE + (TILESIZE - ITEMSIZE) * GRIDS[row][column].items[i][1]))
	for row in range(NUM_ROW):
		for column in range(NUM_COL):
			for p in range(len(GRIDS[row][column].players)):
				xcoor = int(column*TILESIZE + (TILESIZE - PLAYERSIZE) * GRIDS[row][column].players[p][0] + GRIDS[row][column].players[p][2].xshift * TILESIZE)
				ycoor = int(row*TILESIZE + (TILESIZE - PLAYERSIZE) * GRIDS[row][column].players[p][1] + GRIDS[row][column].players[p][2].yshift * TILESIZE)
				print("( " + str(xcoor) + ", " + str(ycoor) + ")")
				DISPLAYSURFACE.blit((GRIDS[row][column].players[p][2]).img, (xcoor, ycoor))
	print("Done")
#					DISPLAYSURFACE.blit((GRIDS[row][column].players[p][2]).img, (column*TILESIZE + (TILESIZE - PLAYERSIZE) * GRIDS[row][column].players[p][0], row*TILESIZE + (TILESIZE - PLAYERSIZE) * GRIDS[row][column].players[p][1]))

def main():
	# setup pygame, default max win is 500 * 500 <---we need to change this

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
	ALL_PLAYER = {}
	GRIDS = []
	COUNTER = 1
	while GAMEOVER != True:
		if (COUNTER == 1):
			data = ""
			GET_FULL_DATA = False
			sep = "@"
			# to make sure we have the full data to run
			while not GET_FULL_DATA:
				data += s.recv(BUFFER_SIZE)
				GET_FULL_DATA = sep in data.split("\n")

			data_split = data.split("\n")
			map_data = data_split[0].split(",")
			print (map_data)
	#####################################setup the grid, only need to do this once, ################################
	#####################################we can sent "im gfx" to server when first connect##########################
	#####################################server will send back a grid size, only once, use special char#############
			NUM_ROW = int(map_data.pop(0))
			NUM_COL = int(map_data.pop(0))


		# setting up grids
		if(GRIDS == []):
			for r in range (NUM_ROW):
				GRIDS.append([])
				for c in range (NUM_COL):
					if "#" not in map_data[0]:
						new_grid = Grid()
						new_grid.setup(TEXTURES[GRASSFLOWER], int(map_data.pop(0)), [])
						GRIDS[r].append(new_grid)
	################################################################################################################
	######################################this part is the players #################################################
	# we can #1: make a new list of players, and compare each of them with the old list and do stuff accordingly
	#        #2: we can add an attribute in the player object, maybe old position? and update it when we read data
	#  maybe #3???? but for now, I am going to make it simple and easy...

		# 1 grid 4 frame
		# make all players disappear first
		for py in ALL_PLAYER:
			ALL_PLAYER[py].present = 0
			ALL_PLAYER[py].xshift = 0
			ALL_PLAYER[py].yshift = 0
			
		for i in range(1, len(data_split)):
			if not (data_split[i] == '' or data_split[i] == '@'):
				new_player = Player()
				new_player.setup(data_split[i])
				if not(new_player.id < 0):
					if new_player.id in ALL_PLAYER:
						print("already has something")
						ALL_PLAYER[new_player.id].coor[2] = new_player.coor[2]
						x_change = new_player.coor[0] - ALL_PLAYER[new_player.id].coor[0]
						y_change = new_player.coor[1] - ALL_PLAYER[new_player.id].coor[1]
						if x_change != 0:
							print("walk x")
							ALL_PLAYER[new_player.id].update(COUNTER)
							ALL_PLAYER[new_player.id].xshift = (0.25 * COUNTER * x_change / abs(x_change))
							GRIDS[ALL_PLAYER[new_player.id].coor[1]][ALL_PLAYER[new_player.id].coor[0]].updateplayer(new_player.id, ALL_PLAYER[new_player.id].xshift, ALL_PLAYER[new_player.id].yshift)
							if COUNTER == 4:
								ALL_PLAYER[new_player.id].xshift = 0
								GRIDS[ALL_PLAYER[new_player.id].coor[1]][ALL_PLAYER[new_player.id].coor[0]].removeplayer(new_player.id)
								ALL_PLAYER[new_player.id].coor[0] = new_player.coor[0]
								GRIDS[new_player.coor[1]][new_player.coor[0]].addplayer(new_player)
							
						if y_change != 0:
							print("walk y")
							ALL_PLAYER[new_player.id].update(COUNTER)						
							ALL_PLAYER[new_player.id].yshift = (0.25 * COUNTER * y_change / abs(y_change))
							GRIDS[ALL_PLAYER[new_player.id].coor[1]][ALL_PLAYER[new_player.id].coor[0]].updateplayer(new_player.id, ALL_PLAYER[new_player.id].xshift, ALL_PLAYER[new_player.id].yshift)
							blitz_grid(NUM_ROW, NUM_COL, DISPLAYSURFACE, GRIDS)
							if COUNTER == 4:								
								ALL_PLAYER[new_player.id].yshift = 0
								GRIDS[ALL_PLAYER[new_player.id].coor[1]][ALL_PLAYER[new_player.id].coor[0]].removeplayer(new_player.id)
								ALL_PLAYER[new_player.id].coor[1] = new_player.coor[1]
								GRIDS[new_player.coor[1]][new_player.coor[0]].addplayer(new_player)
					else:
						print("new player " + str(new_player.id))
						ALL_PLAYER[new_player.id] = new_player
						GRIDS[new_player.coor[1]][new_player.coor[0]].addplayer(new_player)
						
#						while ALL_PLAYER[new_player.id].coor[0] != new_player.coor[0]:
#							if ALL_PLAYER[new_player.id].coor[0] < new_player.coor[0]:
#								ALL_PLAYER[new_player.id].coor[0] += ALL_PLAYER[new_player.id].movespeed
#							else:
#								ALL_PLAYER[new_player.id].coor[0] -= ALL_PLAYER[new_player.id].movespeed
#							ALL_PLAYER[new_player.id].counter = (ALL_PLAYER[new_player.id].counter + 1) % len(f_images)
#							DISPLAYSURFACE.blit(pygame.image.load(f_images[ALL_PLAYER[new_player.id].counter]),(ALL_PLAYER[new_player.id].coor[1], ALL_PLAYER[new_player.id].coor[0]))
#							pygame.display.update()
#						while ALL_PLAYER[new_player.id].coor[1] != new_player.coor[1]:
#							if ALL_PLAYER[new_player.id].coor[1] < new_player.coor[1]:
#								ALL_PLAYER[new_player.id].coor[1] += ALL_PLAYER[new_player.id].movespeed
#							else:
#								ALL_PLAYER[new_player.id].coor[1] -= ALL_PLAYER[new_player.id].movespeed
#							ALL_PLAYER[new_player.id].counter = (ALL_PLAYER[new_player.id].counter + 1) % len(f_images)
#							DISPLAYSURFACE.blit(pygame.image.load(f_images[ALL_PLAYER[new_player.id].counter]),(ALL_PLAYER[new_player.id].coor[1], ALL_PLAYER[new_player.id].coor[0]))
#							pygame.display.update()

	################################################################################################################
		
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if event.type == pygame.QUIT:
				GAMEOVER = True
		COUNTER += 1
		if COUNTER == 5:
			COUNTER = 1
			
		blitz_grid(NUM_ROW, NUM_COL, DISPLAYSURFACE, GRIDS)
		pygame.display.flip()
		pygame.time.delay(100)
#		for row in range(NUM_ROW):
#			for column in range(NUM_COL):
#				DISPLAYSURFACE.blit(GRIDS[row][column].background, (column*TILESIZE, row*TILESIZE))
#				for i in range(7):
#					if GRIDS[row][column].items[i][2] is 1:
#						DISPLAYSURFACE.blit(ITEMS[i], (column*TILESIZE + (TILESIZE - ITEMSIZE) * GRIDS[row][column].items[i][0], row*TILESIZE + (TILESIZE - ITEMSIZE) * GRIDS[row][column].items[i][1]))
#				for p in range(len(GRIDS[row][column].players)):
#					DISPLAYSURFACE.blit(GRIDS[row][column].players[p][2], (column*TILESIZE + (TILESIZE - PLAYERSIZE) * GRIDS[row][column].players[p][0], row*TILESIZE + (TILESIZE - PLAYERSIZE) * GRIDS[row][column].players[p][1]))
	
main()