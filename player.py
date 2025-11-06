import pygame

from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
     def __init__(self, x, y, shots_group):
         super().__init__(x, y, PLAYER_RADIUS)
         # self.radius = radius
         self.rotation = 0
         self.shots_group = shots_group

     # in the player class
     def triangle(self):
         forward = pygame.Vector2(0, 1).rotate(self.rotation)
         right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
         a = self.position + forward * self.radius
         b = self.position - forward * self.radius - right
         c = self.position - forward * self.radius + right
         return [a, b, c]

     def draw(self, screen):
         pygame.draw.polygon(screen, "white", self.triangle(), 2)

     def rotate(self, dt):
         self.rotation += PLAYER_TURN_SPEED * dt

     def update(self, dt):
         keys = pygame.key.get_pressed()

         if keys[pygame.K_a]:
             return self.rotate(dt * -1)
         if keys[pygame.K_d]:
             return self.rotate(dt)
         if keys[pygame.K_w]:
             return self.move(dt)
         if keys[pygame.K_s]:
             return self.move(dt * -1)
         if keys[pygame.K_SPACE]:
             return self.shoot(dt)

     def move(self, dt):
         forward = pygame.Vector2(0, 1).rotate(self.rotation)
         self.position += forward * PLAYER_SPEED * dt

     def shoot(self, dt):
         direction_vector = pygame.Vector2(0, 1).rotate(self.rotation)
         velocity = direction_vector * PLAYER_SHOOT_SPEED * dt
         bullet = Shot(self.position, velocity)
         self.shots_group.add(bullet)
