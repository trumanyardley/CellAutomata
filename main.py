#Imports
import pygame
import numpy as np
from button import *
from cursor import *

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
quit_button = Button("Quit", 12,20, 20, 50, 30, (128,128,128))
stills_button = Button("Stills", 12,10, 70, 70, 30, (128,128,128))
oscillators_button = Button("Oscillators", 12,10, 130, 70, 30, (128,128,128))
spaceships_button = Button("Spaceships", 12,10, 190, 70, 30, (128,128,128))


#Cell array setup
rows = int(SCREEN_HEIGHT / 20)
cols = int(SCREEN_WIDTH / 20)
cells = np.zeros((rows, cols), dtype=bool)

#Time
last_update_cell_time = pygame.time.get_ticks()

#Cursor object used for placing and drawing highlight
cursor = Cursor(screen)

#Patterns
stills = ["Block", "Beehive", "Loaf", "Boat", "Tub"]
oscillators = ["Blinker", "Toad", "Beacon", "Pulsar", "Penta-Decathon"]
spaceships = ["Glider", "Lwss", "Mwss", "Hwss"]

#Current pattern for each group
current_pattern_group = "Stills" #Current group based on button selected
current_still = "Block"
current_oscillator = "Blinker"
current_spaceship = "Glider"

def updatePattern():
    if current_pattern_group == "Stills":
        return current_still
    elif current_pattern_group == "Oscillators":
        return current_oscillator
    else:
        return current_spaceship


#Main runtime loop
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


    #update cursor to current mouse position
    cursor.update()

    #update current pattern based on which group is selected
    current_pattern = updatePattern()

    #draw current pattern selected highlight on canvas
    cursor.drawHighlight(current_pattern)

    #Event detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            cells = np.zeros((rows, cols), dtype=bool)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            if current_pattern_group == "Stills":
                currInd = stills.index(current_still)
                current_still = stills[(currInd + 1) % len(stills)]
                current_pattern = current_still 
            elif current_pattern_group == "Oscillators":
                currInd = oscillators.index(current_oscillator)
                current_oscillator = oscillators[(currInd + 1) % len(oscillators)]
                current_pattern = current_oscillator
            else:
                currInd = spaceships.index(current_spaceship)
                current_spaceship = spaceships[(currInd + 1) % len(spaceships)]
                current_pattern = current_spaceship
        elif event.type == pygame.MOUSEBUTTONDOWN and quit_button.is_clicked():
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and stills_button.is_clicked():
            current_pattern_group = "Stills"
        elif event.type == pygame.MOUSEBUTTONDOWN and oscillators_button.is_clicked():
            current_pattern_group = "Oscillators"
        elif event.type == pygame.MOUSEBUTTONDOWN and spaceships_button.is_clicked():
            current_pattern_group = "Spaceships"
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            cursor.placePattern(cells, current_pattern) 


    #Draw in Buttons on top of screen
    quit_button.draw(screen, current_pattern_group)
    stills_button.draw(screen, current_pattern_group)
    oscillators_button.draw(screen, current_pattern_group)
    spaceships_button.draw(screen, current_pattern_group)

    # flip() the display to put your work on screen
    pygame.display.flip()

    #limit FPS to whatever
    clock.tick(60) 

pygame.quit()
