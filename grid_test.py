import random

class Grid:
	def __init__(self):
		self.background = None
		self.items = [] #[{x0, y0, 0}, {x1, y1,1}, ...., {x6, y6,1}] # will always be length 7
		self.players = [] #[{x0, y0, image}, {x1, y1, image},......] # might be empty
		for i in range(0, 7):
			self.items.append([random.random(), random.random(), 0]) # set up the random xy coordinates and start with no item
	
	
	"""
	Funciton to setup a grid
	Args:
    	img: the background image used for this grid(preloaded using pygames.image.load)
    	items: an int ranging from 0 to 255 representing the items that will apppear in this grid
		player: data type TBD, (tuple?) contains information of the team and the orientation of all players on the grid

	Returns:
    	None

	Raises:
    	Nothing for now
	"""
	def setup(self, img, items, players):
		self.background = img
		for i in range(6, -1, -1):
			self.items[i][1] = items % 2
			items = items / 2
			
		# test items
		for j in range(0, 7):
			print("Item " + str(j) + " is " + str(self.items[j][1]))

		# set up players
		self.players = []

new_grid = Grid()
new_grid.setup(None, 127, [])
print("Should be 1 1 1 1 1 1 1")

new_grid.setup(None, 111, [])
print("Should be 1 1 0 1 1 1 1")