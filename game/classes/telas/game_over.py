import pygame
from global_vars import *

class GameOver:
    def __init__(self, result):
        self.assets = {
            'font_20' : pygame.font.Font(pygame.font.get_default_font(), 20),
            'font_12' : pygame.font.Font(pygame.font.get_default_font(), 12),
            'font_60' : pygame.font.Font(pygame.font.get_default_font(), 60),
            'background' : pygame.image.load("assets/backgrounds/gameover.png"),
            'click_sound' : pygame.mixer.Sound('assets/sons/click_sound.mp3')
            }

        self.result = result
        self.name = GAMEOVER

        self.button_play = pygame.Rect(485, 423, 135, 35)
    
    def update_events(self, screens, window):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return QUIT
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if self.clicked_button(self.button_play, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    return TITLE

        return GAMEOVER

    def draw(self, window):
        window.fill((0, 0, 0))
        window.blit(self.assets['background'], (0,0))
        
        text = self.assets['font_60'].render(f"{self.result}", True, (0, 255, 20))
        text_rect = text.get_rect()
        window.blit(text, (WIDTH/2 - text_rect[2]/2, HEIGHT/2 - 30))

        pygame.display.update()
    
    def clicked_button(self, button, coordx, coordy):
        if button[0] <= coordx <= button[0] + button[2] and button[1] <= coordy <= button[1] + button[3]:
            return True
        else:
            return False