'''
Esse módulo é responsável pela lógica principal do minigame 4 (Precisão / Desvio Padrão)
'''

from minigames_pygame.precisao_minigame.classes.telas import *
import pygame


def inicialize():
    '''
    Inicializa todas as variáveis principais do minigame (imagens, nome da tela, tela atual, time)
    '''
    tela_inicial = pygame.image.load("assets/minigames_images/tela_inicial_mg4.png")
    tela_final = pygame.image.load("assets/minigames_images/tela_final_mg4.png")
    game_screen = pygame.image.load("assets/minigames_images/game_screen_mg4.png")

    state = {
        "screen" : Inicialize_minigame(),
        'current_screen' : "Iniciar_minigame",
        "distance_from_green": 320,

        "tela_inicial" : tela_inicial,
        "tela_final" : tela_final,
        "game_screen" : game_screen,
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

        if state['current_screen'] == "Minigame4":
            state['screen'] = Minigame4(state)
        
        if state['current_screen'] == "Finalize_minigame":
            state['screen'] = Finalize_minigame()
        
    return True


def gameloop(window, state):
    '''
    Loop principal do Minigame
    - Cura os eventos e desenha a tela correspondente

    window -> variável que armazena tela do pygame
    state -> dicionário com todas as variáveis de controle do jogo
    '''
    while update_events(window, state):
        state["screen"].draw(window, state)
    
def run_minigame4(window):
    '''
    Função chamada pelo jogo principal para rodar o minigame e retornar a pontuação do jogador ('tempo')

    window -> variável que armazena a tela do pygame
    '''

    atletica_music = pygame.mixer.Sound('assets/sons/musica_mingames.mp3')
    pygame.mixer.music.pause()
    pygame.mixer.Channel(3).play(atletica_music)
    
    state = inicialize()
    gameloop(window, state)

    pygame.mixer.Channel(3).stop()
    pygame.mixer.music.unpause()
    
    return state["distance_from_green"]