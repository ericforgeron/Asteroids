import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
     def __init__(self, position, velocity):
          super().__init__(position, position, SHOT_RADIUS)
          self.position = position
          self.radius = SHOT_RADIUS
          self.velocity = velocity

     def draw(self, screen):
         pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

     def update(self, dt):
         # forward = self.position.rotate(self.rotation)
         self.position += self.velocity * dt
         self.rect.center = self.position 
