import pygame
from minigames_pygame.atletica_minigame.classes.telas import *


def update_events(window, state):
    
    state['current_screen'] = state['screen'].update_events(state)
    if state['current_screen'] == "quit":
        return False
    
    if state['current_screen'] != state['screen'].name:

        if state['current_screen'] == "Minigame2":
            state['screen'] = Minigame2()
        
        if state['current_screen'] == "Finalizar_minigame":
            state['screen'] = Finalizar_minigame()

    return True
        

def inicializa():
    
    tela_inicial = pygame.image.load("assets/tela_inicial_mg2.png")
    tela_final = pygame.image.load("assets/tela_final_mg2.png")
    game_screen = pygame.image.load("assets/game_screen_mg2.png")

    state = {
        "screen" : Iniciar_minigame(),
        'current_screen' : "Iniciar_minigame",

        "tela_inicial" : tela_inicial,
        "tela_final": tela_final,
        "game_screen" : game_screen,
        "tempo": 0
    }


    return state


def gameloop(window, state):
    
    while update_events(window, state):
        state["screen"].draw(window, state)


def run_minigame2(window):
    atletica_music = pygame.mixer.Sound('assets\sons\musica_mingames.mp3')
    pygame.mixer.music.pause()
    pygame.mixer.Channel(1).play(atletica_music)
    
    state = inicializa()
    gameloop(window, state)

    pygame.mixer.Channel(1).stop()
    pygame.mixer.music.unpause()

    return state["tempo"]