import socket
import pygame
from grid_test import *
from player_test import *

# TILES

GRASS = 0
GRASSFLOWER = 1
GRASSSTONE = 2
SOIL = 3

FOOD = 0
LINEMATE = 1
DERAUMERE = 2
SIBUR = 3
MENDIANE = 4
PHIRAS = 5
THYSTAME = 6


TILESIZE = 120
ITEMSIZE = 25
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
    FOOD: pygame.transform.scale(pygame.image.load('./textures/item/food.png'), (ITEMSIZE, ITEMSIZE)),
    LINEMATE: pygame.transform.scale(pygame.image.load('./textures/item/linemate54.png'), (ITEMSIZE, ITEMSIZE)),
    DERAUMERE: pygame.transform.scale(pygame.image.load('./textures/item/deraumere54.png'), (ITEMSIZE, ITEMSIZE)),
    SIBUR: pygame.transform.scale(pygame.image.load('./textures/item/sibur54.png'), (ITEMSIZE, ITEMSIZE)),
    MENDIANE: pygame.transform.scale(pygame.image.load('./textures/item/mendiane54.png'), (ITEMSIZE, ITEMSIZE)),
    PHIRAS: pygame.transform.scale(pygame.image.load('./textures/item/phiras54.png'), (ITEMSIZE, ITEMSIZE)),
    THYSTAME: pygame.transform.scale(pygame.image.load('./textures/item/thystame54.png'), (ITEMSIZE, ITEMSIZE))
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
                # print("( " + str(xcoor) + ", " + str(ycoor) + ")")
                DISPLAYSURFACE.blit((GRIDS[row][column].players[p][2]).img, (xcoor, ycoor))
#   DISPLAYSURFACE.blit((GRIDS[row][column].players[p][2]).img, (column*TILESIZE + (TILESIZE - PLAYERSIZE) * GRIDS[row][column].players[p][0], row*TILESIZE + (TILESIZE - PLAYERSIZE) * GRIDS[row][column].players[p][1]))

def main():

    TCP_IP = '127.0.0.1'
    TCP_PORT = 4242
    BUFFER_SIZE = 8192

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    data = "gfx"
    for x in range(BUFFER_SIZE - len("gfx")):
        data += '#'
    s.send(data)
    data = s.recv(BUFFER_SIZE).split("@")[0].split(",")
    NUM_COL = int(data[0])
    NUM_ROW = int(data[1])

    pygame.init()
    pygame.display.set_caption('testing')
    DISPLAYSURFACE = pygame.display.set_mode((NUM_COL * TILESIZE, NUM_ROW * TILESIZE))

    GAMEOVER = False
    ALL_PLAYER = {}
    GRIDS = []
    COUNTER = 1
    while GAMEOVER != True:
        if (COUNTER == 1):
            data = ""
            GET_FULL_DATA = False
            while not GET_FULL_DATA:
                data += s.recv(BUFFER_SIZE)
                GET_FULL_DATA = "@" in data
            p = data.replace("#", "")
            data_split = p.split("\n")
            map_data = data_split.pop(0).split(",")
            # print ("map data= " + str(map_data))
            # print ("data_split= " + str(data_split))
        # setting up grids
            if(GRIDS == []):
                for r in range (NUM_ROW):
                    GRIDS.append([])
                    for c in range (NUM_COL):
                        new_grid = Grid()
                        new_grid.setup(TEXTURES[GRASSFLOWER], int(map_data.pop(0)), [])
                        GRIDS[r].append(new_grid)
            else:
                for r in range (NUM_ROW):
                    for c in range (NUM_COL):
                        GRIDS[r][c].updateitem(int(map_data.pop(0)))
