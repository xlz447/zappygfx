import random


# player_id,team_id,x,y,orientation,linemate,deraumere,sibur,mendiane,phiras,thystame,food
class Player:
	def __init__(self, playerid, teamid, x,y,orientation,linemate,deraumere,sibur,mendiane,phiras,thystame,food):
		self.id = playerid
		self.items = [] #array of int # will always be length 7
		self.coor = [0, 0]
		
		for i in range(0, 7):
			self.items.append([random.random(), random.random(), 0]) # set up the random xy coordinates and start with no item


	"""
	Funciton to change a grid
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
		for i in range(6, -1, -1):
			self.items[i][2] = items % 2
			items = items / 2
		# set up players (do we still need this now??)
		self.players = []




