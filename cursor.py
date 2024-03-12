import pygame

#Constants
HOT_PINK = (255, 87, 51) #Color RGB

patterns = {
        "Block": [(0, 0), (-1, 0), (0, -1), (-1, -1)],
        "Beehive": [(0, 0), (-1, -1), (-2, -1), (-3, 0), (-1, 1), (-2, 1)],
        "Loaf": [(0, 0), (-1, 0), (-2, 1), (-1, 2), (0, 3), (1, 2), (1, 1)],
        "Boat": [(0, 0), (1, 0), (0, 1), (2, 1), (1, 2)],
        "Tub": [(-1, 0), (1, 0), (0, -1), (0, 1)],
        "Blinker": [(0, 0), (0, -1), (0, 1)],
        "Toad": [(0, 0), (-1, 0), (-2, 0), (-1, -1), (0, -1), (1, -1)],
        "Beacon": [(0, 0), (1, 0), (0, 1), (3, 3), (3, 2), (2, 3)],
        "Pulsar": [(-2, -1), (-3, -1), (-4, -1), (2, -1), (3, -1), (4, -1),
                   (-2, 1), (-3, 1), (-4, 1), (2, 1), (3, 1), (4, 1),
                   (-1, 2), (-1, 3), (-1, 4), (-1, -2), (-1, -3), (-1, -4),
                   (1, 2), (1, 3), (1, 4), (1, -2), (1, -3), (1, -4),
                   (2, -6), (3, -6), (4, -6), (-2, -6), (-3, -6), (-4, -6),
                   (2, 6), (3, 6), (4, 6), (-2, 6), (-3, 6), (-4, 6),
                   (6, -2), (6, -3), (6, -4), (-6, -2), (-6, -3), (-6, -4),
                   (6, 2), (6, 3), (6, 4), (-6, 2), (-6, 3), (-6, 4)],
        "Penta-Decathon": [(0, 0), (-1, 0), (1, 0), (0, 1), (-1, 1), (1, 1),
                           (0, -2), (-1, -2), (1, -2), (0, 3), (-1, 3), (1, 3),
                           (0, -3), (0, -4), (0, -5), (0, 4), (0, 5), (0, 6),
                           (-1, 6), (1, 6), (1, -5), (-1, -5)],
        "Glider": [(0, 0), (-1, 0), (-2, -1), (0, -1), (0, -2)],
        "Lwss": [(0, 0), (0, -1), (0, -2), (1, -3), (1, 0), (2, 0), (3, 0), (4, -1), (4, -3)],
        "Mwss": [(0, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0), (0, 1), (0, 2), (-1, 3), (-3, 4), (-5, 1), (-5, 3)],
        "Hwss": [(0, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (0, -1), (0, -2), (-6, -1), (-6, -3), (-1, -3), (-3, -4), (-4, -4)]
        # Add more patterns as needed
    }

class Cursor:
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.curr_col = 0
        self.curr_row = 0
        screen_info = pygame.display.Info()
        self.max_rows = (screen_info.current_h / 20)
        self.max_cols = (screen_info.current_w / 20)

    #Update cursor x,y position to where mouse is and the row and columns its at
    def update(self):
        self.x, self.y = pygame.mouse.get_pos()
        if self.x < 20:
            self.curr_col = 0
        else:
            self.curr_col = int(self.x / 20)
        if self.y < 20:
            self.curr_row = 0
        else:
            self.curr_row = int(self.y / 20)


    def drawHighlight(self, current_pattern):
        for rel_row, rel_col in patterns.get(current_pattern, []):
                pygame.draw.rect(self.screen, HOT_PINK, ((self.curr_col + rel_col) * 20, (self.curr_row + rel_row) * 20, 20, 20), width=2)

    def placePattern(self, cells, current_pattern):
        for rel_row, rel_col in patterns.get(current_pattern, []):
            row, col = self.curr_row + rel_row, self.curr_col + rel_col
            if 0 <= row < self.max_rows and 0 <= col < self.max_cols:
                cells[row][col] = True
