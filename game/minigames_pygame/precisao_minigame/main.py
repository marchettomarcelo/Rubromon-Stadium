from minigames_pygame.precisao_minigame.classes.telas import *
import pygame
import random

def update_events(window, state):
    
    state['current_screen'] = state['screen'].update_events(state)
    if state['current_screen'] == "quit":
        return False
    
    if state['current_screen'] != state['screen'].name:

        if state['current_screen'] == "Minigame4":
            state['screen'] = Minigame4(state)
        
        if state['current_screen'] == "Finalize_minigame":
            state['screen'] = Finalize_minigame()
        
    return True



def inicialize():
    tela_inicial = pygame.image.load("assets/tela_inicial_mg4.png")
    tela_final = pygame.image.load("assets/tela_final_mg4.png")
    game_screen = pygame.image.load("assets/game_screen_mg4.png")

    state = {
        "screen" : Inicialize_minigame(),
        'current_screen' : "Iniciar_minigame",
        "distance_from_green": 320,

        "tela_inicial" : tela_inicial,
        "tela_final" : tela_final,
        "game_screen" : game_screen,
    }


    return state


def gameloop(window, state):
    while update_events(window, state):
        state["screen"].draw(window, state)
    
def run_minigame4(window):
    atletica_music = pygame.mixer.Sound('assets/sons/musica_mingames.mp3')
    pygame.mixer.music.pause()
    pygame.mixer.Channel(3).play(atletica_music)
    
    state = inicialize()
    gameloop(window, state)

    pygame.mixer.Channel(3).stop()
    pygame.mixer.music.unpause()
    
    return state["distance_from_green"]