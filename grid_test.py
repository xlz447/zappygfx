import random

class Grid:
    def __init__(self):
        self.background = None
        self.items = [] #[{x0, y0, 0}, {x1, y1,1}, ...., {x6, y6,1}] # will always be length 7
        self.players = [] #[x0, y0, image], [x1, y1, image],......] # might be empty
        for i in range(0, 7):
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
    def setup(self, img, item, players):
        self.background = img
        #print("setting up: " + str(bin(item)))
        for i in range(6,-1,-1):
            self.items[i][2] = item % 2
            item = item // 2
        # print(self.items)
        # set up players (do we still need this now??)
        self.players = []

    def updateitem(self, item):
        #print("updating up: " + str(bin(item)))
        for i in range(6,-1,-1):
            self.items[i][2] = item % 2
            item = item / 2
        #print(self.items)
    """
    Funciton to add a player
    Args:
        img: the image used for this player(preloaded using pygames.image.load)

    Returns:
        None

    Raises:
        Nothing for now
    """
    def addplayer(self, player):
#        repeated = True
#        while repeated:
#            repeated = False
#            x = random.random()
#            y = random.random()
#            for it in self.items:
#                if it[2] == 1 and it[0] - x < 0.05 and it[1] - y < 0.05:
#                    repeated = True
#            for pl in self.players:
#                if pl[0] - x < 0.05 and pl[1] - y < 0.05:
#                    repeated = True
        x = 0.5
        y = 0.5
        self.players.append([x, y, player])

    """
    Funciton to remove a player
    Args:
        targetid: the id of the player

    Returns:
        None

    Raises:
        Nothing for now
    """
    def removeplayer(self, targetid):
        for pl in self.players:
            if pl[2].id == targetid:
                self.players.remove(pl)

    """
    Funciton to update a player
    Args:
        targetid: the id of the player

    Returns:
        None

    Raises:
        Nothing for now
    """
    def updateplayer(self, targetid, xshift, yshift):
        for i in range(len(self.players)):
            if self.players[i][2].id == targetid:
                self.players[i][2].xshift = xshift
                self.players[i][2].yshift = yshift
