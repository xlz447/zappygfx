import random


class Player:
	def __init__(self):
		self.id = -1 # player id
		self.team  = -1 # team id
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