import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

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

    def split(self):

        random_spin = random.uniform(20, 50)
        vect_1 = self.velocity.rotate(random_spin)
        vect_2 = self.velocity.rotate(-random_spin)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        smol_ast_list = []

        if new_radius >= ASTEROID_MIN_RADIUS:
            ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast_2.velocity = vect_1 * 1.1
            ast_3 = Asteroid(self.position.x, self.position.y, new_radius)
            ast_3.velocity = vect_2 * 1.2

            smol_ast_list.extend([ast_2, ast_3])

        self.kill()  # Remove the original asteroid
        return smol_ast_list
