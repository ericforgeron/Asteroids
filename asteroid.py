import pygame
import random # imported this in Chapter 4 Lesson 6 so I can create new angles for asteroids in the .split() method
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
    def split(self):
        self.kill() # We kill the asteroid because it's been hit by a bullet.  We will then create 2 smaller asteroids
                    # to take its place
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(90)
            new_velocity2 = self.velocity.rotate(-90)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_velocity1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            # asteroid1.velocity = new_velocity1 * 1.2
            asteroid2.velocity = new_velocity2 * 1.2
