import pygame

pygame.init()
pygame.display.set_caption('testing')
DISPLAYSURFACE = pygame.display.set_mode((300, 300))

OVER = False
item = pygame.image.load('./sprites/team0/t0_f0.png')
x = 0
y = 0

while not OVER:
	DISPLAYSURFACE.fill((0, 0, 0))
	DISPLAYSURFACE.blit(item, (x, y))
	x += 10
	y += 10

	for event in pygame.event.get():
	    keys = pygame.key.get_pressed()
	    if event.type == pygame.QUIT:
	        OVER = True
	pygame.display.update()
