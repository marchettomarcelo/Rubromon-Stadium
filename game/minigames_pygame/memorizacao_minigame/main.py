from minigames_pygame.memorizacao_minigame.classes.telas import *
import pygame
import random

def update_events(window, state):
    
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



def inicializa():
    correct_sequence = []

    for i in range(5):
        correct_sequence.append(i)

    random.shuffle(correct_sequence)


    tela_inicial = pygame.image.load("assets/tela_inicial_mg3.png")
    tela_final = pygame.image.load("assets/tela_final_mg3.png")
    tela_sequencia = pygame.image.load("assets/sequencia.png")

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


def gameloop(window, state):
    while update_events(window, state):
        state["screen"].draw(window, state)
    
def run_minigame3(window):
    atletica_music = pygame.mixer.Sound('assets/sons/musica_mingames.mp3')
    pygame.mixer.music.pause()
    pygame.mixer.Channel(2).play(atletica_music)
    
    state = inicializa()
    gameloop(window, state)

    pygame.mixer.Channel(2).stop()
    pygame.mixer.music.unpause()
    return state["tempo"]