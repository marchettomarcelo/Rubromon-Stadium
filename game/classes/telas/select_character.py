import pygame
from global_vars import *


class SelectCharacter():
    def __init__(self):
        self.assets = {
            'font_20' : pygame.font.Font(pygame.font.get_default_font(), 20),
            'font_12' : pygame.font.Font(pygame.font.get_default_font(), 12),
            'background' : pygame.image.load('assets/backgrounds/select_character.png'),
            'click_sound' : pygame.mixer.Sound('assets/sons/click_sound.mp3'),
            'cant_click_sound' : pygame.mixer.Sound('assets/sons/error_click.mp3')
            }

        self.name = SELECT_CHARACTER
        self.player1 = ''
        self.player2 = ''

        self.clicked_key = False

        self.menus_list = {
            'Player 1' : ['Diabo Loiro', 'Toshi Coxinha', 'Insper Boy', 'Raposa Loka'],
            'Player 2' : ['Diabo Loiro', 'Toshi Coxinha', 'Insper Boy', 'Raposa Loka']
        }

        self.button_back = pygame.Rect(30, HEIGHT - 50, 60, 30)

        self.text_index = 0
        self.current_menu = 'Player 1'
        self.current_item = 0
        self.menu = self.menus_list[self.current_menu]
    
    def update_events(self, screens, window):
        self.menu = self.menus_list[self.current_menu]

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return QUIT
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if self.clicked_button(self.button_back, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    return RULES
            if ev.type == pygame.KEYDOWN and not self.clicked_key:
                if ev.key == pygame.K_SPACE or ev.key == pygame.K_RETURN:
                    if self.current_menu == 'Player 1':
                        pygame.mixer.Channel(9).play(self.assets['click_sound'])
                        self.player1 = self.menu[self.current_item]
                        self.current_menu = 'Player 2'
                    elif self.player1 != self.menu[self.current_item]:
                        pygame.mixer.Channel(9).play(self.assets['click_sound'])
                        self.player2 = self.menu[self.current_item]

                        screens['player1'] = self.player1
                        screens['player2'] = self.player2
                        return BATTLE
                    else:
                        pygame.mixer.Channel(9).play(self.assets['cant_click_sound'])
                if ev.key == pygame.K_ESCAPE:
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    if self.current_menu == 'Player 1':
                        return RULES
                    else:
                        self.player1 = ''
                        self.current_menu = 'Player 1'
                if ev.key == pygame.K_UP:
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    self.current_item -= 1
                    if self.current_item < 0:
                        self.current_item = len(self.menu) - 1
                if ev.key == pygame.K_DOWN:
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    self.current_item += 1
                    if self.current_item >= len(self.menu):
                        self.current_item = 0
            if ev.type == pygame.KEYUP:
                self.clicked_key = False

        return self.name
    
    def draw(self, window):
        window.fill((0, 0, 0))
        window.blit(self.assets['background'], (0, 0))

        text_image = self.assets['font_20'].render(self.current_menu, True, (255, 200, 200))
        window.blit(text_image, (50, 125))

        for i in range(len(self.menu)):
            text = self.menu[i]

            if text == self.player1:
                color = (255, 200, 200)
            else:
                color = (255, 255, 255)

            if i == self.current_item:
                window.blit(characters[text]['skins'][1], (WIDTH/2 + 35, HEIGHT/2 - 30))
                text = '> ' + text
            else:
                text = '  ' + text
            
            text_image = self.assets['font_20'].render(text, True, color)
            window.blit(text_image, (50, 125 + (i + 1) * 25))

        pygame.display.update()

    def clicked_button(self, button, coordx, coordy):
        if button[0] <= coordx <= button[0] + button[2] and button[1] <= coordy <= button[1] + button[3]:
            return True
        else:
            return False