#     ################################################################################################################
#     ######################################this part is the players #################################################
#     # we can #1: make a new list of players, and compare each of them with the old list and do stuff accordingly
#     #        #2: we can add an attribute in the player object, maybe old position? and update it when we read data
#     #  maybe #3???? but for now, I am going to make it simple and easy...
#
#         # 1 grid 4 frame
#         # make all players disappear first
        for py in ALL_PLAYER:
            ALL_PLAYER[py].present = 0
            ALL_PLAYER[py].xshift = 0
            ALL_PLAYER[py].yshift = 0
        for i in range(len(data_split)):
            if not (data_split[i] == '' or data_split[i] == '@'):
                new_player = Player()
                new_player.setup(data_split[i])
                if not(new_player.id < 0):
                    if new_player.id in ALL_PLAYER:
                        # print("already has something")
                        if ALL_PLAYER[new_player.id].coor[2] != new_player.coor[2]:
                            GRIDS[new_player.coor[1]][new_player.coor[0]].updateplayer(new_player.id, 0, 0, new_player.img)
                            ALL_PLAYER[new_player.id].updatefacing(new_player.coor[2])
                        # print("now facing " + str(new_player.coor[2]))
                        x_change = new_player.coor[0] - ALL_PLAYER[new_player.id].coor[0]
                        if x_change == NUM_COL-1 or x_change == (NUM_COL-1)*-1:
                            x_change /= (-1 * (NUM_COL-1))
                        y_change = new_player.coor[1] - ALL_PLAYER[new_player.id].coor[1]
                        if y_change == NUM_ROW-1 or y_change == (NUM_ROW-1)*-1:
                            y_change /= (-1 * (NUM_ROW-1))
                        ALL_PLAYER[new_player.id].update(COUNTER)
                        if x_change != 0:
                            # print("walk x")
                            ALL_PLAYER[new_player.id].xshift = (COUNTER * x_change / abs(x_change) *.25)
                            GRIDS[ALL_PLAYER[new_player.id].coor[1]][ALL_PLAYER[new_player.id].coor[0]].updateplayer(new_player.id, ALL_PLAYER[new_player.id].xshift, ALL_PLAYER[new_player.id].yshift, ALL_PLAYER[new_player.id].img)
                            if COUNTER == 4:
                                ALL_PLAYER[new_player.id].xshift = 0
                                GRIDS[ALL_PLAYER[new_player.id].coor[1]][ALL_PLAYER[new_player.id].coor[0]].removeplayer(new_player.id)
                                ALL_PLAYER[new_player.id].coor[0] = new_player.coor[0]
                                GRIDS[new_player.coor[1]][new_player.coor[0]].addplayer(new_player)

                        if y_change != 0:
                            print("walk y")
                            ALL_PLAYER[new_player.id].yshift = (COUNTER * y_change / abs(y_change) *.25)
                            GRIDS[ALL_PLAYER[new_player.id].coor[1]][ALL_PLAYER[new_player.id].coor[0]].updateplayer(new_player.id, ALL_PLAYER[new_player.id].xshift, ALL_PLAYER[new_player.id].yshift, ALL_PLAYER[new_player.id].img)
                            if COUNTER == 4:
                                ALL_PLAYER[new_player.id].yshift = 0
                                GRIDS[ALL_PLAYER[new_player.id].coor[1]][ALL_PLAYER[new_player.id].coor[0]].removeplayer(new_player.id)
                                ALL_PLAYER[new_player.id].coor[1] = new_player.coor[1]
                                GRIDS[new_player.coor[1]][new_player.coor[0]].addplayer(new_player)

                        blitz_grid(NUM_ROW, NUM_COL, DISPLAYSURFACE, GRIDS)
                    else:
                        print("new player " + str(new_player.id))
                        ALL_PLAYER[new_player.id] = new_player
                        GRIDS[new_player.coor[1]][new_player.coor[0]].addplayer(new_player)
        # here, need to check if the id exsist and not any more

    ################################################################################################################

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                GAMEOVER = True
        COUNTER += 1
        if COUNTER == 6:
            COUNTER = 1

        blitz_grid(NUM_ROW, NUM_COL, DISPLAYSURFACE, GRIDS)
        pygame.display.update()
        # pygame.time.delay(100)
main()
