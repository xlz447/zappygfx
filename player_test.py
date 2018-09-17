import random, pygame
import pprint

TEAM0 = 0
TEAM1 = 1
TEAM2 = 2
TEAM3 = 3
TEAM4 = 4
TEAM5 = 5

# IMAGES FOR ANIMATED WALKING
# TEAM_ID, ORIENTATION, FRAME
IMAGEPATH = [[[0 for k in xrange(4)] for j in xrange(4)] for i in xrange(6)]
for i in range(6):
	IMAGEPATH[i][0] = ['./sprites/team'+str(i)+'/t'+str(i)+'_f'+str(f)+'.png' for f in range(4)]
	IMAGEPATH[i][1] = ['./sprites/team'+str(i)+'/t'+str(i)+'_l'+str(f)+'.png' for f in range(4)]
	IMAGEPATH[i][2] = ['./sprites/team'+str(i)+'/t'+str(i)+'_r'+str(f)+'.png' for f in range(4)]
	IMAGEPATH[i][3] = ['./sprites/team'+str(i)+'/t'+str(i)+'_b'+str(f)+'.png' for f in range(4)]
#pprint.pprint(IMAGEPATH)

# 0 for f; 1 for l; 2 for r; 3 for b
IMAGE = {
    TEAM0: [pygame.image.load('./sprites/team0/t0_f0.png'), pygame.image.load('./sprites/team0/t0_l0.png'), pygame.image.load('./sprites/team0/t0_r0.png'), pygame.image.load('./sprites/team0/t0_b0.png')],
    TEAM1: [pygame.image.load('./sprites/team1/t1_f0.png'), pygame.image.load('./sprites/team1/t1_l0.png'), pygame.image.load('./sprites/team1/t1_r0.png'), pygame.image.load('./sprites/team1/t1_b0.png')],
    TEAM2: [pygame.image.load('./sprites/team2/t2_f0.png'), pygame.image.load('./sprites/team2/t2_l0.png'), pygame.image.load('./sprites/team2/t2_r0.png'), pygame.image.load('./sprites/team2/t2_b0.png')],
	TEAM3: [pygame.image.load('./sprites/team3/t3_f0.png'), pygame.image.load('./sprites/team3/t3_l0.png'), pygame.image.load('./sprites/team3/t3_r0.png'), pygame.image.load('./sprites/team3/t3_b0.png')],
	TEAM4: [pygame.image.load('./sprites/team4/t4_f0.png'), pygame.image.load('./sprites/team4/t4_l0.png'), pygame.image.load('./sprites/team4/t4_r0.png'), pygame.image.load('./sprites/team4/t4_b0.png')],
	TEAM5: [pygame.image.load('./sprites/team5/t5_f0.png'), pygame.image.load('./sprites/team5/t5_l0.png'), pygame.image.load('./sprites/team5/t5_r0.png'), pygame.image.load('./sprites/team5/t5_b0.png')],
}

class Player:
	def __init__(self):
		self.id = -1 # player id
		self.team  = -1 # team id
		self.img = None
		self.coor = [0, 0, 0] # x,y coordinate and orientation
		self.items = [0, 0, 0, 0, 0, 0, 0] #array of int, will always be length 7
		self.present = 1
		self.xshift = 0
		self.yshift = 0
#		self.movespeed = 0.25
#		self.counter = 0



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

#		print("Get info: ")
#		print(info)

		self.id = int(info[0])

#		print("Created player " + str(self.id))

		self.team = int(info[1])

#		print(" at team " + str(self.team))

		for cor in range(3):
			self.coor[cor] = int(info[cor + 2])

#		print(" at coor (" + str(self.coor[0]) + ", " + str(self.coor[1]) + ")")
#		print(" facing " + str(self.coor[2]))

		self.img = IMAGE[self.team][self.coor[2]-1]
		for item in range(7):
			self.items[item] = int(info[item + 5])

#		print("owning these items: ")
#		print(self.items)

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
	def update(self, cnt):
		print (IMAGEPATH[self.team][self.coor[2] - 1][(cnt - 1) % 4])
		self.img = pygame.image.load(IMAGEPATH[self.team][self.coor[2] - 1][(cnt - 1) % 4])
