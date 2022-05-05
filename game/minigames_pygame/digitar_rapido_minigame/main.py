'''
Esse módulo é responsável pela lógica principal do minigame 1 (Digita Rápido / RataType)
'''

import pygame
from minigames_pygame.digitar_rapido_minigame.classes.telas import *


def inicializa():
    '''
    Inicializa todas as variáveis principais do minigame (imagens, nome da tela, tela atual, time) 
    '''
    fundo = pygame.image.load("assets/minigames_images/tela_inicial_mg1.png")
    fundo2 = pygame.image.load("assets/minigames_images/tela_final_mg1.png")

    state = {
        "screen" : Inicialize_minigame(),
        'current_screen' : "Inicialize_minigame",
        "fundo" : fundo,
        "fundo2" : fundo2,
        "tempo": 0
    }

    return state


def update_events(window, state):
    '''
    Função hub de mudança de telas:
    - Recebe o nome da próxima tela e compara. Caso seja diferente do nome atual, troca para essa tela

    state -> dicionário de telas com informações de próx. tela, players e resultado
    window -> armazena tela do pygame
    '''
    
    state['current_screen'] = state['screen'].update_events(state)
    if state['current_screen'] == "quit":
        return False
    
    if state['current_screen'] != state['screen'].name:

        if state['current_screen'] == "Minigame1":
            state['screen'] = Minigame1()
        
        if state['current_screen'] == "Finalize_minigame":
            state['screen'] = Finalize_minigame()
        
    return True


def gameloop(window, state):
    '''
    Loop principal do Minigame
    - Cura os eventos e desenha a tela correspondente
    '''
    while update_events(window, state):
        state["screen"].draw(window, state)
    
def run_minigame1(window):
    '''
    Função chamada pelo jogo principal para rodar o minigame e retornar a pontuação do jogador ('tempo')
    '''

    atletica_music = pygame.mixer.Sound('assets/sons/musica_mingames.mp3')
    pygame.mixer.music.pause()
    pygame.mixer.Channel(0).play(atletica_music)
    
    state = inicializa()
    gameloop(window, state)

    pygame.mixer.Channel(0).stop()
    pygame.mixer.music.unpause()
    
    return state["tempo"]