import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
     def __init__(self):
          # super().__init__(x, y)
          self.position = (pygame.math.Vector2(0, 1))
          self.radius = SHOT_RADIUS
          # self.velocity = pygame.math.Vector2(0, 1)

     def draw(self, screen):
         pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

     def update(self, dt):
         forward = self.position.rotate(self.rotation)
         self.position += forward * PLAYER_SHOOT_SPEED * dt
