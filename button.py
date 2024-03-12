import pygame

class Button:
    def __init__(self, text, x, y, width, height, color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        #Hover effect
        m_x, m_y = pygame.mouse.get_pos()
        if m_x >= self.x and m_x <= self.x + self.width and m_y >= self.y and m_y <= self.y + self.height:
            #Draw button slighly enlarged
            pygame.draw.rect(screen, self.color, (self.x-5, self.y-5, self.width+10, self.height+10))
        else:
            #Draw button normal size
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        #Add text to button
        font = pygame.font.SysFont("Arial", 16)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

    def is_clicked(self):
        m_x, m_y = pygame.mouse.get_pos()
        withinBounds = m_x >= self.x and m_x <= self.x + self.width and m_y >= self.y and m_y <= self.y + self.height
        return withinBounds



