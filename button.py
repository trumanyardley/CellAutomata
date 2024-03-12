import pygame

#Constants
DARK_GREY = (50,50,50)

class Button:
    def __init__(self, text, fontsize, x, y, width, height, color):
        self.text = text
        self.fontsize = fontsize
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen, current_pattern_group):
        #change color of box to show it is selected
        if current_pattern_group == self.text:
            self.color = DARK_GREY
        else:
            self.color = (128,128,128)
        #Hover effect
        m_x, m_y = pygame.mouse.get_pos()
        if m_x >= self.x and m_x <= self.x + self.width and m_y >= self.y and m_y <= self.y + self.height:
            #Draw button slighly enlarged
            pygame.draw.rect(screen, self.color, (self.x-5, self.y-5, self.width+10, self.height+10))
        else:
            #Draw button normal size
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        #Add text to button
        font = pygame.font.SysFont("Arial", self.fontsize)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

    def is_clicked(self):
        m_x, m_y = pygame.mouse.get_pos()
        withinBounds = m_x >= self.x and m_x <= self.x + self.width and m_y >= self.y and m_y <= self.y + self.height
        return withinBounds



