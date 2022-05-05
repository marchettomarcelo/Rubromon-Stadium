import pygame
from global_vars import *

class Title:
    def __init__(self):
        self.assets = {
            'background' : pygame.image.load("assets/backgrounds/title_screen.png")
            }

        self.name = TITLE
        self.button_play = pygame.Rect(WIDTH/2 - 100, HEIGHT/2 + 80, 200, 75)
        self.button_quit = pygame.Rect(10, 15, 30, 30)

    def update_events(self, screens, window):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return QUIT
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if self.clicked_button(self.button_play, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    return RULES
                if self.clicked_button(self.button_quit, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    return QUIT

        return TITLE

    def draw(self, window):
        window.fill((0, 0, 0))
        window.blit(self.assets['background'], (0,0))
        
        pygame.display.update()
    
    def clicked_button(self, button, coordx, coordy):
        if button[0] <= coordx <= button[0] + button[2] and button[1] <= coordy <= button[1] + button[3]:
            return True
        else:
            return False