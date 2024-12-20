import sys
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)


	asteroid_field = AsteroidField()
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

		for obj in drawable:
			obj.draw(screen)
		
		for obj in updatable:
			obj.update(dt)

		for asteroid in asteroids:
			if asteroid.collides_with(player) == True:
				print("Game over !")
				sys.exit()

			for shot in shots:
				if shot.collides_with(asteroid):
					asteroid.split()
					shot.kill()
			

		pygame.display.flip()

		# limit the framerate to 60 FPS
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
