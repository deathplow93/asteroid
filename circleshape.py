import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_detection(self, vector_2):
        dist = self.position.distance_to(vector_2.position)
        combined_radius = (self.radius - 13) + vector_2.radius
        # combined_radius_sub = (self.radius - 1) + vector_2.radius

        # print(f"dist:{dist}")
        # print(f"combined :{combined_radius}")
        # print(f"combined sub:{combined_radius_sub}")

        if dist <= combined_radius:
            # print("get hit bitch")
            return True
        else:
            # print("did not git hit bitch")
            return False
