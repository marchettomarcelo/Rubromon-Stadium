import pygame
from minigames_pygame.digitar_rapido_minigame.classes.telas import *


def update_events(window, state):
    
    state['current_screen'] = state['screen'].update_events(state)
    if state['current_screen'] == "quit":
        return False
    
    if state['current_screen'] != state['screen'].name:

        if state['current_screen'] == "Minigame1":
            state['screen'] = Minigame1()
        
        if state['current_screen'] == "Finalize_minigame":
            state['screen'] = Finalize_minigame()
        
    return True
        

def inicializa():
    fundo = pygame.image.load("assets/tela_inicial_mg1.png")
    fundo2 = pygame.image.load("assets/tela_final_mg1.png")

    state = {
        "screen" : Inicialize_minigame(),
        'current_screen' : "Inicialize_minigame",
        "fundo" : fundo,
        "fundo2" : fundo2,
        "tempo": 0
    }

    return state


def gameloop(window, state):
    while update_events(window, state):
        state["screen"].draw(window, state)
    
def run_minigame1(window):
    atletica_music = pygame.mixer.Sound('assets\sons\musica_mingames.mp3')
    pygame.mixer.music.pause()
    pygame.mixer.Channel(0).play(atletica_music)
    
    state = inicializa()
    gameloop(window, state)

    pygame.mixer.Channel(0).stop()
    pygame.mixer.music.unpause()
    return state["tempo"]