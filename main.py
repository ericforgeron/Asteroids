import pygame
from constants import *
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Here is where I initialize the game to start
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #This is where I create the screen for the game
    while True:  # An infinite loop to keep the game going until a condition is met that breaks the loop
        log_state() # writes the state of the app to the log file
        for event in pygame.event.get(): # For loop used to check for input, update the game, redraw the game
           if event.type == pygame.QUIT:
               return
        pygame.Surface.fill(screen, "black") # Gives the game a black background
        pygame.display.flip() # redraws the screen with effect of user input

if __name__ == "__main__":
    main()
