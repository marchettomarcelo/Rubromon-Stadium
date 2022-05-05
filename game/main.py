'''
Esse é o módulo principal do jogo, onde o loop principal ocorre
'''

import pygame
from classes.telas.select_character import SelectCharacter
from classes.telas.title_screen import Title
from classes.telas.rules import Rules
from classes.telas.battle import Battle
from classes.telas.game_over import GameOver
from global_vars import *


def initialize():
    '''
    Inicializa o pygame, o mixer, o clock e todas as variáveis principais do jogo 
    WIDTH = 640
    HEIGHT = 480
    '''
    pygame.init()

    pygame.mixer.init()
    pygame.mixer.set_num_channels(10)
    pygame.mixer.music.load('assets/sons/ambient_sound.mp3')
    pygame.mixer.music.play(-1)

    window = pygame.display.set_mode((WIDTH, HEIGHT), vsync=True)
    pygame.display.set_caption('Rubromon Stadium')
    pygame.display.set_icon(pygame.image.load("assets/atleticas/raposa.png"))
    clock = pygame.time.Clock()

    screens = {
        'screen' : Title(),
        'current_screen' : GAMEOVER,
        'player1' : '',
        'player2' : '',
        'result' : ''
    }
    
    return window, screens, clock


def finalize():
    '''
    Função finaliza o pygame
    '''
    pygame.quit()


def update_events(screens, clock):
    '''
    Função hub de mudança de telas:
    - Atualiza o FPS (60)
    - Recebe o nome da próxima tela e compara. Caso seja diferente do nome atual, troca para essa tela
      e incializa sua música

    screens -> dicionário de telas com informações de próx. tela, players e resultado
    clock -> variável que guarda o pygame.clock
    '''
    clock.tick(FPS)
    screens['current_screen'] = screens['screen'].update_events(screens, window)

    if screens['current_screen'] == QUIT:
        return False
    
    if screens['current_screen'] != screens['screen'].name:
        if screens['current_screen'] == RULES:
            screens['screen'] = Rules()
        elif screens['current_screen'] == SELECT_CHARACTER:
            screens['screen'] = SelectCharacter()
        elif screens['current_screen'] == BATTLE:
            pygame.mixer.music.load('assets/sons/battle_music.mp3')
            pygame.mixer.music.play(-1)
            screens['screen'] = Battle(screens['player1'], screens['player2'])
        elif screens['current_screen'] == GAMEOVER:
            pygame.mixer.music.load('assets/sons/victory_music.mp3')
            pygame.mixer.music.play(-1)
            screens['screen'] = GameOver(screens['result'])
        else:
            pygame.mixer.music.load('assets/sons/ambient_sound.mp3')
            pygame.mixer.music.play(-1)
            screens['screen'] = Title()

    return True


def gameloop(window, screens, clock):
    '''
    Loop principal do jogo:
    - Trata os eventos e desenha a tela

    window -> variável da tela do pygame
    screens -> dicionário de telas com informações de próx. tela, players e resultado
    clock -> variável que guarda o pygame.clock
    '''
    while update_events(screens, clock):
        screens['screen'].draw(window)



if __name__ == '__main__':
    pygame.init()
    window, screens, clock = initialize()
    gameloop(window, screens, clock)

    pygame.QUIT