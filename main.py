import pygame
import random
import math

pygame.init()

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