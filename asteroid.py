import pygame
import random # imported this in Chapter 4 Lesson 6 so I can create the .split() method
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event #imported this in Chapter 4 Lesson 6 so I create a log record of the asteroid split

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # self.position  = [x, y]
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    # Created this method in Chapter 4 Lesson 6 to split asteroids when they get hit by a bullet
    def split():
        self.kill() # We kill the asteroid because it's been hit by a bullet.  We will then create 2 smaller asteroids
                    # to take its place
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random.uniform(20, 50)
