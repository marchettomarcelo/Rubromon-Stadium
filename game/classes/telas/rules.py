import pygame
from global_vars import *

class Rules:
    def __init__(self):
        self.assets = {
            'font_20' : pygame.font.Font(pygame.font.get_default_font(), 20),
            'background' : pygame.image.load("assets/backgrounds/rules.png"),
            'click_sound' : pygame.mixer.Sound('assets/sons/click_sound.mp3')
            }

        self.name = RULES
        self.button_play = pygame.Rect(WIDTH/2 - 170, HEIGHT/2 + 120, 340, 70)
        self.button_back = pygame.Rect(30, HEIGHT - 50, 60, 30)

    def update_events(self, screens, window):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return QUIT
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if self.clicked_button(self.button_back, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    return TITLE
                if self.clicked_button(self.button_play, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    return SELECT_CHARACTER

        return RULES

    def draw(self, window):
        window.fill((0, 0, 0))
        window.blit(self.assets['background'], (0,0))
        
        pygame.display.update()
    
    def clicked_button(self, button, coordx, coordy):
        if button[0] <= coordx <= button[0] + button[2] and button[1] <= coordy <= button[1] + button[3]:
            return True
        else:
            return False