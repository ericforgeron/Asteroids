# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screenClock = pygame.time.Clock()
    dt = 0
    # creating containers for my game
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # creating player for my game and setting the player in both groups
    # newPlayer.containers = (updatable, drawable)
    newPlayer = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    # newPlayer.containers = (updatable, drawable)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        updatable.update(dt)
        for frame in drawable:
            frame.draw(screen)
        pygame.display.flip()
        dt = screenClock.tick(60)/1000


if __name__ == "__main__":
    main()
