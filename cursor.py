import pygame

#Constants
HOT_PINK = (255, 87, 51) #Color RGB


class Cursor:
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.curr_col = 0
        self.curr_row = 0
        screen_info = pygame.display.Info()
        self.max_rows = (screen_info.current_w / 20)
        self.max_cols = (screen_info.current_h / 20)

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


    #This is going to be tedious, kms
    def drawHighlight(self, current_pattern):
        if current_pattern == "Block":
            pygame.draw.rect(self.screen, HOT_PINK, (self.curr_col*20, self.curr_row*20, 20,20), width=2)
            pygame.draw.rect(self.screen, HOT_PINK, ((self.curr_col-1)*20, self.curr_row*20, 20,20), width=2)
            pygame.draw.rect(self.screen, HOT_PINK, ((self.curr_col-1)*20, (self.curr_row-1)*20, 20,20), width=2)
            pygame.draw.rect(self.screen, HOT_PINK, (self.curr_col*20, (self.curr_row-1)*20, 20,20), width=2)
        elif current_pattern == "Blinker":
            pygame.draw.rect(self.screen, HOT_PINK, (self.curr_col*20, self.curr_row*20, 20,20), width=2)
            pygame.draw.rect(self.screen, HOT_PINK, (self.curr_col*20, (self.curr_row-1)*20, 20,20), width=2)
            pygame.draw.rect(self.screen, HOT_PINK, (self.curr_col*20, (self.curr_row+1)*20, 20,20), width=2)
        elif current_pattern == "Glider":
            pygame.draw.rect(self.screen, HOT_PINK, (self.curr_col*20, self.curr_row*20, 20,20), width=2)
            pygame.draw.rect(self.screen, HOT_PINK, ((self.curr_col-1)*20, self.curr_row*20, 20,20), width=2)
            pygame.draw.rect(self.screen, HOT_PINK, ((self.curr_col-2)*20, (self.curr_row-1)*20, 20,20), width=2)
            pygame.draw.rect(self.screen, HOT_PINK, (self.curr_col*20, (self.curr_row-1)*20, 20,20), width=2)
            pygame.draw.rect(self.screen, HOT_PINK, (self.curr_col*20, (self.curr_row-2)*20, 20,20), width=2)

    #This is going to be even more tedious fuuuukkkkkk
    def placePattern(self, cells, current_pattern):
        if current_pattern == "Block":
            cells[self.curr_row][self.curr_col] = True
            if self.curr_col-1>=0:
                cells[self.curr_row][self.curr_col-1] = True
            if self.curr_row-1 >= 0:
                cells[self.curr_row-1][self.curr_col] = True
            if self.curr_row-1 >= 0 and self.curr_col >= 0:
                cells[self.curr_row-1][self.curr_col-1] = True
        if current_pattern == "Blinker":
            cells[self.curr_row][self.curr_col] = True
            if self.curr_row+1 < self.max_rows:
                cells[self.curr_row+1][self.curr_col] = True
            if self.curr_row-1 >= 0:
                cells[self.curr_row-1][self.curr_col] = True
        if current_pattern == "Glider":
            cells[self.curr_row][self.curr_col] = True
            if self.curr_col-1>=0:
                cells[self.curr_row][self.curr_col-1] = True
            if self.curr_col - 2 >= 0 and self.curr_row - 1 >= 0:
                cells[self.curr_row-1][self.curr_col-2] = True
            if self.curr_row-1 >= 0:
                cells[self.curr_row-1][self.curr_col] = True
            if self.curr_row-2 >= 0:
                cells[self.curr_row-2][self.curr_col] = True

