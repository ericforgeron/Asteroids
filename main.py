import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Here is where I initialize the game to start
    pygame.init()
    clock = pygame.time.Clock() #this is my screen clock object
    dt = 0 # this is my delta time variable
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #This is where I create the screen for the game
    
    # Here is where I create groups for my game
    updatable = pygame.sprite.Group() # This is the group for objects that can be updated each frame
    drawable = pygame.sprite.Group() # This is the group for objects that can be drawn in each frame
    asteroids = pygame.sprite.Group() # This is the group for all the asteroids that will be hurled at my ship
    asteroidfield = pygame.sprite.Group() # This group I think will contain all the asteroids in the asteroid group

    # Here is where I create my containers
    Player.containers = (updatable, drawable) # I'm adding the Player class to these 2 groups
    Asteroid.containers = (updatable, drawable, asteroids) #I'm adding the asteroids to these 3 groups
    AsteroidField.containers = (updatable) # Asteroid Field only needs updatable because it's not a drawable object

    # Create our player and our asteroid field:
    player  = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # this is the instance of the player
    game_asteroidfield = AsteroidField()

    # This loop here is the game.  We draw a frame, accept input, then redraw the frame based on that input
    while True:  # An infinite loop to keep the game going until a condition is met that breaks the loop
        log_state() # writes the state of the app to the log file
        for event in pygame.event.get(): # For loop used to check for input, update the game, redraw the game
           if event.type == pygame.QUIT:
               return
        updatable.update(dt) # Replaced player.update() with this so all objects that need updating get updated at the same time
        for asteroid in asteroids:
           if player.collides_with(asteroid):
               log_event("player_hit")
               print(f"Game over!")
               sys.exit()
        screen.fill("black") # makes the background black
        # Replacing player.draw(screen) with this for loop to redraw all the objects on the screen instead of just the player spaceship 
        for object in drawable:
           object.draw(screen)
        pygame.display.flip() # redraws the screen with effect of user input
        # clock.tick(60) # this is how I run the game at 60 frames per second
        dt = clock.tick(60) / 1000 # saving the delta time between each loop in seconds (milliseconds/1000)
        clock.tick(60)

if __name__ == "__main__":
    main()
