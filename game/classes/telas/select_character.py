'''
Esse módulo é responsável pela lógica da tela de seleção de personagens para ambos jogadores
'''

import pygame
from global_vars import *


class SelectCharacter():
    '''
    Classe Seleciona Personagem:
    - Tela de seleção de personagem para os dois jogadores  
    '''
    def __init__(self):
        '''
        - Inicializa todas as variáveis necessárias (assets, nome da tela, nome dos personagens
          escolhidos, etc.)
        '''
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

        #variável para impedir que jogador segura a tecla
        self.clicked_key = False

        #menus com personagens
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
        '''
        Função atualiza eventos:
        - Trata todos os eventos de entrada do usuário e determina a próxima ação na batalha

        screens -> dicionário com todas as telas e variáveis principais (resultado, etc.)
        window -> variável que armazena a janela do jogo
        '''
        self.menu = self.menus_list[self.current_menu]

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return QUIT

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if self.clicked_button(self.button_back, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    #retorna para a tela de regras
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    return RULES

            if ev.type == pygame.KEYDOWN and not self.clicked_key:
                #seleciona item no menu e salva o personagem para o jogador correspondente 
                if ev.key == pygame.K_SPACE or ev.key == pygame.K_RETURN:
                    if self.current_menu == 'Player 1':
                        pygame.mixer.Channel(9).play(self.assets['click_sound'])
                        self.player1 = self.menu[self.current_item]
                        self.current_menu = 'Player 2'
                    
                    #condição que impede que o jogador 2 selecione o mesmo personagem que o jogador 1
                    elif self.player1 != self.menu[self.current_item]:
                        pygame.mixer.Channel(9).play(self.assets['click_sound'])
                        self.player2 = self.menu[self.current_item]

                        screens['player1'] = self.player1
                        screens['player2'] = self.player2
                        return BATTLE
                    else:
                        pygame.mixer.Channel(9).play(self.assets['cant_click_sound'])
                
                #retorna para o menu anterior
                if ev.key == pygame.K_ESCAPE:
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    if self.current_menu == 'Player 1':
                        return RULES
                    else:
                        self.player1 = ''
                        self.current_menu = 'Player 1'
                
                #navega pelo menu
                if ev.key == pygame.K_UP:
                    self.current_item -= 1
                    if self.current_item < 0:
                        self.current_item = len(self.menu) - 1
                if ev.key == pygame.K_DOWN:
                    self.current_item += 1
                    if self.current_item >= len(self.menu):
                        self.current_item = 0

            if ev.type == pygame.KEYUP:
                self.clicked_key = False

        return self.name
    
    def draw(self, window):
        '''
        - Desenha todos os elementos da tela de regras

        window -> variável que armazena a janela do pygame
        '''
        window.fill((0, 0, 0))
        window.blit(self.assets['background'], (0, 0))

        #desenha menu
        text_image = self.assets['font_20'].render(self.current_menu, True, (255, 200, 200))
        window.blit(text_image, (50, 125))

        for i in range(len(self.menu)):
            text = self.menu[i]

            #pinta de vermelho o personagem que já foi selecionado
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
        '''
        Função Clicou Botão:
        - Retorna se o usuário clicou com o mouse em um certo botão

        button -> pygame.rect com retângulo do botão
        coordx -> coordenada x do clique do mouse
        coordy -> coordenada y do clique do mouse
        '''
        if button[0] <= coordx <= button[0] + button[2] and button[1] <= coordy <= button[1] + button[3]:
            return True
        else:
            return False