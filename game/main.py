import pygame
from classes.telas.select_character import SelectCharacter
from classes.telas.title_screen import Title
from classes.telas.rules import Rules
from classes.telas.battle import Battle
from classes.telas.game_over import GameOver
from global_vars import *


def initialize():
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
    pygame.quit()


def update_events(screens, clock):
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
    while update_events(screens, clock):
        screens['screen'].draw(window)



if __name__ == '__main__':
    pygame.init()
    window, screens, clock = initialize()
    gameloop(window, screens, clock)

    pygame.QUIT