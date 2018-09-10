import random

TEAM0 = 0
TEAM1 = 1
TEAM2 = 2
TEAM3 = 3

# 0 for b; 1 for f; 2 for l; 3 for r
IMAGE = {
    TEAM0: [pygame.image.load('./sprites/link0/link_b0.png'), pygame.image.load('./sprites/link0/link_f0.png'), pygame.image.load('./sprites/link0/link_l0.png'), pygame.image.load('./sprites/link0/link_r0.png')],
    TEAM1: [pygame.image.load('./sprites/link1/link_b0.png'), pygame.image.load('./sprites/link1/link_f0.png'), pygame.image.load('./sprites/link1/link_l0.png'), pygame.image.load('./sprites/link1/link_r0.png')],
    TEAM2: [pygame.image.load('./sprites/link2/link_b0.png'), pygame.image.load('./sprites/link2/link_f0.png'), pygame.image.load('./sprites/link2/link_l0.png'), pygame.image.load('./sprites/link2/link_r0.png')],
	TEAM3: [pygame.image.load('./sprites/link3/link_b0.png'), pygame.image.load('./sprites/link3/link_f0.png'), pygame.image.load('./sprites/link3/link_l0.png'), pygame.image.load('./sprites/link3/link_r0.png')]
}

class Player:
	def __init__(self):
		self.id = -1 # player id
		self.team  = -1 # team id
		self.img = None
		self.coor = [0, 0, 0] # x,y coordinate and orientation
		self.items = [0, 0, 0, 0, 0, 0, 0] #array of int, will always be length 7		


	"""
	Funciton to setup a player
	Args:
		player_data: a string containing <player_id,team_id,x,y,orientation,linemate,deraumere,sibur,mendiane,phiras,thystame,food>
		separated by commas

	Returns:
    	None

	Raises:
    	Nothing for now
	"""
	def setup(self, player_data):
		info = player_data.split(",")
		self.id = int(info[0])
		self.team = int(info[1])
		self.img = IMAGE[self.team]
		for i in range(3):
		self.coor[i] = int(info[i + 2])
	
	
	"""
	Function to update a player, updates the player's info to new info(will have to cooperate with the graphics for moving and so on)
	Args:
		player_data: a string containing <player_id,team_id,x,y,orientation,linemate,deraumere,sibur,mendiane,phiras,thystame,food>
		separated by commas

	Returns:
    	None

	Raises:
    	Nothing for now
	"""
	def update(self, player_data):
		print("Implement later")