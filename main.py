import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
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

            player.update(dt)
            screen.fill("black")

            player.draw(screen)
            pygame.display.flip()
            dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
