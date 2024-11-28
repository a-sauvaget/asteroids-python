import pygame

from constants import *
from player import Player

def main():
	pygame.init()
	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius = PLAYER_RADIUS)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	
	# Game loop
	while True:
		# This will check if the user has closed the window and exit the game loop if they do. 
		# It will make the window's close button work.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")

		player.draw(screen)
		player.update(dt)

		pygame.display.flip()

		# limit the framerate to 60 FPS
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
