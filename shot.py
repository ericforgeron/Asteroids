# This file contains the Shot class for bullets in the Asteroids game.  It was created in Chapter 4 Lesson 3
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

# The Shot class is just like the Asteroid class
class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)
        #self.position = [x, y]
        self.radius = SHOT_RADIUS

    # in the Shot class 
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
