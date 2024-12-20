import pygame
from circleshape import CircleShape
from constants import *


# Base class for game objects
class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (self.position.x, self.position.y),
            self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt
        # print(f"Shot moved to position: {self.position}")
