import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        self.image.fill((0, 0, 0, 0))  # Transparent black

        pygame.draw.circle(
            self.image,  # surface to draw on - correct
            "white",
            (self.radius, self.radius),
            self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position
