# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from logger import log_state
from player import *
from asteroidfield import *
from sys import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screenClock = pygame.time.Clock()
    dt = 0
    # creating groups for my game
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Creating containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # creating player for my game and setting the player in both groups
    newPlayer = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, shots_group = shots)
    # creating a new asteroid field object
    asteroidField = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        updatable.update(dt)
        for shot in shots:
            shot.update(dt)
        for asteroid in asteroids:
            if newPlayer.collision(asteroid):
               print(f"Game over!")
               sys.exit()
        for frame in drawable:
            frame.draw(screen)
        pygame.display.flip()
        dt = screenClock.tick(60)/1000


if __name__ == "__main__":
    main()
