#Imports
import pygame
import numpy as np
from button import *

# pygame setup
pygame.init()

#Constants
HOT_PINK = (255, 87, 51) #Color RGB
CELL_UPDATE_FPS = 10 #FPS at which cells will update

#Screen setup
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
step = 1

#Buttons
quit_button = Button("Quit", 20, 20, 50, 30, "grey")
patterns_button = Button("Patterns", 10, 70, 70, 30, "grey")

#Cell array setup
rows = int(SCREEN_HEIGHT / 20)
cols = int(SCREEN_WIDTH / 20)
cells = np.zeros((rows, cols), dtype=bool)


#Update cell to draw a glider to canvas
def drawGlider(cells, row, col):
    cells[row][col] = True
    if col-1>=0:
        cells[row][col-1] = True
    if col - 2 >= 0 and row - 1 >= 0:
        cells[row-1][col-2] = True
    if row-1 >= 0:
        cells[row-1][col] = True
    if row-2 >= 0:
        cells[row-2][col] = True

last_update_cell_time = pygame.time.get_ticks()

while running:


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    #Draw cells on screen
    for i in range(rows):
        for j in range(cols):
            if cells[i][j]:
                x = j * 20
                y = i * 20
                pygame.draw.rect(screen, "black", (x, y, 20, 20))

    #update cells based on an fps separate from runtime fps
    current_time = pygame.time.get_ticks()
    update_interval = 1000 / CELL_UPDATE_FPS
    if current_time - last_update_cell_time > update_interval:
        #Update cells to automata rules
        new_cells = cells.copy()
        for i in range(rows):
            for j in range(cols):
                #how many adjacent neighbors current cell has
                neighbors = 0
                #top left
                if i-1 >= 0 and j-1 >=0:
                    if cells[i-1][j-1]:
                        neighbors += 1
                #top middle
                if i-1 >= 0:
                    if cells[i-1][j]:
                        neighbors += 1
                #top right
                if i-1 >= 0 and j+1 <= cols - 1:
                    if cells[i-1][j+1]:
                        neighbors += 1
                #left
                if j-1 >= 0:
                    if cells[i][j-1]:
                        neighbors += 1
                #right
                if j+1 <= cols - 1:
                    if cells[i][j+1]:
                        neighbors += 1
                #bottom left
                if i+1 <= rows - 1 and j-1 >= 0:
                    if cells[i+1][j-1]:
                        neighbors += 1
                #bottom middle
                if i+1 <= rows - 1:
                    if cells[i+1][j]:
                        neighbors += 1
                #bottom right
                if i+1 <= rows - 1 and j+1 <= cols - 1:
                    if cells[i+1][j+1]:
                        neighbors += 1

                #update cell based on neighbors
                #BIRTH: current cell is off and has 3 neighbors
                if not cells[i][j] and neighbors == 3:
                    new_cells[i][j] = True
                #SURVIVAL: cell is on and neighbors is 2 or 3
                elif cells[i][j] and (neighbors == 2 or neighbors == 3):
                    pass
                #DEATH: cell is on and neighbors is not 3
                elif cells[i][j] and neighbors != 3:
                    new_cells[i][j] = False
     
        cells = new_cells
        last_update_cell_time = pygame.time.get_ticks()


    #Current mouse position in array
    m_x, m_y = pygame.mouse.get_pos()
    curr_row = 0
    curr_col = 0
    if m_x < 20:
        curr_col = 0
    else:
        curr_col = int(m_x / 20)
    if m_y < 20:
        curr_row = 0
    else:
        curr_row = int(m_y / 20)

    pygame.draw.rect(screen, HOT_PINK, (curr_col*20, curr_row*20, 20,20), width=2)


    # #Only time step when space is pressed
    # flag = True
    # while flag:
        # for event in pygame.event.get():
            # if event.type == pygame.QUIT:
                # running = False
                # flag = False
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # flag = False
                # step += 1
                # print(step)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            cells = np.zeros((rows, cols), dtype=bool)
        elif event.type == pygame.MOUSEBUTTONDOWN and quit_button.is_clicked():
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawGlider(cells, curr_row, curr_col)


    #Draw in Buttons on top of screen
    quit_button.draw(screen)
    patterns_button.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    #limit FPS to whatever
    clock.tick(60) 

pygame.quit()
