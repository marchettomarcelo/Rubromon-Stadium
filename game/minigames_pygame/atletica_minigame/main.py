'''
Esse módulo é responsável pela lógica principal do minigame 2 (Atleticano / Space Invaders)
'''

import pygame
from minigames_pygame.atletica_minigame.classes.telas import *


def inicialize():
    '''
    Inicializa todas as variáveis principais do minigame (imagens, nome da tela, tela atual, time) 
    '''
    
    tela_inicial = pygame.image.load("assets/minigames_images/tela_inicial_mg2.png")
    tela_final = pygame.image.load("assets/minigames_images/tela_final_mg2.png")
    game_screen = pygame.image.load("assets/minigames_images/game_screen_mg2.png")

    screens = {
        "screen" : Iniciar_minigame(),
        'next_screen' : "Iniciar_minigame",

        "tela_inicial" : tela_inicial,
        "tela_final": tela_final,
        "game_screen" : game_screen,
        "time": 0
    }


    return screens


def update_events(window, screens):
    '''
    Função hub de mudança de telas:
    - Recebe o nome da próxima tela e compara. Caso seja diferente do nome atual, troca para essa tela

    screens -> dicionário de telas com informações de próx. tela, players e resultado
    window -> armazena tela do pygame
    '''
    
    screens['next_screen'] = screens['screen'].update_events(screens)
    if screens['next_screen'] == "quit":
        return False
    
    if screens['next_screen'] != screens['screen'].name:

        if screens['next_screen'] == "Minigame2":
            screens['screen'] = Minigame2()
        
        if screens['next_screen'] == "Finalizar_minigame":
            screens['screen'] = Finalizar_minigame()

    return True
        

def gameloop(window, screens):
    '''
    Loop principal do Minigame
    - Cura os eventos e desenha a tela correspondente
    '''
    while update_events(window, screens):
        screens["screen"].draw(window, screens)


def run_minigame2(window):
    '''
    Função chamada pelo jogo principal para rodar o minigame e retornar a pontuação do jogador ('time')
    '''
    music_atletica = pygame.mixer.Sound('assets/sons/musica_mingames.mp3')
    pygame.mixer.music.pause()
    pygame.mixer.Channel(1).play(music_atletica)
    
    screens = inicialize()
    gameloop(window, screens)

    pygame.mixer.Channel(1).stop()
    pygame.mixer.music.unpause()

    return screens["time"]