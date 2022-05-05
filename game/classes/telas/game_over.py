'''
Esse módulo é responsável pela lógica da tela de Fim de Jogo e todas as suas ações
'''

import pygame
from global_vars import *

class GameOver:
    '''
    Classe Fim de Jogo:
    - Tela de Fim de Jogo com informação de quem ganhou a partida
    '''
    def __init__(self, result):
        '''
        - Inicia todaas as variáveis necessárias para a tela (assets, resultado, nome da tela)

        result -> str com o nome do personagem vencedor da batalha
        '''
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
                if self.clicked_button(self.button_play, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    pygame.mixer.Channel(9).play(self.assets['click_sound'])
                    return TITLE

        return GAMEOVER

    def draw(self, window):
        '''
        - Desenha todos os elementos da tela final

        window -> variável que armazena a janela do pygame
        '''
        window.fill((0, 0, 0))
        window.blit(self.assets['background'], (0,0))
        
        text = self.assets['font_60'].render(f"{self.result}", True, (0, 255, 20))
        text_rect = text.get_rect()
        window.blit(text, (WIDTH/2 - text_rect[2]/2, HEIGHT/2 - 30))

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