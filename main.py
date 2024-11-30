import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()
    keep_game_running = True
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    dt = 0

    while keep_game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_game_running = False
                return print("Game has Quit")

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if obj.collision_detection(player.position) == True:
                print("game over")
                keep_game_running = False

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
