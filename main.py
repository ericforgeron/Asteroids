import pygame
from constants import *
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Here is where I initialize the game to start
    pygame.init()
    clock = pygame.time.Clock() #this is my screen clock object
    dt = 0 # this is my delta time variable
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #This is where I create the screen for the game
    while True:  # An infinite loop to keep the game going until a condition is met that breaks the loop
        log_state() # writes the state of the app to the log file
        for event in pygame.event.get(): # For loop used to check for input, update the game, redraw the game
           if event.type == pygame.QUIT:
               return
        pygame.Surface.fill(screen, "black") # Gives the game a black background
        pygame.display.flip() # redraws the screen with effect of user input
        clock.tick(60) # this is how I run the game at 60 frames per second
        dt = clock.tick() / 1000 # saving the delta time between each loop in seconds (milliseconds/1000)

if __name__ == "__main__":
    main()
