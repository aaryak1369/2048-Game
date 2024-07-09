import pygame
import random
import math

pygame.init()

# Constants Defined

# speed: frames per second 
FPS = 60

WIDTH = 800
HEIGHT = 800

ROWS = 4
COLS = 4

RECT_WIDTH = WIDTH // COLS
RECT_HEIGHT = HEIGHT // ROWS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BG_COLOR = (205,192,180)
FONT_COLOR = (119, 110, 101)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("2048-Game")

FONT = pygame.font.SysFont("sans", 60, bold=True)

MOVE_VELOCITY = 20


def main(window):
    # regulates speed of the game loop
    clock = pygame.time.Clock()
    run = True

    # tiles = generate_tiles()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_tiles(window, tiles, clock, "left")
                if event.key == pygame.K_RIGHT:
                    move_tiles(window, tiles, clock, "right")
                if event.key == pygame.K_UP:
                    move_tiles(window, tiles, clock, "up")
                if event.key == pygame.K_DOWN:
                    move_tiles(window, tiles, clock, "down")

        draw(window, tiles)

    pygame.quit()

if __name__ == "__main__":
    main(WINDOW)