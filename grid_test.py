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
	def setup(self, img, items, players):
		self.background = img
		for i in range(6, -1, -1):
			self.items[i][2] = items % 2
			items = items / 2
		# set up players (do we still need this now??)
		self.players = []

	"""
	Funciton to add a player
	Args:
    	img: the image used for this player(preloaded using pygames.image.load)
    	
	Returns:
    	None

	Raises:
    	Nothing for now
	"""
	def addplayer(self, img):
		repeated = True
		while repeated:
			repeated = False
			x = random.random()
			y = random.random()
			for it in self.items:
				if it[2] == 1 and it[0] - x < 0.05 and it[1] - y < 0.05:
					repeated = True
			for pl in self.players:
				if pl[0] - x < 0.05 and pl[1] - y < 0.05:
					repeated = True
		self.players.append([x, y, img])