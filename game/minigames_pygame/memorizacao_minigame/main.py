'''
Esse módulo é responsável pela lógica principal do minigame 3 (Decorar ordem / Dory Decore)
'''

from minigames_pygame.memorizacao_minigame.classes.telas import *
import pygame
import random


def inicializa():
    '''
    Inicializa todas as variáveis principais do minigame (imagens, nome da tela, tela atual, time)
    '''
    correct_sequence = []

    for i in range(5):
        correct_sequence.append(i)

    #aleatoriza sequência de números
    random.shuffle(correct_sequence)

    #imagens utilizadas
    tela_inicial = pygame.image.load("assets/minigames_images/tela_inicial_mg3.png")
    tela_final = pygame.image.load("assets/minigames_images/tela_final_mg3.png")
    tela_sequencia = pygame.image.load("assets/minigames_images/sequencia.png")

    state = {
        "screen" : Iniciar_minigame(),
        'current_screen' : "Iniciar_minigame",
        "tempo": 0,

        "tela_inicial" : tela_inicial,
        "tela_final" : tela_final,
        "tela_sequencia": tela_sequencia,

        "correct_sequence" : correct_sequence
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

        if state['current_screen'] == "Minigame3":
            state['screen'] = Minigame3(state)
        
        if state['current_screen'] == "Random_sequence":
            state['screen'] = Random_sequence()
        
        if state['current_screen'] == "Finalizar_minigame":
            state['screen'] = Finalizar_minigame()
        
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
    
def run_minigame3(window):
    '''
    Função chamada pelo jogo principal para rodar o minigame e retornar a pontuação do jogador ('tempo')
    
    window -> variável que armazena a tela do pygame
    '''
    
    atletica_music = pygame.mixer.Sound('assets/sons/musica_mingames.mp3')
    pygame.mixer.music.pause()
    pygame.mixer.Channel(2).play(atletica_music)
    
    state = inicializa()
    gameloop(window, state)

    pygame.mixer.Channel(2).stop()
    pygame.mixer.music.unpause()
    
    return state["tempo"]