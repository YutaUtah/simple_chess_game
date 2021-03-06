import pygame
from .config import BLACK, ROWS, RED, SQUARE_SIZE

class Board:
    def __init__(self):
        # Store teh board in 2 dimensional array
        self.board = [[],
                      []]
        self.selected_piece = None
        self.red_left = 12
        self.white_left = 12
        self.red_kings = 0
        self.white_kings = 0

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))