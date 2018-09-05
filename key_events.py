import pygame
import sys

"""
Lib for all key events
"""

# IMAGES FOR LINK ANIMATED WALKING
img_path = './sprites/link/link_'
f_path = img_path + 'f'
b_path = img_path + 'b'
r_path = img_path + 'r'
l_path =  img_path + 'l'

f_images = [f_path+str(f)+'.png' for f in range(7)]
b_images = [b_path+str(b)+'.png' for b in range(7)]
r_images = [r_path+str(r)+'.png' for r in range(7)]
l_images = [l_path+str(l)+'.png' for l in range(7)]

class KeyEvents:
    def __init__(self, PLAYER):
        self.PLAYER = PLAYER
        self.counter = 0
        self.movement = .05

    def global_events(self):
            self.movement = .05

    def quit(self):
        pygame.quit()
        sys.exit()

    def key_down(self, pos, height):
		if (pos < height - 0.5):
			self.PLAYER.PLAYER_POS[1] += self.movement
		else:
			self.PLAYER.PLAYER_POS[1] = 0
		self.PLAYER.DIRECTION = 'd'
		self.PLAYER.SPRITE_POS = pygame.image.load(f_images[self.counter])
		self.counter = (self.counter + 1) % len(f_images)

    def key_up(self, pos, height):
		if (pos > 0):
			self.PLAYER.PLAYER_POS[1] -= self.movement
		else:
			self.PLAYER.PLAYER_POS[1] = height * 0.99
		self.PLAYER.DIRECTION = 'u'

		self.PLAYER.SPRITE_POS = pygame.image.load(b_images[self.counter])
		self.counter = (self.counter + 1) % len(b_images)

    def key_left(self, pos, width):
		if (pos > 0):
			self.PLAYER.PLAYER_POS[0] -= self.movement
		else:
			self.PLAYER.PLAYER_POS[0] = width * 0.99
		self.PLAYER.DIRECTION = 'l'

		self.PLAYER.SPRITE_POS = pygame.image.load(l_images[self.counter])
		self.counter = (self.counter + 1) % len(l_images)

    def key_right(self, pos, width):
		if (pos < width - 0.5):
			self.PLAYER.PLAYER_POS[0] += self.movement
		else:
			self.PLAYER.PLAYER_POS[0] = 0
		self.PLAYER.DIRECTION = 'r'
		self.PLAYER.SPRITE_POS = pygame.image.load(r_images[self.counter])
		self.counter = (self.counter + 1) % len(r_images)
