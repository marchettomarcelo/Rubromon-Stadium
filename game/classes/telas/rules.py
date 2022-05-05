'''
Esse módulo é responsável pela lógica da tela que apresenta todas as regras ao jogador
'''

import pygame
from global_vars import *

class Rules:
    '''
    Classe Regras:
    - Tela de Regras com todas as informações da lógica de batalha
    '''
    def __init__(self):
        '''
        - Inicializa todas as variáveis necessárias (assets, nome da tela, botões)
        '''
        self.assets = {
            'font_20' : pygame.font.Font(pygame.font.get_default_font(), 20),
            'background' : pygame.image.load("assets/backgrounds/rules.png"),
            'click_sound' : pygame.mixer.Sound('assets/sons/click_sound.mp3')
            }

        self.name = RULES
        self.button_play = pygame.Rect(WIDTH/2 - 170, HEIGHT/2 + 120, 340, 70)
        self.button_back = pygame.Rect(30, HEIGHT - 50, 60, 30)

    def update_events(self, screens, window):
        '''
        Função atualiza eventos:
        - Trata todos os eventos de entrada do usuário e determina a próxima ação na batalha

        screens -> dicionário com todas as telas e variáveis principais (resultado, etc.)
        window -> variável que armazena a janela do jogo
        '''
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return QUIT
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #voltar para o menu inicial
                if self.clicked_button(self.button_back, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    return TITLE
                #ir para o menu de seleção de personagem
                if self.clicked_button(self.button_play, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    return SELECT_CHARACTER

        return RULES

    def draw(self, window):
        '''
        - Desenha todos os elementos da tela de regras

        window -> variável que armazena a janela do pygame
        '''
        window.fill((0, 0, 0))
        window.blit(self.assets['background'], (0,0))
        
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